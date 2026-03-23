#!/usr/bin/env python3
"""
Extrae texto de los PDFs de proyectos CyT y genera cyt_bills_data.json
V3: Extracción mejorada de autores y bloques políticos.
"""

import csv
import json
import re
from pathlib import Path
from datetime import datetime

try:
    import fitz  # PyMuPDF
except ImportError:
    print("ERROR: pip install pymupdf")
    exit(1)

# ─── EJES TEMATICOS ──────────────────────────────────────────────
EJES = [
    {
        "key": "Nuclear y Energía", "icon": "⚛️", "color": "#dc2626",
        "title_keywords": ["nuclear", "nucleoeléctrica", "atómic", "reactor", "uranio", "cnea", "na-sa", "atucha", "embalse", "smr"],
        "text_keywords": ["nuclear", "nucleoeléctrica", "atómic", "reactor", "uranio", "cnea", "energía atómica", "radiactiv"],
        "min_title_score": 1, "min_text_score": 5,
    },
    {
        "key": "Espacio y Antártida", "icon": "🚀", "color": "#0891b2",
        "title_keywords": ["espacio", "espacial", "satélite", "antártida", "antártic", "conae", "arsat", "órbita", "lanzador"],
        "text_keywords": ["espacial", "satélite", "antártida", "antártic", "conae", "arsat", "órbita", "lanzador", "cohete", "base antártica"],
        "min_title_score": 1, "min_text_score": 4,
    },
    {
        "key": "Tecnologías Cuánticas", "icon": "🔮", "color": "#7c3aed",
        "title_keywords": ["cuántic", "quantum", "qubit"],
        "text_keywords": ["cuántic", "quantum", "computación cuántica", "qubit", "criptografía cuántica", "tecnologías cuánticas"],
        "min_title_score": 1, "min_text_score": 3,
    },
    {
        "key": "Biotecnología", "icon": "🧬", "color": "#16a34a",
        "title_keywords": ["biotecnología", "biotecnológic", "genómic", "genétic", "génic", "bioeconomía", "terapia génica", "crispr", "renbiotech"],
        "text_keywords": ["biotecnología", "biotecnológic", "genómic", "genétic", "edición génica", "crispr", "transgénic", "bioeconomía", "bioinformática", "terapia génica"],
        "min_title_score": 1, "min_text_score": 4,
    },
    {
        "key": "Neuroderechos", "icon": "🧠", "color": "#a855f7",
        "title_keywords": ["neuroderechos", "neurotecnología", "neurodatos", "privacidad mental"],
        "text_keywords": ["neuroderechos", "neurotecnología", "neurodatos", "privacidad mental", "integridad mental", "libertad cognitiva", "actividad cerebral"],
        "min_title_score": 1, "min_text_score": 3,
    },
    {
        "key": "Salud y Tecnología Médica", "icon": "🏥", "color": "#e11d48",
        "title_keywords": ["salud", "médic", "sanitari", "medicamento", "fármaco", "telemedicin"],
        "text_keywords": ["medicamento", "fármaco", "salud", "sanitari", "tecnología sanitaria", "innovación médica", "telemedicina", "dispositivo médico", "farmacéutic", "enfermedad"],
        "min_title_score": 1, "min_text_score": 5,
    },
    {
        "key": "Seguridad Vial y Transporte", "icon": "🚗", "color": "#64748b",
        "title_keywords": ["seguridad vial", "tránsito", "transporte", "vehículo", "automotor"],
        "text_keywords": ["seguridad vial", "tránsito", "transporte", "vehículo", "automotor", "conducción"],
        "min_title_score": 1, "min_text_score": 3,
    },
    {
        "key": "Educación y Formación CyT", "icon": "🎓", "color": "#ea580c",
        "title_keywords": ["educación", "currícula", "formación", "escuela", "clubes de ciencia", "educativo", "currículas"],
        "text_keywords": ["currícula", "educación", "formación", "escuela", "docente", "programa educativo", "clubes de ciencia", "digital", "alfabetización", "nivel primario", "nivel secundario", "nivel inicial"],
        "min_title_score": 1, "min_text_score": 6,
        "exclude_if_title_has": ["inteligencia artificial", " ia ", " ia,"],
    },
    {
        "key": "I+D y Financiamiento", "icon": "💰", "color": "#ca8a04",
        "title_keywords": ["financiamiento", "fondo nacional", "inversión", "presupuesto", "incentivo", "i+d", "investigación y desarrollo", "beca", "sostenimiento", "emergencia presupuestaria", "fosit", "capital de riesgo", "enfi"],
        "text_keywords": ["fondo nacional", "financiamiento", "presupuesto", "inversión en ciencia", "ley 27.614", "sostenimiento de la ciencia", "subsidio", "beca", "incentivo fiscal", "capital de riesgo", "fideicomiso"],
        "min_title_score": 1, "min_text_score": 4,
    },
    {
        "key": "Gobernanza e Institucionalidad CyT", "icon": "🏛️", "color": "#475569",
        "title_keywords": ["directorio", "agencia", "derogación", "decreto", "ina", "inmet", "sello", "yozma", "nodos de innovación", "planificación", "transferencia", "sinpte", "otheguy", "activo estratégico"],
        "text_keywords": ["agencia", "consejo", "observatorio", "comisión", "ministerio de ciencia", "sistema nacional de ciencia", "directorio", "derogación", "decreto", "reglament", "organismo", "ina", "inmet", "sello", "yozma", "nodos de innovación", "planificación", "transferencia de conocimiento"],
        "min_title_score": 1, "min_text_score": 5,
    },
    {
        "key": "Datos y Digitalización", "icon": "🔐", "color": "#4f46e5",
        "title_keywords": ["datos personales", "protección de datos", "privacidad", "ciberseguridad", "digitalización", "plataformas tecnológicas"],
        "text_keywords": ["datos personales", "protección de datos", "privacidad", "ciberseguridad", "digitalización", "gobierno digital", "interoperabilidad", "5g"],
        "min_title_score": 1, "min_text_score": 5,
    },
    {
        "key": "Inteligencia Artificial", "icon": "🤖", "color": "#2563eb",
        "title_keywords": ["inteligencia artificial", " ia ", "algoritmo", "deepfake", "reconocimiento facial"],
        "text_keywords": ["inteligencia artificial", "algoritmo", "aprendizaje automático", "machine learning", "deep learning", "deepfake", "reconocimiento facial", "sesgo algorítmico", "sistemas autónomos", "robótica"],
        "min_title_score": 1, "min_text_score": 3,
    },
]

# ─── DIPUTADO → BLOQUE MAPPING ───────────────────────────────────
# Manual mapping based on known diputados
DIPUTADO_BLOQUE = {
    "silvana giudici": "La Libertad Avanza",
    "marcela marina pagano": "La Libertad Avanza",
    "marcela pagano": "La Libertad Avanza",
    "pamela calletti": "Innovación Federal",
    "julián pinciaroli": "La Libertad Avanza",
    "julian pinciaroli": "La Libertad Avanza",
    "cecilia solange wissocq": "La Libertad Avanza",
    "cecilia wissocq": "La Libertad Avanza",
    "oscar agost carreño": "Encuentro Federal",
    "dante lópez rodríguez": "Unión por la Patria",
    "dante lopez rodriguez": "Unión por la Patria",
    "gisela marziotta": "Unión por la Patria",
    "esteban paulón": "Unión por la Patria",
    "esteban paulon": "Unión por la Patria",
    "daniel gollan": "Unión por la Patria",
    "yolanda vega": "Innovación Federal",
    "gabriela estévez": "Unión por la Patria",
    "gabriela estevez": "Unión por la Patria",
    "gabriel chumpitaz": "La Libertad Avanza",
    "gabriel felipe chumpitaz": "La Libertad Avanza",
    "danya tavela": "UCR",
    "maximiliano ferraro": "Coalición Cívica",
    "monica fein": "Encuentro Federal",
    "silvana micaela ginocchio": "Unión por la Patria",
    "juan fernando brügge": "Provincias Unidas",
    "victoria rosso": "Frente de Todos",
    "jimena latorre": "UCR",
    "victoria morales gorleri": "PRO",
    "martin yeza": "PRO",
    "martín yeza": "PRO",
    "pablo outes": "Innovación Federal",
    "manuel ignacio aguirre": "UCR",
    "natalia silvina sarapura": "UCR",
    "diego giuliano": "Unión por la Patria",
    "adolfo bermejo": "Unión por la Patria",
    "héctor baldassi": "PRO",
    "hbaldassi": "PRO",
    "fabio quetglas": "UCR",
    "pablo juliano": "Socialista",
    "paola vessvessian": "Unión por la Patria",
    "pablo lópez": "Unión por la Patria",
    "pablo lopez": "Unión por la Patria",
}


def extract_pdf_text(pdf_path: str, max_pages: int = 8) -> str:
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for i, page in enumerate(doc):
            if i >= max_pages:
                break
            text += page.get_text("text") + "\n"
        doc.close()
        return text
    except Exception as e:
        return ""


def extract_full_text(pdf_path: str) -> str:
    """Get ALL text, including last pages for author extraction."""
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text("text") + "\n"
        doc.close()
        return text
    except:
        return ""


def extract_authors_from_text(text: str) -> list[str]:
    """Extract author names from PDF text."""
    names = []
    
    # Pattern 1: Name + "Diputado/a Nacional"
    pat1 = re.compile(
        r"([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+){1,4})\s*\n\s*(?:Diputad[oa]\s+Nacional|DIPUTAD[OA]\s+NACIONAL)",
        re.MULTILINE
    )
    for m in pat1.finditer(text):
        name = m.group(1).strip()
        if 5 < len(name) < 50 and "Artículo" not in name and "Proyecto" not in name:
            names.append(name)
    
    # Pattern 2: UPPERCASE names + Diputado
    pat2 = re.compile(
        r"([A-ZÁÉÍÓÚÑ]{3,}(?:\s+[A-ZÁÉÍÓÚÑ]{2,}){1,4})\s*\n\s*(?:Diputad[oa]|DIPUTAD[OA])",
        re.MULTILINE
    )
    for m in pat2.finditer(text):
        raw = m.group(1).strip()
        name = raw.title()
        if 5 < len(name) < 50 and name not in names:
            names.append(name)
    
    # Pattern 3: "FIRMANTE:" or "Firma:"
    pat3 = re.compile(r"(?:FIRMANTE|Firma|firmante)[:\s]+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+)+)", re.MULTILINE)
    for m in pat3.finditer(text):
        name = m.group(1).strip()
        if 5 < len(name) < 50 and name not in names:
            names.append(name)
    
    # Pattern 4: "Dip. Name" or "DIPUTADO Name"
    pat4 = re.compile(r"(?:Dip\.|DIPUTADO|Diputado)\s+([A-ZÁÉÍÓÚÑ][a-záéíóúñ]+(?: [A-ZÁÉÍÓÚÑ][a-záéíóúñ]+){1,3})", re.MULTILINE)
    for m in pat4.finditer(text):
        name = m.group(1).strip()
        if 5 < len(name) < 50 and name not in names and "Nacional" not in name:
            names.append(name)
    
    # Deduplicate keeping order
    seen = set()
    unique = []
    for n in names:
        key = n.lower().strip()
        if key not in seen:
            seen.add(key)
            unique.append(n)
    
    return unique[:5]


def get_bloque(author_name: str, text: str = "") -> str:
    """Map author name to bloque."""
    key = author_name.lower().strip()
    
    # Direct lookup
    if key in DIPUTADO_BLOQUE:
        return DIPUTADO_BLOQUE[key]
    
    # Partial match
    for known, bloque in DIPUTADO_BLOQUE.items():
        if known in key or key in known:
            return bloque
    
    # Check last name only
    parts = key.split()
    if len(parts) >= 2:
        last = parts[-1]
        for known, bloque in DIPUTADO_BLOQUE.items():
            if last in known.split():
                return bloque
    
    return "Sin datos"


def extract_objeto(text: str) -> str:
    patterns = [
        r"(?:Art[íi]culo\s+1[°º]?\s*[\.\-–:\s]+)(.*?)(?:Art[íi]culo\s+2)",
        r"Objeto[\.:\s]+(.*?)(?:Art[íi]culo\s+2|$)",
    ]
    for pat in patterns:
        m = re.search(pat, text, re.IGNORECASE | re.DOTALL)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip()[:500]
    return ""


def count_kw(text: str, keywords: list[str]) -> int:
    text_lower = text.lower()
    return sum(text_lower.count(kw.lower()) for kw in keywords)


def classify_eje(title: str, objeto: str, full_text: str) -> tuple[str, int]:
    title_lower = (title or "").lower()
    objeto_lower = (objeto or "").lower()

    for eje in EJES:
        key = eje["key"]
        excludes = eje.get("exclude_if_title_has", [])
        if any(ex in title_lower for ex in excludes):
            continue
        title_score = count_kw(title_lower, eje["title_keywords"])
        if title_score >= eje["min_title_score"] and key != "Inteligencia Artificial":
            return key, title_score * 10
        objeto_score = count_kw(objeto_lower, eje["text_keywords"])
        if objeto_score >= eje.get("min_text_score", 3) and key != "Inteligencia Artificial":
            return key, objeto_score * 3

    for eje in EJES:
        key = eje["key"]
        if key == "Inteligencia Artificial":
            continue
        excludes = eje.get("exclude_if_title_has", [])
        if any(ex in title_lower for ex in excludes):
            continue
        text_score = count_kw(full_text[:3000].lower(), eje["text_keywords"])
        if text_score >= eje.get("min_text_score", 3) * 2:
            return key, text_score

    ia_eje = EJES[-1]
    ia_score = count_kw(full_text[:3000].lower(), ia_eje["text_keywords"])
    if ia_score >= 3:
        return "Inteligencia Artificial", ia_score

    return "Gobernanza e Institucionalidad CyT", 0


def extract_title_clean(text: str, meta_title: str | None) -> str:
    # Strategy 1: Use meta_title from PDF metadata if available and useful
    if meta_title and not meta_title.startswith(("El Senado", "EL SENADO", "La Honorable", "La Cámara")):
        clean = re.sub(r"^(?:PL\s*-\s*|Pr\s+de\s+Ley\s+|Proyecto\s+de\s+Ley\s*-?\s*)", "", meta_title.strip(), flags=re.IGNORECASE)
        if len(clean) > 10:
            return clean.strip()

    # Strategy 2: Look for ALL CAPS title lines in the text (common in Argentine law PDFs)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    skip_patterns = [
        r'^\d{4}\s*-\s*año', r'^proyecto de ley', r'^el senado',
        r'^la c[aá]mara', r'^sancionan', r'^"', r'^art[íi]culo',
        r'^\d+$', r'^naci[oó]n', r'^www\.', r'^honorable',
        r'^buenos aires', r'^expediente', r'^mesa de entradas',
        r'^trámite', r'^comisi[oó]n', r'^n[uú]mero',
        r'^la honorable', r'^rep[uú]blica', r'^poder ejecutivo',
    ]
    title_parts = []
    found_title = False
    for line in lines[:40]:
        line_clean = line.strip()
        if not line_clean:
            if found_title and title_parts:
                break
            continue
        skip = any(re.match(p, line_clean.lower()) for p in skip_patterns)
        if skip:
            continue
        # Title lines are usually in ALL CAPS
        if line_clean == line_clean.upper() and len(line_clean) > 8 and not line_clean.startswith(('ARTÍCULO', 'ARTICULO', 'ART.')):
            title_parts.append(line_clean)
            found_title = True
        elif found_title:
            break

    if title_parts:
        return " ".join(title_parts).title()[:200]

    # Strategy 3: Extract from Objeto (Article 1) with broader patterns
    objeto = extract_objeto(text)
    if objeto:
        # Try multiple patterns for extracting the core subject
        objeto_patterns = [
            r"(?:tiene por objeto|por objeto)\s+(.*?)(?:\.|,\s*(?:con|que|en|a)\s)",
            r"(?:Créase|Créese|Establécese|Institúyese|Declárase)\s+(.*?)(?:\.|$)",
            r"(?:créase|créese|establécese|institúyese|declárase)\s+(.*?)(?:\.|$)",
            r"(?:La presente ley tiene por (?:objeto|fin|finalidad))\s+(.*?)(?:\.|$)",
        ]
        for pat in objeto_patterns:
            m = re.search(pat, objeto, re.IGNORECASE)
            if m:
                core = m.group(1).strip()
                if 10 < len(core) < 200:
                    return core[:150]

        # If we have an Objeto but no pattern matched, use first sentence
        first_sentence = re.split(r'\.\s', objeto)[0].strip()
        if len(first_sentence) > 15:
            return first_sentence[:150]

    # Strategy 4: Use meta_title even if short
    if meta_title:
        clean = re.sub(r"^(?:PL\s*-\s*|Pr\s+de\s+Ley\s+)", "", meta_title.strip(), flags=re.IGNORECASE)
        if len(clean) > 5:
            return clean.strip()

    # Strategy 5: First meaningful non-boilerplate line from the text
    boilerplate = {'proyecto de ley', 'el senado', 'la cámara', 'sancionan con fuerza',
                   'honorable', 'buenos aires', 'expediente', 'nación argentina'}
    for line in lines[:30]:
        l = line.strip()
        if len(l) > 15 and not any(bp in l.lower() for bp in boilerplate):
            if not re.match(r'^(art[íi]culo|\d+[°º\.\-])', l, re.IGNORECASE):
                return l[:150]

    return "Proyecto sin título disponible"


def extract_resumen(text: str, max_len: int = 300) -> str:
    objeto = extract_objeto(text)
    if objeto and len(objeto) > 30:
        return objeto[:max_len] + ("..." if len(objeto) > max_len else "")

    m = re.search(r"FUNDAMENTOS\s*\n(.*?)(?:\n\n|\nArt)", text, re.IGNORECASE | re.DOTALL)
    if m:
        resumen = re.sub(r"\s+", " ", m.group(1)).strip()
        if len(resumen) > 30:
            return resumen[:max_len] + ("..." if len(resumen) > max_len else "")

    paragraphs = [p.strip() for p in text.split("\n\n") if len(p.strip()) > 50]
    skip_words = ["cámara", "honorable", "expediente", "buenos aires", "mesa de entradas", "trámite"]
    for p in paragraphs[:5]:
        clean = re.sub(r"\s+", " ", p).strip()
        if not any(w in clean.lower()[:50] for w in skip_words):
            return clean[:max_len] + ("..." if len(clean) > max_len else "")

    return "Resumen no disponible"


def classify_tipo(text: str) -> str:
    text_lower = text[:3000].lower()
    tipo_map = [
        ("MARCO REGULATORIO", ["marco regulatorio", "marco normativo", "régimen jurídico", "ley marco", "marco legal"]),
        ("CREA ÓRGANOS", ["créase el", "creación del", "creación de la", "créase el programa"]),
        ("FINANCIAMIENTO", ["fondo nacional", "fondo fiduciario", "presupuesto", "inversión", "incentivo fiscal", "emergencia presupuestaria", "fideicomiso"]),
        ("EDUCATIVA", ["currícula", "programa educativo", "clubes de ciencia", "educación nacional"]),
        ("MODIFICA LEY", ["modifícase", "modifíquese", "sustitúyese", "incorpórase", "derógase", "restitúyase"]),
        ("PENAL", ["código penal", "prisión", "delito", "reprimido"]),
        ("PROMOCIÓN", ["programa nacional", "plan nacional", "promuévase", "foméntese", "régimen de promoción"]),
        ("DECLARATIVA", ["declaración", "interés nacional", "declara", "activo estratégico"]),
    ]
    for tipo, keywords in tipo_map:
        if any(kw in text_lower for kw in keywords):
            return tipo
    return "PROYECTO DE LEY"


def main():
    base = Path(__file__).resolve().parent
    pdfs_json_path = base / "CyT proyectos" / "PDFs_AllProyectos_Ley" / "pdfs.json"
    pdfs_base_dir = base / "CyT proyectos" / "PDFs_AllProyectos_Ley"
    out_path = base / "cyt_bills_data.json"

    # Also load bills_data.json for cross-reference
    ia_data_path = base / "bills_data.json"
    ia_bills = {}
    if ia_data_path.exists():
        ia_data = json.loads(ia_data_path.read_text(encoding="utf-8"))
        for b in ia_data.get("bills", []):
            ia_bills[b["id"]] = b

    # Load curated CSV taxonomy
    csv_path = base / "Proyectos_de_LeyCyT.xlsx - Proyectos de Ley.csv"
    csv_lookup = {}
    if csv_path.exists():
        with open(csv_path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                exp = (row.get("Expediente") or "").strip()
                if exp:
                    csv_lookup[exp] = {
                        "tematica": (row.get("Tipo / Temática") or "").strip(),
                        "subtematica": (row.get("SUBTEMATICA") or "").strip(),
                        "autor_csv": (row.get("Autor/es") or "").strip(),
                        "bloque_csv": (row.get("Bloque") or "").strip(),
                    }
        print(f"CSV taxonomy loaded: {len(csv_lookup)} entries")

    pdfs_meta = json.loads(pdfs_json_path.read_text(encoding="utf-8"))
    pdf_entries = pdfs_meta.get("pdfs", [])

    print(f"Total PDFs: {len(pdf_entries)}")
    print(f"IA cross-ref bills: {len(ia_bills)}")

    bills = []
    eje_counts = {}
    year_counts = {}
    bloque_counts = {}
    tematica_counts = {}
    subtema_counts = {}
    autor_counts = {}

    for entry in pdf_entries:
        expediente = entry["expediente"]
        year = entry["year"]
        pdf_path = pdfs_base_dir / entry["path"]
        meta_title = entry.get("title")
        meta_author = entry.get("author")

        print(f"  {expediente}...", end=" ")

        if not pdf_path.exists():
            print("NO ENCONTRADO")
            continue

        text = extract_pdf_text(str(pdf_path))
        full_text = extract_full_text(str(pdf_path))
        if not text.strip():
            text = f"{meta_title or ''} {expediente}"
            full_text = text

        objeto = extract_objeto(text)
        titulo = extract_title_clean(text, meta_title)
        eje, eje_score = classify_eje(meta_title or titulo, objeto, text)
        resumen = extract_resumen(text)
        tipo = classify_tipo(text)

        # Author extraction: try multiple sources
        authors = extract_authors_from_text(full_text)
        
        # Cross-reference with IA bills_data
        ia_ref = ia_bills.get(expediente)
        if ia_ref and not authors:
            authors = ia_ref.get("autores", [])
        
        # Fallback to PDF metadata
        if not authors and meta_author:
            authors = [meta_author]
        
        # Map bloque
        bloque = "Sin datos"
        if ia_ref:
            bloque = ia_ref.get("bloque", "Sin datos")
        elif authors:
            bloque = get_bloque(authors[0], full_text)
        
        autor_principal = authors[0] if authors else "No disponible"

        print(f"→ {eje} | {autor_principal[:25]} ({bloque})")

        eje_counts[eje] = eje_counts.get(eje, 0) + 1
        yr = str(year)
        year_counts[yr] = year_counts.get(yr, 0) + 1
        bloque_counts[bloque] = bloque_counts.get(bloque, 0) + 1
        
        if autor_principal != "No disponible":
            autor_counts[autor_principal] = autor_counts.get(autor_principal, 0) + 1

        # Merge curated CSV taxonomy
        csv_row = csv_lookup.get(expediente, {})
        tematica = csv_row.get("tematica", "") or eje  # fallback to auto eje
        subtematica = csv_row.get("subtematica", "")
        
        # Override bloque from CSV if script didn't find one
        if bloque == "Sin datos" and csv_row.get("bloque_csv"):
            bloque = csv_row["bloque_csv"]
        
        # Override author from CSV if script didn't find one
        if autor_principal == "No disponible" and csv_row.get("autor_csv") and csv_row["autor_csv"] != "—":
            autor_principal = csv_row["autor_csv"]
            authors = [autor_principal]

        tematica_counts[tematica] = tematica_counts.get(tematica, 0) + 1
        if subtematica:
            subtema_counts[subtematica] = subtema_counts.get(subtematica, 0) + 1

        bill = {
            "id": expediente,
            "titulo": titulo,
            "autores": authors,
            "autor_principal": autor_principal,
            "bloque": bloque,
            "camara": "Diputados",
            "año": year,
            "eje": eje,
            "eje_score": eje_score,
            "tematica": tematica,
            "subtematica": subtematica,
            "resumen": resumen,
            "tipo": tipo,
            "paginas": entry.get("pages", 0),
            "pdf_path": f"CyT proyectos/PDFs_AllProyectos_Ley/{entry['path']}",
        }
        bills.append(bill)

    bills.sort(key=lambda b: (-b["año"], b["id"]))

    eje_info = {e["key"]: {"icon": e["icon"], "color": e["color"]} for e in EJES}
    eje_stats = [
        {"eje": eje, "total": count, "icon": eje_info.get(eje, {}).get("icon", "📋"), "color": eje_info.get(eje, {}).get("color", "#666")}
        for eje, count in sorted(eje_counts.items(), key=lambda x: -x[1])
    ]
    year_stats = [{"año": yr, "total": count} for yr, count in sorted(year_counts.items())]
    
    # Bloque stats with colors
    BLOQUE_COLORS = {
        "La Libertad Avanza": "#7B2D8E",
        "Unión por la Patria": "#00AEEF",
        "PRO": "#FFD700",
        "UCR": "#E30613",
        "Innovación Federal": "#2E86C1",
        "Coalición Cívica": "#8BC34A",
        "Encuentro Federal": "#FF9800",
        "Provincias Unidas": "#4CAF50",
        "Frente de Todos": "#00BCD4",
        "Democracia para Siempre": "#9C27B0",
        "Socialista": "#E91E63",
        "Sin datos": "#9ca3af",
    }
    
    bloque_stats = [
        {"bloque": bloque, "total": count, "color": BLOQUE_COLORS.get(bloque, "#9ca3af")}
        for bloque, count in sorted(bloque_counts.items(), key=lambda x: -x[1])
    ]
    
    # Top autores
    top_autores = [
        {"autor": a, "total": c}
        for a, c in sorted(autor_counts.items(), key=lambda x: -x[1])[:15]
    ]

    # Year-eje matrix
    year_eje_matrix = {}
    for bill in bills:
        yr = str(bill["año"])
        eje = bill["eje"]
        if yr not in year_eje_matrix:
            year_eje_matrix[yr] = {}
        year_eje_matrix[yr][eje] = year_eje_matrix[yr].get(eje, 0) + 1

    # Temática stats with colors
    TEMATICA_COLORS = {
        "IA": "#7c3aed",
        "Estrategia Tecnologica Nacional": "#2563a0",
        "Innovación y Desarrollo Productivo": "#059669",
        "Tecnologías Estratégicas ": "#dc2626",
        "Privacidad Digital / Derechos Digitales": "#d97706",
    }
    tipo_stats = [
        {"tipo": t, "total": c, "color": TEMATICA_COLORS.get(t, "#9ca3af")}
        for t, c in sorted(tematica_counts.items(), key=lambda x: -x[1])
    ]
    subtema_stats = [
        {"subtema": s, "total": c}
        for s, c in sorted(subtema_counts.items(), key=lambda x: -x[1])
    ]

    output = {
        "metadata": {
            "generado": datetime.now().isoformat(),
            "total": len(bills),
            "fuente": "Comisión de Ciencia, Tecnología e Innovación Productiva — H. Cámara de Diputados",
            "periodo": f"{min(b['año'] for b in bills)}–{max(b['año'] for b in bills)}" if bills else "",
            "con_autor": sum(1 for b in bills if b["autor_principal"] != "No disponible"),
            "con_bloque": sum(1 for b in bills if b["bloque"] != "Sin datos"),
        },
        "eje_stats": eje_stats,
        "year_stats": year_stats,
        "bloque_stats": bloque_stats,
        "top_autores": top_autores,
        "year_eje_matrix": year_eje_matrix,
        "tipo_stats": tipo_stats,
        "subtema_stats": subtema_stats,
        "bills": bills,
    }

    out_path.write_text(json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n{'='*60}")
    print(f"✅ Generado: {out_path}")
    print(f"   Total: {len(bills)} | Con autor: {output['metadata']['con_autor']} | Con bloque: {output['metadata']['con_bloque']}")
    print(f"   Ejes: {len(eje_stats)}")
    for s in eje_stats:
        print(f"     {s['icon']} {s['eje']}: {s['total']}")
    print(f"   Bloques:")
    for s in bloque_stats:
        print(f"     {s['bloque']}: {s['total']}")


if __name__ == "__main__":
    main()
