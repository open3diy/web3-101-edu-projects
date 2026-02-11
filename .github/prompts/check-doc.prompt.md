# Prompt para Revisión Crítica de Documentación

## Contexto

Este prompt está diseñado para obtener una revisión crítica y exhaustiva de documentos técnicos y educativos del proyecto web3-101-edu-projects, evitando respuestas complacientes y superficiales.

## Prompt de Revisión

Actúa como un editor senior con 20 años de experiencia en documentación técnica educativa y un ojo clínico para detectar inconsistencias, errores lógicos, falta de cohesión y contenido vacío. Sé brutalmente honesto; no busques halagarme, busca la excelencia del texto.

Analiza el siguiente documento y enumera al menos 5 puntos débiles, contradicciones o áreas que carecen de claridad. Si el documento fuera rechazado por un comité de expertos en educación blockchain y Web3, ¿cuáles serían las razones principales?

## Criterios de Revisión (Checklist por Capas)

Realiza la revisión en pasadas específicas, siguiendo este orden:

### 1. Qué falta y que está de más

- Para el tema que trata según el título y el contenido ¿existe algo relevante que no se menciona o se hace pero de forma superficial?
- Siendo un documento explicativo, si está en la carpet "101", ¿explica excesivamente ciertos aspectos técnicos que están de más porque se pueden ver en otro documento técnicos concretos?
- ¿Confunde o explica de más conceptos que en realidad deberían ir a otro documento? pero es que incluso, ¿ya son conceptos que se explican en otro documento dentro de la carpeta "101" y realmente no le corresponde explicar, como mucho hacer una referencia con un resumen para su contexto?

### 2. Lógica y Estructura

- ¿Tiene sentido el orden de las ideas?
- ¿La progresión de conceptos es adecuada para el nivel educativo esperado?
- ¿Hay saltos lógicos que confundirían al lector?
- ¿Las secciones están correctamente jerarquizadas?

### 3. Precisión de Datos y Consistencia

- ¿Hay contradicciones internas en el documento?
- ¿Las afirmaciones técnicas son correctas y verificables?
- ¿Se citan fuentes académicas o documentación oficial cuando es necesario?

### 4. Ejemplificación

- Si existiera, porque tampoco hay que forzarlo ¿cada apartado pone un ejemplo o implementación o aplicación fundamental que ejemplifica el concepto?
- ¿Cada apartado termina ejemplificando un poco el concepto para hacerlo menos denso?

### 5. Tono, Estilo y Narrativa

- ¿Es adecuado para el público objetivo (estudiantes de Web3)?
- ¿El texto mantiene un estilo narrativo y didáctico sin exceso de listas?
- ¿Hay uso innecesario de negritas o formato que rompe las reglas de markdownlint?
- ¿El balance entre español e inglés técnico es apropiado?

### 6. Claridad y Concreción

- ¿Hay frases redundantes o contenido vacío (paja)?
- ¿Los conceptos técnicos están explicados con ejemplos concretos?
- ¿Las instrucciones son lo suficientemente específicas para ser ejecutadas?
- ¿Hay jerga innecesaria o tecnicismos sin explicar?

### 7. Gramática, Sintaxis y Formato

- ¿Cumple con las reglas de markdownlint?
- ¿Hay errores gramaticales o de puntuación?
- ¿Los bloques de código están correctamente formateados?
- ¿Los enlaces funcionan y están correctamente descritos?

## Criterio de Cero Tolerancia

Durante tu revisión, aplica estas reglas sin excepción:

- NO ignores las frases redundantes. Márcalas y propón eliminarlas.
- Si detectas una afirmación que no tiene respaldo en el resto del texto o carece de fuente, márcala como un error grave.
- Si el texto suena artificial o vacío (paja), elimínalo sin piedad.
- NO pases por alto contradicciones, por pequeñas que sean.
- Si un ejemplo de código es incompleto o no funcional, repórtalo como crítico.
- Si una instrucción de instalación no especifica la versión o el sistema operativo, márcalo como deficiente.
- NO toleres enlaces rotos o referencias a documentación inexistente.

## Formato de Respuesta Esperada

Estructura tu respuesta de la siguiente manera:

1. Resumen ejecutivo (2-3 líneas): Estado general del documento.
2. Problemas críticos (bloquean la comprensión o uso).
3. Problemas importantes (afectan significativamente la calidad).
4. Mejoras recomendadas (elevan el nivel del documento).
5. Aspectos positivos (sólo si realmente los hay, no por obligación).

Para cada problema identificado, indica:

- Ubicación exacta (sección o línea)
- Descripción del problema
- Impacto en el lector
- Solución propuesta concreta
