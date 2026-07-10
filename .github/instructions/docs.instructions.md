---
applyTo: "**/*.md"
description: "Guía de estilo y estructura para documentación Markdown del proyecto. Usa cuando escribas, edites o revises archivos .md: idioma, formato narrativo, linting, enlaces, referencias académicas y convenciones de nombrado."
---

# Guías de documentación para archivos Markdown

- Los nombres de archivo deben estar en inglés y usar formato kebab-case (p. ej., `smart-contracts-guide.md`, `installation-troubleshooting.md`)
- Los nombres de carpeta también deben seguir la convención kebab-case en inglés
- Encabezados: Usar una jerarquía adecuada (#, ##, ###) pero evitar una profundidad excesiva para mantener la estructura simple. Todos los encabezados deben ir seguidos de una línea en blanco.
- Todas las explicaciones, descripciones y textos deben escribirse en español (idioma nativo del proyecto)
- Usar términos técnicos en inglés cuando sean estándar de la industria (p. ej., "smart contracts", "blockchain", "stack")
- La prosa narrativa es el estándar por defecto para el cuerpo de cada sección. No usar tablas o texto en negrita, y no recurrir a listas con viñetas o numeradas como atajo para lo que debería ser una explicación fluida. Las listas siguen siendo aceptables solo para elementos que no necesitan conexión narrativa (una lista de archivos, un conjunto de opciones) o para contenido que genuinamente no puede ser prosa (un bloque de código, un glosario).
- Evitar emojis en la documentación.
- Evitar aperturas pedantes que sepulten al lector en jerga antes de establecer contexto. Los documentos a menudo sirven a múltiples audiencias a la vez (curiosos del mercado retail, founders y ocasionalmente profesionales), por lo que un punto de entrada accesible importa incluso en material de profundidad técnica.
- Explicar con lenguaje claro y términos simples. Claridad y precisión por encima de brevedad: no escribir denso, parco ni pedante. Preferir frases directas a construcciones recargadas.
- Describir acciones concretas de actores, no procesos abstractos. Decir quién hace qué (el usuario deposita, el agente adelanta los fondos), no fórmulas vacías como "eso arranca el camino lento" que no dicen nada verificable.
- Al explicar un mecanismo, un primer párrafo dice qué es y el siguiente recorre las interacciones. Ese recorrido es una secuencia concreta de quién hace qué, en orden y empezando por el usuario (con su dapp o wallet): quién crea la operación, a quién se manda, quién paga, quién inicia cada paso y quién liquida al final. Nombrar en cada paso el agente de ejecución que interviene, sin dejar acciones colgando de un "el sistema" o "el protocolo" sin sujeto.
- No usar un término técnico (p. ej. "settlement canónico") sin explicarlo la primera vez que aparece, ahí mismo y en palabras simples. Si se usa una sigla, desarrollarla al introducirla.
- Evitar metáforas imprecisas que falseen el mecanismo (p. ej. "los tokens viajan" cuando en realidad se bloquean en una cadena y se libera el equivalente en otra). Describir lo que ocurre de verdad.
- Linting: Seguir las reglas de markdownlint, como asegurar que no haya espacios adicionales en los encabezados y rodear los bloques de código con líneas en blanco.
