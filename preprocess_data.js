const fs = require('fs');
const path = require('path');

const DATASETS = path.join(__dirname, 'datasets_cyt');
const OUT = path.join(__dirname, 'data');
fs.mkdirSync(OUT, { recursive: true });

function parseCSV(file, sep = ',') {
  const content = fs.readFileSync(file, 'utf-8');
  const lines = content.split('\n').filter(l => l.trim());
  if (lines.length === 0) return [];
  const headers = lines[0].split(sep).map(h => h.trim().replace(/"/g, ''));
  return lines.slice(1).map(line => {
    const values = line.split(sep).map(v => v.trim().replace(/^"|"$/g, ''));
    const obj = {};
    headers.forEach((h, i) => obj[h] = values[i] || '');
    return obj;
  });
}

console.log('=== Preprocesando datos para Dashboard CyT ===\n');

// =============================================
// 1. SICYTAR - Personal por año
// =============================================
console.log('[1/10] Investigadores por año...');
const researchersByYear = {};
const researchersByGender = {};

for (let year = 2011; year <= 2019; year++) {
  const file = path.join(DATASETS, '01_SICYTAR', 'personal_cyt', `personas_${year}.csv`);
  if (!fs.existsSync(file)) continue;
  const data = parseCSV(file, ';');
  researchersByYear[year] = data.length;
  
  // Gender distribution
  const male = data.filter(d => d.sexo_id === '1').length;
  const female = data.filter(d => d.sexo_id === '2').length;
  const other = data.length - male - female;
  researchersByGender[year] = { male, female, other };
}
fs.writeFileSync(path.join(OUT, 'researchers_by_year.json'), JSON.stringify(researchersByYear, null, 2));
fs.writeFileSync(path.join(OUT, 'researchers_by_gender.json'), JSON.stringify(researchersByGender, null, 2));
console.log(`  → ${Object.keys(researchersByYear).length} años procesados`);

// =============================================
// 2. SICYTAR - By discipline (from latest year)
// =============================================
console.log('[2/10] Investigadores por disciplina...');
const latestFile = path.join(DATASETS, '01_SICYTAR', 'personal_cyt', 'personas_2019.csv');
if (fs.existsSync(latestFile)) {
  const data = parseCSV(latestFile, ';');
  const byDiscipline = {};
  data.forEach(d => {
    const disc = d.disciplina_maximo_grado_academico_id || 'Sin datos';
    byDiscipline[disc] = (byDiscipline[disc] || 0) + 1;
  });
  
  // Get grado academico distribution
  const byGrado = {};
  data.forEach(d => {
    const grado = d.maximo_grado_academico_id || 'Sin datos';
    byGrado[grado] = (byGrado[grado] || 0) + 1;
  });
  
  // Age distribution
  const byAge = {};
  data.forEach(d => {
    const age = parseInt(d.edad);
    if (isNaN(age)) return;
    const bracket = age < 30 ? '<30' : age < 40 ? '30-39' : age < 50 ? '40-49' : age < 60 ? '50-59' : '60+';
    byAge[bracket] = (byAge[bracket] || 0) + 1;
  });
  
  fs.writeFileSync(path.join(OUT, 'researchers_by_discipline.json'), JSON.stringify(byDiscipline, null, 2));
  fs.writeFileSync(path.join(OUT, 'researchers_by_degree.json'), JSON.stringify(byGrado, null, 2));
  fs.writeFileSync(path.join(OUT, 'researchers_by_age.json'), JSON.stringify(byAge, null, 2));
  console.log(`  → ${Object.keys(byDiscipline).length} disciplinas, ${Object.keys(byGrado).length} grados, ${Object.keys(byAge).length} rangos etarios`);
}

// =============================================
// 3. SICYTAR - Producciones por año
// =============================================
console.log('[3/10] Producciones científicas por año...');
const productionsByYear = {};
for (let year = 2011; year <= 2018; year++) {
  const files = fs.readdirSync(path.join(DATASETS, '01_SICYTAR', 'producciones')).filter(f => f.includes(year.toString()) && f.endsWith('.csv'));
  if (files.length === 0) continue;
  const file = path.join(DATASETS, '01_SICYTAR', 'producciones', files[0]);
  const data = parseCSV(file, ';');
  productionsByYear[year] = data.length;
}
fs.writeFileSync(path.join(OUT, 'productions_by_year.json'), JSON.stringify(productionsByYear, null, 2));
console.log(`  → ${Object.keys(productionsByYear).length} años`);

// =============================================
// 4. SICYTAR - Proyectos por fuente
// =============================================
console.log('[4/10] Proyectos por fuente...');
const projectsBySource = {};
const projectsByYear = {};
const projDir = path.join(DATASETS, '01_SICYTAR', 'proyectos');
const projFiles = fs.readdirSync(projDir).filter(f => f.endsWith('.csv'));
for (const f of projFiles) {
  const yearMatch = f.match(/(\d{4})/);
  const year = yearMatch ? yearMatch[1] : 'unknown';
  const data = parseCSV(path.join(projDir, f), ';');
  projectsByYear[year] = data.length;
  data.forEach(d => {
    const source = d.proyecto_fuente || 'Sin datos';
    projectsBySource[source] = (projectsBySource[source] || 0) + 1;
  });
}
fs.writeFileSync(path.join(OUT, 'projects_by_source.json'), JSON.stringify(projectsBySource, null, 2));
fs.writeFileSync(path.join(OUT, 'projects_by_year.json'), JSON.stringify(projectsByYear, null, 2));
console.log(`  → ${Object.keys(projectsBySource).length} fuentes, ${Object.keys(projectsByYear).length} años`);

// =============================================
// 5. ENACOM - Internet Fija
// =============================================
console.log('[5/10] Internet Fija (ENACOM)...');
const internetFile = path.join(DATASETS, '03_ENACOM', 'internet_fija', 'Internet_Fija_Accesos_BAF_Provincias-csv.csv');
if (fs.existsSync(internetFile)) {
  const data = parseCSV(internetFile);
  
  // By province (latest year)
  const latestYear = Math.max(...data.map(d => parseInt(d.anio)).filter(y => !isNaN(y)));
  const byProvince = {};
  data.filter(d => parseInt(d.anio) === latestYear && parseInt(d.trimestre) === 4).forEach(d => {
    byProvince[d.provincia] = parseInt(d.banda_ancha_fija) || 0;
  });
  
  // Evolution by year
  const byYearQuarter = {};
  data.forEach(d => {
    const key = `${d.anio}-Q${d.trimestre}`;
    byYearQuarter[key] = (byYearQuarter[key] || 0) + (parseInt(d.total) || 0);
  });
  
  fs.writeFileSync(path.join(OUT, 'internet_by_province.json'), JSON.stringify(byProvince, null, 2));
  fs.writeFileSync(path.join(OUT, 'internet_evolution.json'), JSON.stringify(byYearQuarter, null, 2));
  console.log(`  → ${Object.keys(byProvince).length} provincias, ${Object.keys(byYearQuarter).length} períodos`);
}

// =============================================
// 6. ENACOM - Móvil
// =============================================
console.log('[6/10] Comunicaciones Móviles (ENACOM)...');
const mobileFile = path.join(DATASETS, '03_ENACOM', 'comunicaciones_moviles', 'Comunicaciones_Móviles_Accesos-csv.csv');
const mobilePenFile = path.join(DATASETS, '03_ENACOM', 'comunicaciones_moviles', 'Comunicaciones_Móviles_Penetracion-csv.csv');
const mobileData = {};

if (fs.existsSync(mobileFile)) {
  const data = parseCSV(mobileFile);
  data.forEach(d => {
    const key = `${d.anio}-Q${d.trimestre}`;
    mobileData[key] = { 
      pospago: parseInt(d.pospago) || 0, 
      prepago: parseInt(d.prepago) || 0, 
      total: parseInt(d.operativos) || 0 
    };
  });
}
if (fs.existsSync(mobilePenFile)) {
  const data = parseCSV(mobilePenFile);
  data.forEach(d => {
    const key = `${d.anio}-Q${d.trimestre}`;
    if (mobileData[key]) mobileData[key].penetracion = parseFloat(d.accesos_100_hab) || 0;
  });
}
fs.writeFileSync(path.join(OUT, 'mobile.json'), JSON.stringify(mobileData, null, 2));
console.log(`  → ${Object.keys(mobileData).length} períodos`);

// =============================================
// 7. ARSAT - REFEFO
// =============================================
console.log('[7/10] ARSAT REFEFO...');
const refefoFile = path.join(DATASETS, '04_ARSAT', 'puntos_refefo', 'Puntos_de_conexión_a_la_Red_Federal_de_Fibra_Óptica.csv');
if (fs.existsSync(refefoFile)) {
  const data = parseCSV(refefoFile, ';');
  const byProvince = {};
  const byStatus = {};
  data.forEach(d => {
    const prov = d.PROVINCIA || 'Sin datos';
    const status = d.ESTADO || 'Sin datos';
    byProvince[prov] = (byProvince[prov] || 0) + 1;
    byStatus[status] = (byStatus[status] || 0) + 1;
  });
  fs.writeFileSync(path.join(OUT, 'refefo.json'), JSON.stringify({ byProvince, byStatus, total: data.length }, null, 2));
  console.log(`  → ${data.length} nodos, ${Object.keys(byProvince).length} provincias`);
}

// =============================================
// 8. DACYTAR Summary
// =============================================
console.log('[8/10] DACYTAR resumen...');
const dacytarSummary = path.join(DATASETS, '00_DACYTAR', '_summary.json');
if (fs.existsSync(dacytarSummary)) {
  const data = JSON.parse(fs.readFileSync(dacytarSummary));
  const byDiscipline = {};
  for (const d of data.disciplines) {
    byDiscipline[d.name] = d.found;
  }
  fs.writeFileSync(path.join(OUT, 'dacytar.json'), JSON.stringify({ total: data.total_found, byDiscipline }, null, 2));
  console.log(`  → ${data.total_found} datasets, ${Object.keys(byDiscipline).length} disciplinas`);
}

// =============================================
// 9. Instituciones CyT
// =============================================
console.log('[9/10] Instituciones CyT...');
const instFile = path.join(DATASETS, '01_SICYTAR', 'instituciones', 'organizaciones.csv');
if (fs.existsSync(instFile)) {
  const data = parseCSV(instFile, ';');
  const byType = {};
  data.forEach(d => {
    const tipo = d.tipo_institucion_id || 'Sin datos';
    byType[tipo] = (byType[tipo] || 0) + 1;
  });
  fs.writeFileSync(path.join(OUT, 'institutions.json'), JSON.stringify({ total: data.length, byType }, null, 2));
  console.log(`  → ${data.length} instituciones, ${Object.keys(byType).length} tipos`);
}

// =============================================
// 10. KPIs Summary
// =============================================
console.log('[10/10] KPIs...');
const kpis = {
  researchers_2019: researchersByYear[2019] || researchersByYear[2018] || 0,
  total_productions: Object.values(productionsByYear).reduce((a,b) => a+b, 0),
  total_projects: Object.values(projectsByYear).reduce((a,b) => a+b, 0),
  dacytar_datasets: JSON.parse(fs.readFileSync(path.join(OUT, 'dacytar.json'))).total,
  institutions: JSON.parse(fs.readFileSync(path.join(OUT, 'institutions.json'))).total,
};
fs.writeFileSync(path.join(OUT, 'kpis.json'), JSON.stringify(kpis, null, 2));
console.log(`  → KPIs generados`);

console.log('\n=== PREPROCESAMIENTO COMPLETO ===');
console.log(`Archivos generados en: ${OUT}`);
fs.readdirSync(OUT).forEach(f => console.log(`  ${f}: ${(fs.statSync(path.join(OUT, f)).size / 1024).toFixed(1)} KB`));
