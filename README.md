# Dashboard CyT — Comisión de Ciencia, Tecnología e Innovación Productiva

Análisis integral de los **75 proyectos legislativos** presentados ante la Comisión de Ciencia, Tecnología e Innovación Productiva del H. Cámara de Diputados de la Nación Argentina.

## 🌐 Deploy

Este proyecto se despliega como sitio estático en **Vercel**. No requiere build.

| Página | Ruta |
|--------|------|
| Landing CyT | `/landing-cyt` |
| Dashboard CyT | `/dashboard-cyt` |
| Landing General | `/` |
| Dashboard IA | `/dashboard` |

## 📊 Datos

- **73/75** proyectos con autor identificado
- **73/75** con bloque político mapeado
- **14** bloques políticos representados
- **12** ejes temáticos

Fuentes: PDFs de proyectos (extracción de texto), dataset oficial HCDN (`proyectos_parlamentarios.json`, `diputados.json`).

## 🛠️ Stack

- HTML / CSS / JavaScript (vanilla)
- Chart.js (visualizaciones)
- Datos: `cyt_bills_data.json` (generado por `extract_cyt_data.py`)

## 📁 Estructura

```
├── landing-cyt.html      # Landing institucional CyT
├── dashboard-cyt.html    # Dashboard interactivo CyT
├── index.html            # Landing general
├── dashboard.html        # Dashboard IA
├── cyt_bills_data.json   # Datos de 75 proyectos CyT
├── bills_data.json       # Datos proyectos IA
├── vercel.json           # Config Vercel
└── extract_cyt_data.py   # Script extracción (no se sube)
```

## 🚀 Desarrollo local

```bash
npx http-server -p 8080 -c-1 --cors
```
