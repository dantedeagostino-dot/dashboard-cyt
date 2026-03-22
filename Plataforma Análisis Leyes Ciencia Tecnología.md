# **Arquitecturas de inteligencia legislativa para la Comisión de Ciencia, Tecnología e Innovación Productiva: Un análisis global de herramientas, metodologías de evaluación y marcos comparativos**

El fenómeno de la aceleración tecnológica ha impuesto un desafío sin precedentes sobre las estructuras parlamentarias tradicionales, las cuales a menudo operan bajo ritmos deliberativos que no coinciden con la velocidad de la innovación. En el caso específico de la Comisión de Ciencia, Tecnología e Innovación Productiva del Congreso de la Nación Argentina, la necesidad de una plataforma de análisis avanzado se vuelve imperativa para procesar una agenda que abarca desde la regulación de la inteligencia artificial hasta la soberanía nuclear y el desarrollo biotecnológico.1 La construcción de tal plataforma no es meramente un ejercicio de ingeniería de software, sino una síntesis de ciencia política, derecho computacional y análisis de impacto socioeconómico. Para sentar una base de reglas que permita discutir proyectos en su conjunto e identificar prioridades, es necesario integrar las mejores prácticas globales en monitoreo legislativo con las capacidades más recientes de procesamiento de lenguaje natural y los marcos de evaluación de organismos internacionales como la Organización para la Cooperación y el Desarrollo Económicos (OCDE) y el Banco Interamericano de Desarrollo (BID).4

## **Ecosistema global de herramientas de monitoreo y seguimiento legislativo**

El mercado global de herramientas de seguimiento legislativo ha evolucionado desde simples bases de datos indexadas hacia ecosistemas de inteligencia política que utilizan el aprendizaje automático para predecir el éxito de las iniciativas y mapear la influencia de los actores clave. La eficacia de estas herramientas se mide por su capacidad para transformar la "ruido" de miles de documentos en señales claras para la toma de decisiones estratégicas.7

### **Plataformas líderes en inteligencia política y gubernamental**

Dentro del ámbito comercial, Quorum y FiscalNote dominan el sector mediante el uso intensivo de inteligencia artificial aplicada a la incidencia política. Quorum se define como una plataforma de gestión de asuntos públicos impulsada por IA que no solo rastrea proyectos de ley, sino que también facilita el compromiso con los legisladores a través de un mapeo detallado de sus redes de contacto y comportamientos históricos.7 Una de sus funciones más potentes para el análisis de comisiones es su capacidad para generar resúmenes automáticos de proyectos y transcripciones de audiencias en tiempo real, lo que permite a los analistas capturar los matices de la discusión técnica sin necesidad de una revisión manual exhaustiva.9 Esta plataforma alcanza una valoración de 9.8 sobre 10 en funcionalidades, destacándose por su sistema de alertas tempranas que monitorea no solo el texto legal, sino también las menciones en redes sociales y medios de comunicación por parte de los miembros de las comisiones.7

FiscalNote, por su parte, ofrece una cobertura global que abarca más de 200 jurisdicciones, lo cual es esencial para el objetivo de comparar proyectos argentinos con los de otros países.8 Su motor analítico incluye modelos predictivos que calculan la probabilidad de que una pieza legislativa sea aprobada, basándose en variables como el patrocinador, el momento del ciclo legislativo y la composición de las mayorías.7 Para una comisión de ciencia y tecnología, FiscalNote proporciona informes bi-semanales curados por analistas de políticas que ayudan a mirar "a la vuelta de la esquina" e identificar tendencias emergentes en regulación tecnológica antes de que lleguen a la mesa de debate nacional.8

| Plataforma | Calificación de Funcionalidad | Cobertura Jurisdiccional | Fortalezas Técnicas |
| :---- | :---- | :---- | :---- |
| Quorum | 9.8/10 | Federal, Estatal (EE.UU.), UE, Internacional | IA para resúmenes, mapeo de stakeholders, análisis de diálogos. |
| FiscalNote | 9.7/10 | Global (+200 países), Federal, Estatal | Analítica predictiva, informes de impacto, alertas globales. |
| Bloomberg Government | 9.5/10 | Federal (EE.UU.) | Datos de contratación pública, análisis regulatorio profundo. |
| StateScape | 9.2/10 | 50 Estados de EE.UU. | Seguimiento de expedientes a nivel de secretaría, gestión de lobby. |
| BillTrack50 | 9.1/10 | Federal, 50 Estados de EE.UU. | Herramientas de comparación de proyectos entre jurisdicciones. |
| LegiScan | 8.8/10 | Federal, 50 Estados de EE.UU. | API robusta para integración de datos abiertos en sistemas propios. |

Otras herramientas como Bloomberg Government se enfocan en la intersección entre la legislación y el gasto público, proporcionando análisis detallados sobre cómo las nuevas leyes pueden afectar la contratación de servicios tecnológicos y la asignación de subvenciones.7 Para el caso argentino, donde la ciencia y la tecnología dependen fuertemente del presupuesto nacional, este enfoque en la viabilidad financiera de los proyectos es un componente crítico de la priorización.11 En contraste, herramientas como Skopos Labs utilizan un modelado puramente impulsado por IA para la predicción de resultados legislativos, eliminando el sesgo humano en la evaluación de qué proyectos tienen mayor tracción política.7

### **Modelos de código abierto y arquitecturas de datos parlamentarios**

Para una plataforma que busca analizar proyectos específicos de la Comisión de Ciencia y Tecnología en Argentina, los modelos de código abierto ofrecen una flexibilidad que las plataformas comerciales cerradas a veces limitan. El proyecto "unitedstates/congress" en GitHub es un referente técnico que proporciona herramientas en Python para recolectar datos sobre proyectos de ley, enmiendas y votaciones, convirtiéndolos en formatos estructurados como JSON y XML.12 Esta arquitectura es ideal para alimentar motores de búsqueda semántica y modelos de lenguaje de gran escala.

La plataforma Open States ha establecido el estándar para la limpieza y normalización de datos parlamentarios, permitiendo que la información de múltiples legislaturas sea accesible a través de una API unificada.13 La arquitectura técnica de estos sistemas suele dividirse en tres fases: una fase de lectura que extrae los enlaces de los portales gubernamentales, una fase de raspado (scraping) que recupera el contenido textual y una fase de procesamiento que establece las relaciones entre los nodos del grafo legislativo (por ejemplo, relacionando una ley con sus decretos reglamentarios o leyes precedentes).14

## **La infraestructura de datos legislativos en la República Argentina**

El diseño de la plataforma propuesta debe anclarse en la realidad técnica de las fuentes de información del Congreso de la Nación. Argentina posee un marco de dominio público sobre su información parlamentaria, lo que permite el uso libre de los datos siempre que se cite la fuente original.1

### **Acceso y estructura de la Cámara de Diputados**

La Honorable Cámara de Diputados de la Nación (HCDN) organiza su información a través de la Dirección de Información Parlamentaria, la cual mantiene registros desde 1983 hasta la actualidad.1 Para la Comisión de Ciencia, Tecnología e Innovación Productiva, la plataforma oficial ofrece metadatos que incluyen la competencia de la comisión, su composición y las agendas detalladas de sus reuniones, identificadas por números de expediente como el 2435-D-2024.1

El sistema de búsqueda permite filtrar proyectos por número de expediente, tipo de trámite (D, S, PE, OV, entre otros) y estado de dictamen en comisiones.1 No obstante, la integración automatizada presenta desafíos, ya que los portales gubernamentales a menudo carecen de APIs con documentación técnica completa para desarrolladores externos, lo que obliga a depender de técnicas de web scraping que deben ser mantenidas ante cambios en el diseño de los sitios web.1

### **Datos abiertos y transparencia en el Senado de la Nación**

El Senado de la Nación ha avanzado en la provisión de datos abiertos a través de un micrositio que permite la descarga de conjuntos de datos en formatos JSON y XLS.15 Esta información incluye:

* **Actividad Parlamentaria:** Listado de asuntos entrados, boletines de novedades y versiones taquigráficas de las sesiones, fundamentales para el análisis cualitativo de la discusión de leyes científicas.15  
* **Normativa Vigente:** Un corpus de leyes y decretos que sirve como base para comparar las nuevas propuestas con el marco legal preexistente.15  
* **Gestión Administrativa:** Datos sobre licitaciones y resoluciones que pueden ser útiles para rastrear la implementación de políticas tecnológicas una vez sancionadas las leyes.15

A nivel del Poder Ejecutivo, el Portal Nacional de Datos Abiertos ofrece APIs para normalizar unidades territoriales y consultar series de tiempo de indicadores socioeconómicos.16 Estos indicadores son cruciales para la plataforma, ya que permiten correlacionar el éxito de una ley de ciencia y tecnología con la evolución de la inversión en I+D como porcentaje del PBI, una métrica que en Argentina ha mostrado una brecha significativa respecto a los países de la OCDE.2

## **Metodologías para la evaluación y priorización de proyectos de ley**

Uno de los objetivos centrales de la consulta es identificar cuáles son los "mejores" proyectos y cuáles deben tener prioridad. Para ello, es necesario adoptar metodologías cuantitativas y cualitativas que aporten objetividad al proceso de selección.

### **El puntaje de efectividad legislativa (Legislative Effectiveness Score)**

La metodología del Legislative Effectiveness Score (LES) permite evaluar el desempeño de un proyecto de ley basándose en su trayectoria a través de quince indicadores críticos distribuidos en cinco etapas del proceso legislativo.19 El cálculo se formaliza mediante la ponderación de los proyectos según su importancia sustantiva.

Para determinar la efectividad, se puede emplear una fórmula que asigne pesos (![][image1]) a los proyectos de la siguiente manera:

![][image2]  
Donde ![][image3] representa el peso del tipo de proyecto (conmemorativo, sustantivo o significativo) y ![][image4] es un indicador binario del éxito en una de las etapas (comisión, aprobación en cámara, sanción final).19

| Tipo de Proyecto | Criterio de Identificación | Peso Asignado (w) |
| :---- | :---- | :---- |
| Conmemorativo (C) | Cambios de nombre, días nacionales, declaraciones sin fuerza de ley. | 1 |
| Sustantivo (S) | Modificaciones a leyes vigentes, regulaciones estándar del sector. | 5 |
| Sustantivo y Significativo (SS) | Reformas de gran escala, leyes presupuestarias plurianuales, marcos para nuevas tecnologías. | 10 |

En la 117.ª legislatura de los EE. UU., se introdujo una refinación a esta metodología para otorgar crédito a los legisladores cuyo lenguaje original es incorporado en otros proyectos de ley exitosos, utilizando comparaciones de similitud de texto de Jaccard.19 Esta es una regla fundamental para la plataforma propuesta, ya que en la Comisión de Ciencia y Tecnología argentina es común que múltiples proyectos sobre un mismo tema (como la Inteligencia Artificial) se fusionen en un único dictamen de mayoría.2

### **Criterios de priorización basados en impacto y riesgo**

Para determinar la prioridad de un proyecto, la plataforma debe ir más allá del progreso administrativo y evaluar su alineación con los objetivos estratégicos nacionales. El Análisis de Impacto Regulatorio (AIR) es la herramienta estándar para este fin. Según las guías de la OCDE, un AIR efectivo debe identificar el problema público, evaluar alternativas (incluyendo la no regulación) y estimar los costos y beneficios para la sociedad.21

En el ámbito de la ciencia y la tecnología, la priorización debe considerar los siguientes ejes extraídos de los marcos internacionales:

1. **Transformación Socioeconómica:** Proyectos que movilizan la ciencia para cambios sistémicos en la economía, como la transición hacia una economía de bajas emisiones o la digitalización industrial.4  
2. **Soberanía Tecnológica y Seguridad:** Iniciativas que protegen infraestructuras críticas (como el sector nuclear) o aseguran la cadena de suministro de componentes estratégicos.3  
3. **Inclusión y Difusión:** Leyes que no solo fomentan la excelencia en centros de investigación, sino que garantizan la difusión del conocimiento hacia las pequeñas y medianas empresas (PyMEs) y regiones rezagadas.4  
4. **Urgencia Regulatoria:** Necesidad de marcos legales para mitigar riesgos inmediatos, como los sesgos algorítmicos en la IA o la protección de datos personales en el entorno digital.20

## **Aplicación de inteligencia artificial y procesamiento de lenguaje natural**

La complejidad intrínseca de los textos legales, caracterizados por oraciones extensas y terminología altamente específica, requiere el uso de técnicas avanzadas de Procesamiento de Lenguaje Natural (NLP) para automatizar el análisis.26

### **Tareas de NLP específicas para el dominio legal**

El análisis de proyectos de ley se beneficia de varias tareas de procesamiento que han sido revolucionadas por los modelos de lenguaje modernos. Los estudios recientes indican que los modelos entrenados específicamente con corpus legales, como Legal-BERT, superan significativamente a los modelos genéricos en tareas de reconocimiento de entidades y clasificación multi-etiqueta.27

* **Clasificación de Textos:** Permite agrupar los proyectos por áreas temáticas (biotecnología, espacio, informática) de manera automática. El uso de modelos de clasificación por temas (Topic Modeling) como LDA (Latent Dirichlet Allocation) ayuda a trazar la evolución de la agenda política a lo largo del tiempo.29  
* **Reconocimiento de Entidades Nombradas (NER):** Extracción sistemática de instituciones (CONICET, CNEA), plazos legales, sanciones monetarias y referencias a otras leyes.26  
* **Minería de Argumentos (Argument Mining):** Identificación de las premisas y conclusiones en los fundamentos de un proyecto de ley, permitiendo evaluar la solidez de la justificación científica de la norma.26  
* **Predicción de Secciones Relevantes:** Marcos basados en TF-IDF y aprendizaje de conjunto pueden predecir qué artículos de códigos existentes (Civil, Penal) serán impactados por una nueva ley científica, reduciendo el riesgo de contradicciones normativas.20

### **El rol de los modelos de lenguaje de gran escala (LLM)**

Los LLMs permiten a la plataforma ofrecer capacidades de resumen ejecutivo personalizadas según el perfil del usuario. Por ejemplo, un asesor técnico puede requerir un resumen de los cambios en los requisitos de patentamiento, mientras que un legislador puede preferir una síntesis de los impactos presupuestarios esperados.9 La arquitectura de Recuperación Aumentada por Generación (RAG) es particularmente útil aquí: permite que el modelo responda preguntas basadas estrictamente en el corpus de proyectos de la comisión, evitando alucinaciones y garantizando la trazabilidad de la fuente.14

## **Marcos de comparación internacional**

Para cumplir con el objetivo de comparar proyectos con los de otros países, la plataforma debe integrar bases de datos y marcos conceptuales internacionales que permitan una evaluación "espejo".

### **El enfoque de ecosistemas industriales de la OCDE**

La OCDE propone pasar de un enfoque puramente sectorial a uno de "ecosistemas industriales" para el diseño de políticas de ciencia y tecnología.32 Este enfoque reconoce que la innovación no ocurre en el vacío, sino en una red de interdependencias entre actores diversos.

| Componente del Ecosistema | Indicadores de Comparación |
| :---- | :---- |
| **Financiamiento** | Inversión pública vs. privada, capital de riesgo, incentivos fiscales para R\&D. |
| **Infraestructura** | Centros de supercomputación, laboratorios de investigación, conectividad 5G/6G. |
| **Talento Humano** | Investigadores por cada 1000 trabajadores, movilidad entre academia e industria. |
| **Gobernanza** | Claridad regulatoria, agilidad administrativa, marcos éticos para tecnologías emergentes. |
| **Difusión** | Tasa de adopción de tecnologías por PyMEs, transferencia tecnológica universidad-empresa. |

La comparación internacional debe utilizar indicadores normalizados como los que ofrece la base de datos de Principales Indicadores de Ciencia y Tecnología (MSTI) de la OCDE, la cual permite calcular benchmarks que ajustan las diferencias en el tamaño de las economías y el poder adquisitivo.6 Esto permite responder preguntas críticas: ¿Es la inversión propuesta en el proyecto de ley X suficiente para cerrar la brecha con el promedio de la región o de la OCDE?.18

### **Diferencias en las filosofías regulatorias globales**

La plataforma debe clasificar los proyectos internacionales y nacionales según su filosofía subyacente, lo que ayuda a prever posibles conflictos comerciales o de cooperación.33

1. **Modelo de la Unión Europea:** Centrado en la protección de los derechos fundamentales y la precaución. La regulación de la IA en la UE, por ejemplo, utiliza un enfoque basado en el riesgo para determinar las obligaciones de los desarrolladores.20  
2. **Modelo de Estados Unidos:** Enfocado en el liderazgo tecnológico y la seguridad nacional. Favorece un entorno de innovación con menos barreras de entrada iniciales, pero con una fuerte aplicación de las leyes de competencia (antitrust) y propiedad intelectual.33  
3. **Modelo de China:** Centralizado y alineado con las prioridades estratégicas del Estado. Utiliza la regulación para fomentar la innovación en áreas críticas mientras mantiene un control estricto sobre el flujo de datos y la estabilidad social.33

## **El contexto argentino: Ciencia, tecnología y soberanía**

El análisis de los proyectos de la comisión en Argentina no puede ignorar el peso histórico de ciertos sectores y la coyuntura política actual. El desarrollo científico-tecnológico nuclear, por ejemplo, ha sido una política de estado durante más de 70 años, proporcionando capacidades de ingeniería únicas en la región.3

### **Temas críticos en la agenda legislativa argentina**

* **Inteligencia Artificial:** Existen múltiples propuestas para crear una Agencia Nacional de Inteligencia Artificial que combine funciones de fomento, regulación y control.2 La discusión se centra en evitar que una regulación excesivamente estricta aniquile a las PyMEs y startups locales frente a los gigantes tecnológicos globales.2  
* **Sectores Estratégicos:** La discusión sobre la privatización de empresas como Nucleoeléctrica Argentina S.A. y el impacto sobre la soberanía energética y tecnológica es un eje central del debate parlamentario reciente.1  
* **Financiamiento de la Ciencia:** La Ley 27.614 establece compromisos de inversión que los legisladores actuales buscan proteger o renegociar ante situaciones de emergencia económica.2 Los proyectos ganadores del concurso INNOV@R en categorías como investigación aplicada y agroindustria sirven como evidencia de los sectores donde Argentina tiene una capacidad de innovación instalada que las leyes deben potenciar.36

### **Casos de éxito y participación ciudadana**

Plataformas como "Vota Inteligente" en Chile y Argentina han demostrado que es posible integrar propuestas de la sociedad civil en la agenda política. Propuestas ciudadanas sobre el compromiso con las ciencias y la inversión en I+D han logrado compromisos de candidaturas presidenciales, lo que subraya la importancia de que la plataforma propuesta tenga una interfaz abierta que permita la retroalimentación de la comunidad científica.37

## **Arquitectura técnica de la plataforma de análisis legislativo**

Para cumplir con la solicitud de armar una plataforma integral, se propone una arquitectura basada en los hallazgos de las herramientas de mayor éxito global y las necesidades específicas del Congreso argentino.

### **Componentes del sistema y flujo de datos**

La plataforma debe estructurarse como un sistema de inteligencia de datos distribuido en cuatro capas funcionales:

1. **Capa de Ingesta y Normalización:** Utilización de scrapers programados en Python para recolectar datos de la HCDN y el Senado. Es fundamental implementar un sistema de gestión de caché y control de errores para manejar la inestabilidad de los portales gubernamentales.12  
2. **Capa de Enriquecimiento Analítico:**  
   * **Motor de Similitud:** Uso de bases de datos vectoriales para comparar el texto de un proyecto con un corpus internacional de leyes científicas.14  
   * **Métrica de Efectividad:** Aplicación automatizada del algoritmo LES para calificar la viabilidad de cada expediente.19  
   * **Análisis de Sentimiento y Diálogo:** Procesamiento de las versiones taquigráficas y menciones en redes sociales de los miembros de la comisión para entender el clima político alrededor de un tema.9  
3. **Capa de Visualización e Interacción:** Desarrollo de un dashboard interactivo que permita ver la "red de leyes", donde los nodos son proyectos y las aristas son citaciones mutuas o similitudes temáticas.39  
4. **Capa de Inteligencia Conversacional:** Un asistente basado en LLM que permita a los asesores de la comisión realizar consultas en lenguaje natural: "¿Qué leyes de biotecnología aprobadas en Brasil en los últimos dos años podrían servir como modelo para nuestra propuesta sobre edición genética?".31

| Módulo de la Plataforma | Tecnología Sugerida | Fuente de Datos Referencial |
| :---- | :---- | :---- |
| Scraping / Ingesta | Python (Selenium, Scrapy) | HCDN, Senado, Parline API.13 |
| Procesamiento NLP | PyTorch, HuggingFace (Legal-BERT) | ArXiv, ReseachGate.26 |
| Base de Datos | PostgreSQL \+ pgvector | SQL Knowledge-graph format.14 |
| Visualización | Streamlit, Plotly, D3.js | Dashboards interactivos.38 |
| IA Generativa | LlamaIndex / LangChain | RAG sobre proyectos de la comisión.31 |

### **Definición de la "Base de Reglas" y Prioridades**

Para sentar la base de reglas solicitada, la plataforma debe automatizar la aplicación de una rúbrica de calidad legislativa. Esta rúbrica evaluará cada proyecto bajo los siguientes parámetros:

* **Coherencia Técnica:** ¿Cita el proyecto fuentes científicas actualizadas o informes de organismos como el CONICET?  
* **Carga Administrativa:** ¿Crea nuevos trámites o simplifica procesos existentes mediante el uso de tecnologías digitales?.22  
* **Impacto Económico Estimado:** ¿Cuál es la inversión proyectada y qué retorno se espera en términos de empleos calificados o patentes?.44  
* **Alineación Internacional:** ¿Sigue los principios de la OCDE para la gobernanza de tecnologías convergentes (bioconvergencia, cuántica, espacio)?.41

La prioridad se asignará mediante un algoritmo que combine la urgencia del problema público (detectada por el monitoreo de noticias y tendencias globales) con la probabilidad de éxito legislativo (calculada por el LES) y el impacto potencial en el desarrollo sostenible.8

## **Conclusiones y recomendaciones estratégicas**

La implementación de una plataforma de análisis para la Comisión de Ciencia, Tecnología e Innovación Productiva del Congreso de la Nación representa una oportunidad histórica para cerrar la brecha entre la producción normativa y el avance científico. El análisis global demuestra que las herramientas más exitosas son aquellas que logran integrar la profundidad de los datos legales con la agilidad de la inteligencia artificial y la visión estratégica de los marcos internacionales.

Para el éxito de esta iniciativa en Argentina, es fundamental:

1. **Asegurar la calidad del dato primario:** Trabajar en la normalización de la información proveniente de ambas cámaras, superando la fragmentación actual mediante el uso de estándares internacionales de datos abiertos parlamentarios.1  
2. **Adoptar un enfoque de "Regulación como Infraestructura":** Entender que los marcos legales para la ciencia y la tecnología no son meras restricciones, sino la infraestructura básica sobre la cual se construye la competitividad nacional en la economía del conocimiento.46  
3. **Fortalecer la capacidad de comparación:** No legislar en aislamiento. La plataforma debe ser una ventana constante a las mejores prácticas de la región y del mundo, permitiendo que Argentina se posicione como un líder en la regulación ética y eficiente de tecnologías emergentes.25  
4. **Involucrar a los beneficiarios:** La priorización de proyectos debe ser un proceso participativo que incluya a la comunidad científica, las PyMEs tecnológicas y la sociedad civil, garantizando que las leyes respondan a necesidades reales y no solo a agendas políticas coyunturales.37

La plataforma propuesta transformará la comisión en un nodo de inteligencia estratégica, capaz de discutir el futuro del país con base en evidencia sólida, reglas claras y una perspectiva global indiscutible. El camino hacia un "Estado Inteligente" en Argentina comienza con un Congreso que sepa utilizar la ciencia y la tecnología para analizar, precisamente, la ciencia y la tecnología.49

#### **Obras citadas**

1. Comisión Permanente de Ciencia y Tecnología e Innovacion ..., fecha de acceso: marzo 22, 2026, [https://www.hcdn.gob.ar/comisiones/permanentes/ccytecnologia](https://www.hcdn.gob.ar/comisiones/permanentes/ccytecnologia)  
2. COMISIÓN COMPLETA: CIENCIA, TECNOLOGÍA E INNOVACIÓN PRODUCTIVA \- 11 de noviembre de 2025 \- HCDN \- YouTube, fecha de acceso: marzo 22, 2026, [https://www.youtube.com/watch?v=SKwNwJ2ZGsA](https://www.youtube.com/watch?v=SKwNwJ2ZGsA)  
3. COMISIÓN COMPLETA: CIENCIA, TECNOLOGÍA E INNOVACIÓN PRODUCTIVA \- 2 de octubre de 2025 \- HCDN \- YouTube, fecha de acceso: marzo 22, 2026, [https://www.youtube.com/watch?v=-kcX5RhWQRY](https://www.youtube.com/watch?v=-kcX5RhWQRY)  
4. OECD Science, Technology and Innovation Outlook 2025, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025\_5fe57b90-en.html](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025_5fe57b90-en.html)  
5. Science, Technology and Innovation \- IDB, fecha de acceso: marzo 22, 2026, [https://www.iadb.org/en/who-we-are/topics/science-technology-and-innovation](https://www.iadb.org/en/who-we-are/topics/science-technology-and-innovation)  
6. Main Science and Technology Indicators | OECD, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/data/datasets/main-science-and-technology-indicators.html](https://www.oecd.org/en/data/datasets/main-science-and-technology-indicators.html)  
7. Top 10 Best Legislative Tracking Software of 2026 \- WifiTalents, fecha de acceso: marzo 22, 2026, [https://wifitalents.com/best/legislative-tracking-software/](https://wifitalents.com/best/legislative-tracking-software/)  
8. Global Policy Tracking | FiscalNote Solutions, fecha de acceso: marzo 22, 2026, [https://fiscalnote.com/solutions/global-policy-tracking](https://fiscalnote.com/solutions/global-policy-tracking)  
9. Bill & Legislative Tracking Software \- Quorum, fecha de acceso: marzo 22, 2026, [https://www.quorum.us/solutions/legislative-tracking/](https://www.quorum.us/solutions/legislative-tracking/)  
10. Top 10 Best Legislative Tracking Software of 2026 \- Gitnux, fecha de acceso: marzo 22, 2026, [https://gitnux.org/best/legislative-tracking-software/](https://gitnux.org/best/legislative-tracking-software/)  
11. FULL COMMISSION: SCIENCE, TECHNOLOGY AND PRODUCTIVE INNOVATION \- September 16, 2025 \- HCDN \- YouTube, fecha de acceso: marzo 22, 2026, [https://www.youtube.com/watch?v=sU40QAnryXw](https://www.youtube.com/watch?v=sU40QAnryXw)  
12. GitHub \- unitedstates/congress: Public domain data collectors for the work of Congress, including legislation, amendments, and votes., fecha de acceso: marzo 22, 2026, [https://github.com/unitedstates/congress](https://github.com/unitedstates/congress)  
13. Open States \- GitHub, fecha de acceso: marzo 22, 2026, [https://github.com/openstates](https://github.com/openstates)  
14. spartypkp/open-source-legislation: Open-source global legislation data in an SQL knowledge-graph format ideal for use with LLMs: Download legislation data in bulk and immediately start building with our Python/Typescript SDKs. Democratize Legal Knowledge For All \- GitHub, fecha de acceso: marzo 22, 2026, [https://github.com/spartypkp/open-source-legislation](https://github.com/spartypkp/open-source-legislation)  
15. Datos abiertos \- Honorable Senado de la Nación Argentina, fecha de acceso: marzo 22, 2026, [https://www.senado.gob.ar/micrositios/DatosAbiertos/](https://www.senado.gob.ar/micrositios/DatosAbiertos/)  
16. APIs \- Datos Argentina, fecha de acceso: marzo 22, 2026, [https://www.datos.gob.ar/apis](https://www.datos.gob.ar/apis)  
17. Innovation is the key to sustainable development in Latin America and the Caribbean \- IDB, fecha de acceso: marzo 22, 2026, [https://www.iadb.org/en/news/innovation-key-sustainable-development-latin-america-and-caribbean](https://www.iadb.org/en/news/innovation-key-sustainable-development-latin-america-and-caribbean)  
18. How can Latin America catch up? \- IDB, fecha de acceso: marzo 22, 2026, [https://www.iadb.org/en/news/how-can-latin-america-catch](https://www.iadb.org/en/news/how-can-latin-america-catch)  
19. Methodology – Center for Effective Lawmaking, fecha de acceso: marzo 22, 2026, [https://thelawmakers.org/methodology](https://thelawmakers.org/methodology)  
20. Proyecto de Ley Marco Normativo y de Desarrollo de los Sistemas de IA \- Diputados, fecha de acceso: marzo 22, 2026, [https://rest.hcdn.gob.ar/web/proyectos/284321/adjuntos/19654](https://rest.hcdn.gob.ar/web/proyectos/284321/adjuntos/19654)  
21. INFORME TÉCNICO \- Arcsa, fecha de acceso: marzo 22, 2026, [https://www.controlsanitario.gob.ec/wp-content/uploads/downloads/2025/12/Informe-Analisis-del-Impacto-Regulatorio-relacionado-al-riesgo-en-la-salud-publica-por-la-comercializacion-de-gases-medicinales-que-no-cumplan-las-Buenas-Practicas-de-Manufactura.pdf](https://www.controlsanitario.gob.ec/wp-content/uploads/downloads/2025/12/Informe-Analisis-del-Impacto-Regulatorio-relacionado-al-riesgo-en-la-salud-publica-por-la-comercializacion-de-gases-medicinales-que-no-cumplan-las-Buenas-Practicas-de-Manufactura.pdf)  
22. RED IBEROAMERICANA Y DEL CARIBE DE MEJORA REGULATORIA \- MPR, fecha de acceso: marzo 22, 2026, [https://www.mpr.gob.es/mpr/subse/occn/Documents/Ponencias.pdf](https://www.mpr.gob.es/mpr/subse/occn/Documents/Ponencias.pdf)  
23. Expanding the benefits of investments in science, technology and innovation \- OECD, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025\_5fe57b90-en/full-report/expanding-the-benefits-of-investments-in-science-technology-and-innovation\_65c4ca1c.html](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025_5fe57b90-en/full-report/expanding-the-benefits-of-investments-in-science-technology-and-innovation_65c4ca1c.html)  
24. Reconfiguring scientific co-operation in a changing geopolitical environment: OECD Science, Technology and Innovation Outlook 2025, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025\_5fe57b90-en/full-report/reconfiguring-scientific-co-operation-in-a-changing-geopolitical-environment\_73f32116.html](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025_5fe57b90-en/full-report/reconfiguring-scientific-co-operation-in-a-changing-geopolitical-environment_73f32116.html)  
25. Argentina-National-AI-Strategy.pdf \- Observatory of Public Sector Innovation, fecha de acceso: marzo 22, 2026, [https://oecd-opsi.org/wp-content/uploads/2021/02/Argentina-National-AI-Strategy.pdf](https://oecd-opsi.org/wp-content/uploads/2021/02/Argentina-National-AI-Strategy.pdf)  
26. Natural Language Processing for the Legal Domain: A Survey of Tasks, Datasets, Models, and Challenges \- arXiv, fecha de acceso: marzo 22, 2026, [https://arxiv.org/pdf/2410.21306](https://arxiv.org/pdf/2410.21306)  
27. Natural language processing in legal document analysis software: A systematic review of current approaches, challenges, and opportunities \- ijirss, fecha de acceso: marzo 22, 2026, [https://www.ijirss.com/index.php/ijirss/article/view/7702](https://www.ijirss.com/index.php/ijirss/article/view/7702)  
28. (PDF) ADVANCED NATURAL LANGUAGE PROCESSING FOR LEGAL DOCUMENT ANALYSIS \- ResearchGate, fecha de acceso: marzo 22, 2026, [https://www.researchgate.net/publication/393232732\_ADVANCED\_NATURAL\_LANGUAGE\_PROCESSING\_FOR\_LEGAL\_DOCUMENT\_ANALYSIS](https://www.researchgate.net/publication/393232732_ADVANCED_NATURAL_LANGUAGE_PROCESSING_FOR_LEGAL_DOCUMENT_ANALYSIS)  
29. Regulatory Innovation for Digital Platforms in the Data-Intelligence Era and Its Implications for E-Commerce \- MDPI, fecha de acceso: marzo 22, 2026, [https://www.mdpi.com/0718-1876/21/1/2](https://www.mdpi.com/0718-1876/21/1/2)  
30. (PDF) Leveraging AI for Legal Text Analysis: Case Study-Based Section Prediction \- ResearchGate, fecha de acceso: marzo 22, 2026, [https://www.researchgate.net/publication/395433671\_Leveraging\_AI\_for\_Legal\_Text\_Analysis\_Case\_Study-Based\_Section\_Prediction](https://www.researchgate.net/publication/395433671_Leveraging_AI_for_Legal_Text_Analysis_Case_Study-Based_Section_Prediction)  
31. dtiberio/Streamlit\_LlamaIndex\_ChinookDB: Python tutorial on how to create a Streamlit Dashboard that leverages LLM models for data analysis \- GitHub, fecha de acceso: marzo 22, 2026, [https://github.com/dtiberio/Streamlit\_LlamaIndex\_ChinookDB](https://github.com/dtiberio/Streamlit_LlamaIndex_ChinookDB)  
32. An ecosystems approach to industrial policy: OECD Science, Technology and Innovation Outlook 2025, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025\_5fe57b90-en/full-report/an-ecosystems-approach-to-industrial-policy\_a9c00ad7.html](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025_5fe57b90-en/full-report/an-ecosystems-approach-to-industrial-policy_a9c00ad7.html)  
33. The Global Race for Tech Regulation: Comparing Approaches in the EU, US, and China, fecha de acceso: marzo 22, 2026, [https://www.abacademies.org/articles/the-global-race-for-tech-regulation-comparing-approaches-in-the-eu-us-and-china-17717.html](https://www.abacademies.org/articles/the-global-race-for-tech-regulation-comparing-approaches-in-the-eu-us-and-china-17717.html)  
34. 2024 Congressional Innovation Scorecard \- Ben Cline, fecha de acceso: marzo 22, 2026, [https://cline.house.gov/uploadedfiles/2024\_congressional\_innovation\_scorecard.pdf](https://cline.house.gov/uploadedfiles/2024_congressional_innovation_scorecard.pdf)  
35. AI regulation in the EU, the US and China: An NLP quantitative and qualitative lexical analysis of the official documents, fecha de acceso: marzo 22, 2026, [https://jelt.padovauniversitypress.it/system/files/papers/JELT-2024-2-7.pdf](https://jelt.padovauniversitypress.it/system/files/papers/JELT-2024-2-7.pdf)  
36. Se conocieron los proyectos ganadores de una nueva edición del concurso INNOVAR, fecha de acceso: marzo 22, 2026, [https://www.argentina.gob.ar/noticias/se-conocieron-los-proyectos-ganadores-de-una-nueva-edicion-del-concurso-innovar](https://www.argentina.gob.ar/noticias/se-conocieron-los-proyectos-ganadores-de-una-nueva-edicion-del-concurso-innovar)  
37. Vota Inteligente \- \#LaElecciónEsNuestra, fecha de acceso: marzo 22, 2026, [https://votainteligente.cl/](https://votainteligente.cl/)  
38. Create Interactive Dashboards With Streamlit in Python \- GitHub, fecha de acceso: marzo 22, 2026, [https://github.com/singhishita/Interactive-Dashboards-With-Streamlit](https://github.com/singhishita/Interactive-Dashboards-With-Streamlit)  
39. ¿Qué es la visualización de datos? \- AWS, fecha de acceso: marzo 22, 2026, [https://aws.amazon.com/es/what-is/data-visualization/](https://aws.amazon.com/es/what-is/data-visualization/)  
40. ¿Qué es la visualización de datos? Definición, ejemplos y recursos. \- Tableau, fecha de acceso: marzo 22, 2026, [https://www.tableau.com/es-mx/learn/articles/data-visualization](https://www.tableau.com/es-mx/learn/articles/data-visualization)  
41. Technology convergence: Trends, prospects and policies: OECD Science, Technology and Innovation Outlook 2025 | OECD, fecha de acceso: marzo 22, 2026, [https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025\_5fe57b90-en/full-report/technology-convergence-trends-prospects-and-policies\_5902a07e.html](https://www.oecd.org/en/publications/oecd-science-technology-and-innovation-outlook-2025_5fe57b90-en/full-report/technology-convergence-trends-prospects-and-policies_5902a07e.html)  
42. Parline API | IPU Parline: global data on national parliaments, fecha de acceso: marzo 22, 2026, [https://data.ipu.org/data-tools/api/](https://data.ipu.org/data-tools/api/)  
43. Visualización de datos: qué es, ejemplos y principales herramientas \- ESIC, fecha de acceso: marzo 22, 2026, [https://www.esic.edu/tecnology/visualizacion-de-datos-que-es-ejemplos-principales-herramientas-c](https://www.esic.edu/tecnology/visualizacion-de-datos-que-es-ejemplos-principales-herramientas-c)  
44. Methods of Assessing Science \- NCBI \- NIH, fecha de acceso: marzo 22, 2026, [https://www.ncbi.nlm.nih.gov/sites/books/NBK26384/](https://www.ncbi.nlm.nih.gov/sites/books/NBK26384/)  
45. Value of Science 202: Quantitative Methods for Impact Assessments \- RFF.org, fecha de acceso: marzo 22, 2026, [https://www.rff.org/publications/explainers/value-of-science-202-quantitative-methods-for-impact-assessments/](https://www.rff.org/publications/explainers/value-of-science-202-quantitative-methods-for-impact-assessments/)  
46. Regulation now shapes innovation as much as technology \- here's why it's an infrastructure investment \- The World Economic Forum, fecha de acceso: marzo 22, 2026, [https://www.weforum.org/stories/2026/01/technology-regulation-must-be-embraced-as-an-infrastructure-project/](https://www.weforum.org/stories/2026/01/technology-regulation-must-be-embraced-as-an-infrastructure-project/)  
47. Science, Technology and Innovation Initiatives \- Inter-American Development Bank, fecha de acceso: marzo 22, 2026, [https://www.iadb.org/en/who-we-are/topics/science-and-technology/science-and-technology-initiatives](https://www.iadb.org/en/who-we-are/topics/science-and-technology/science-and-technology-initiatives)  
48. Competitiveness Technology and Innovation \- IDB, fecha de acceso: marzo 22, 2026, [https://www.iadb.org/en/who-we-are/topics/science-and-technology/competitiveness-technology-and-innovation](https://www.iadb.org/en/who-we-are/topics/science-and-technology/competitiveness-technology-and-innovation)  
49. CIPPEC y Fundar se unen para proponer un diálogo impostergable ..., fecha de acceso: marzo 22, 2026, [https://www.cippec.org/necesitamos-un-estado-inteligente/](https://www.cippec.org/necesitamos-un-estado-inteligente/)

[image1]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAAZCAYAAACRiGY9AAACU0lEQVR4Xu2WP2sUURTFT/5gQkAERQjEyKoICoKimFgYWAslTSCFjaCF+AkUGwsRFMRKJWAIYggRUUmakEqLQAgkTUgjYmOT3g+h53jn7c7efbM7E9diyfzgsLP3zdx5d+a8Ow8oKdk3HKEWqFlqwI11Hb3UFPWVukZNU0vUcPqkbuMzmgvYoeZcrGs4RE34ILq4KK2b1z4Ii3+jLviB/0U/zPcX/cAeqFCfXKyHukHdTo6LMoYCc6tQW9R48l/F/YLdXFyhBpPjvDyg7lBPqJ/Ub+oN9QPFC3oPuz5ogzqRjCnX/eS3hhbxCuwNpZFF1LF08kM3lge17ssupof1nDrn4q3QNd+pe1QfNQJ74GFOx1AvsIZO2PVB2ELWU7kJm0hRXlEHfJBcpV7AJpgHvXHPYVhX1e9bN/Y3sSa+7AdQL+oj9raoZb0Yij9FcQum0bWPqeuwXA2oUk1cT84Timryaw6G0Gw9oTyaROzpF+UWzA1a7w2EoqouLmZgYx5N7Dhab3Wq1GkfhFlZOVV0GuVTZyuCbBx1Q7CfH9TWJnQsj26usWfIXhd6E7KGRx1WTckT7pWVL4aKOumDgbPUKqzTSYvUJVjXeURtwhZl4Cg1n8TPpOKBCvWBugvrWl+obWod2W9X+XYRz5dFWwvLUuep0UhcFlWBnpeIT6IK87pQ99PuXNuldutSlozli3EQ9u3qOFrwMbvEvk95mEQ8Xwzt9Nd88F/RBzurzS/ALFoE5ZNl86Ju3dENsWzU9AVPccoHcqB8MYtn8Q6t51BSUtIh/gBFK1is8QjvaAAAAABJRU5ErkJggg==>

[image2]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAmwAAAA3CAYAAACxQxY4AAAEM0lEQVR4Xu3d3atmUxwH8MVovEQ0kpeUQxSS12iUl1GkpFCK8RKK4kIiKcmlwgUlNOVC5MqklPJSXCm54Upu3Ey5cOGPYH1n7+2ss+Y55zxzOs950edTv9baez1n9p599eu39l6rFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANhxnq/xWo07a7zVjQEAsAOcXuPtsf9VOwAAwM7wUo19NZ6ucUE3BgDADvDd2CZhe68dAAAAAAAAAAAAgE1yV41XNxAAAGyhn2r8U+PKfmCGLPfxc42X+wEAABbnpDIkbIl5/dGfAADYbbKO2ZQEJbJrQOvGZqyP1lKNN2q8UIa/eX3F6OZ5rAzX/rAfWEOqbdvt7Bof1HimDLsyHFo5DACwtmtqPNufbHw6RutI0z+/xifNcdZGu6I53mzflyFpu6kf2KGSMOaeJx/XONAcAwCs63CNvf3JRpKjy8Z+Kmjx2djGLzX2N8fvNv1FmVXl2yov9ieqh/oTjW9qPNgcp6oJAHBc1kt8pvETyuz9OlNRy2/uL8NvtsIDZbhmW9mb11NlqBBO9/rn2P5d46Kxv5a8S/dFc5xdFs5rjnupqOVen6hxYjcGALCuTIeulbCdUZanQ28ow+9nSRLzdRn+rWlPzyREt/33i813bRmu1043rifv151Whr/L/d1dlv9/6S+N/bi36c+SpC3J2jySqH1ehuteNZ7rn0+eIQDAMd6s8UN37v2mnyTmwNjPy/J7alwyRpw6tpMkRLeM/SQgZzVji7DRqdEpSUub/2McHNvJhd1x75WystI2S5+ELdV4fOz3z6d/lgAAR/1ejv3gYErGIglNqmytVNImU/IxSQVuSkJubgcaj9T4do04c/mn6/qyrD0dOcu+GreO/SR70/1m6nJybtOfJclWrju1q5muM0n1cWnst88nFbjrmmMAgKPTcVmANglLkopUxbIsR1utumM8vr4My1KkwvZrWZ7yjCM1bh/7+WozCVTkK9EkQKnILcpGdzLIPT039rNOWz6oOLksv9P26NgujW2vf2etf6et9WONh8f+pWVY/Df655P2eJYqAQCY2zllqFhlejBta7UkZjMkmdxowhZZamOqJCb56qt6mzWVmyQt18qXoVn+pNU/n9+6YwCAhXunLGbR2iRYa01D9u7pT8wh7/YtWvt8UrV8cnkIAGD3SoIzTSvOI1W4462W5RpbWe26rwx7nvYVSgCAXSfvmM07DXpxGd5PO9QPAACwOKmsTct4zBvtBxIAAAAAAAAAAAAAAMD/3LQjwWqya0F2I7i8HwAAYGustkdpK3ucStgAALZBdjg42J+cQcIGALCNDo/t3jJsSt9GNmIPCRsAwDbZU+Oj/mTnlDIsmvtXPwAAwGJdXWP/GAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALAb/AtUGZIbj/f2PwAAAABJRU5ErkJggg==>

[image3]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABUAAAAZCAYAAADe1WXtAAABOklEQVR4XmNgGAWjYGgBcSAWQhdEA0xALIMuiAtMA2I+ID4LxKuRxBcB8X8omxmIm6F8G7gKHEAQiA2gbJAGZENBloAwDEgA8QMgNkUSwwrYoLQUA6oGRgaIJbVQPgyAXM+LJsYCxHpoYmDgzoCqAUSDDAWJI4NqND4IWAJxEbogKLw60CRUGSBe10ASA6mzReLDACcQc6MLggw4yYBqQCwQzwBiLiSxEAZIsCADkB5DNDEwEAbi7UCsCeWDNJYwoBoKitB5UDYM8ABxJBD3ADE7mhwYgAx+DcRHgXgvA8SCE0B8G4iPAXEuA6pGASBOBGIOBkiShEU4BgDZrMSAUACKVVAy4oerwASgVANyBFVBBgMNDO2HYqoCUJgTzGHEAFBYgzIFqIBZy0C4ICIKgCJ0GRB3o0sMLQAAuZwnxrm4YjkAAAAASUVORK5CYII=>

[image4]: <data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAZCAYAAAArK+5dAAABjUlEQVR4Xu2VTStEURjHHy/RYOFlYUi6XjYWlIUpZUEpFiRLSlHIWjZWiqyQnWRjaSvKy8K3sPMBLHwI/v95zpmenjsWd+6s5Fe/bvd/z9znzJnnnBH5p0Ya4CC8hkewJ+TbsCsOysMV/ITLcAe+w3nRgm1mXGY64A0cqJLfwlmXZ2YVfvkwsAcTH2blGX77MLDvg1qIBRKXEy5Tbubgh2iRKO9b7aA8sD3ZLbYAPYTNZlzdaIfHokXW3LMJSRfl/ZLLyvABP1CNRLTAhsm64SPsNBmZll+6MIF3PgxwF7PAgsm4lOPmPlKAJR8StuCbDwOL8ED0pRHONB4fkUY4KellK8MjgLO0LyFFeB+ukTG4C19Mxhbmb3UOL0xe4QEOi545bMtT+CR6bPSZcb1wC56IHh0RZk2iZ9ilySuMhitnMiPaluuS/kaRV9GT1cNl3vRhVrjpOMsWOOKesUC/yzLDl7KjuHR2h7NgLJwb9r/vFnbWlMtywyIroi3KVuYGrCtsCv6lnsEh9+yP8AP3zjepT/gUOQAAAABJRU5ErkJggg==>