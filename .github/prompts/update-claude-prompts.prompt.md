---
description: "Sincroniza los prompts de .github/prompts con sus equivalentes en .claude/commands para que Claude Code los reconozca como slash commands. Usa cuando crees o edites un .prompt.md y quieras propagar el cambio al sistema de comandos de Claude."
---

# Sincronizar prompts con Claude Code

Este proyecto mantiene dos sistemas de prompts en paralelo: los "prompt files" de Copilot Chat en `.github/prompts/*.prompt.md`, y los slash commands de Claude Code en `.claude/commands/*.md`. `.github/prompts/` es la fuente de verdad. `.claude/commands/` debe ser un espejo fiel, adaptado solo en lo mínimo necesario para que Claude Code lo reconozca.

No incluyas este propio archivo (`update-claude-prompts.prompt.md`) entre los prompts a sincronizar.

## Procedimiento

- Recorre todos los archivos `*.prompt.md` de `.github/prompts/`, excluyendo este mismo archivo.
- Para cada uno, calcula el destino quitando el sufijo `.prompt`: `nombre.prompt.md` en `.github/prompts/` corresponde a `nombre.md` en `.claude/commands/`.
- Copia el cuerpo del prompt de forma literal. No reescribas, resumas ni parafrasees el contenido.
- En el frontmatter, conserva únicamente el campo `description` tal cual. Si el archivo origen tiene otros campos específicos de Copilot (por ejemplo `mode`), no los traslades.
- Si el destino ya existe y su contenido difiere del origen, sobrescríbelo para que vuelva a coincidir exactamente con `.github/prompts/`.
- Si encuentras un archivo en `.claude/commands/` que no tiene ningún origen correspondiente en `.github/prompts/`, no lo borres por tu cuenta: señálalo y pregunta antes de eliminarlo.

## Al terminar

Resume qué archivos creaste, cuáles actualizaste porque habían quedado desincronizados, y cuáles ya estaban al día y no necesitaron cambios.
