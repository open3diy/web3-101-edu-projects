---
applyTo: "**/*.md"
---

# Documentation Guidelines for Markdown Files

## Language and Content Standards

- All explanations, descriptions, and texts must be written in Spanish (project's native language)
- Use technical terms in English when they are industry standard (e.g., "smart contracts", "blockchain", "stack")
- Maintain consistency between Spanish explanations and English technical terminology
- File names must be in English and use kebab-case format (e.g., `smart-contracts-guide.md`, `installation-troubleshooting.md`)
- Folder names should also follow kebab-case convention in English

## Formatting and Narrative Style

- Style: Maintain a clean and minimal documentation style. Explanations should be didactic and narrative, avoiding an overuse of lists. Prefer fluid text that guides the reader through concepts.
- Headings: Use a proper hierarchy (#, ##, ###) but avoid excessive depth to keep the structure simple. All headings must be followed by a blank line.
- Bold Formatting: Avoid using bold formatting (`**text**`). The only exception is for creating conceptual subgroups within a section using the format `**Title**:` followed by two line breaks to comply with linting rules.
- Lists: Use lists sparingly, only for items that don't require narrative explanation (e.g., listing files or options). When used, ensure a blank line precedes the first item.
- Code Blocks: Must not be indented and should use the appropriate language identifier (e.g., `bash`, `solidity`, `json`).
- Tabs: Do not use tabs anywhere.
- Linting: Follow markdownlint rules, such as ensuring no extra spaces in headings and surrounding code blocks with blank lines.

## Structure Guidelines

### For Stack Documentation (docs/stacks/**)

- Follow the structure: Concepto → Instalación → Configuración → Uso → Ejemplos
- Separate required tools from optional ones clearly
- Include verification commands after installation steps
- Provide troubleshooting sections when relevant
- Link to official documentation when referencing external tools

### For Installation Guides

- Provide specific commands for Ubuntu (the project's target OS)
- Include version verification steps after each installation
- Group related installations logically
- Explain what each tool does before installation instructions
- Include common troubleshooting scenarios

### For Best Practices Documentation

- Focus on security implications for blockchain development
- Include concrete code examples, not just theoretical explanations
- Reference official standards (ERC-20, ERC-721, etc.) when applicable
- Explain the "why" behind each recommendation

## Code Examples Standards

- Always specify the context where code should be executed
- Include file paths when showing configuration files
- Use realistic examples that match the project's tech stack
- Provide complete command sequences, not partial snippets

## Links and References

- Internal Links: Use relative paths for internal documentation links.
- External Links: Always verify external links are working and point to official sources. Prefer official documentation over third-party tutorials.
- Academic References: For every new theoretical concept introduced, include a link to a relevant academic paper or authoritative technical article. If no academic paper exists, a relevant high-quality article is sufficient. This reference is only required on the first mention of the concept within the document.
- Official Documentation: When referencing concrete tools, technologies, or examples (e.g., Hardhat, OpenZeppelin), always link to their official website.
- Link Descriptions: Include link descriptions in Spanish, even if the target content is in English.

## Technical Accuracy

- Verify all commands work on Ubuntu before documenting them
- Test installation procedures in clean environments when possible
- Keep tool versions current and note when specific versions are required
- Include compatibility information when relevant

## Maintenance Guidelines

- Update documentation immediately when underlying tools change
- Mark deprecated practices clearly and provide migration paths
- Keep examples aligned with the current project structure
- Review and update external links periodically
