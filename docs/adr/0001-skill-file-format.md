# ADR 0001: Lowercase skill.md as Distribution Format

**Статус:** Accepted  
**Дата:** 2026-07-01  
**Контекст:** APES Stage 1

---

## Context

APES Skills must be compatible with multiple agent IDEs: Cursor, Claude Code, Cline, Roo Code, GitHub Copilot, OpenAI Agents, Windsurf, LobeHub.

Different IDEs use different conventions:

- Cursor: `SKILL.md` (uppercase) with YAML frontmatter in `~/.cursor/skills/`
- Other tools: various paths and naming (`skill.md`, `SKILL.md`, plain markdown)

[task.md](../task.md) §6 explicitly requires:

> Each Skill is distributed as a single file: `skill.md`

> User installs exclusively the skill.md file.

---

## Decision

1. **Repository canonical name:** `skill.md` (lowercase) in each skill directory.
2. **No YAML frontmatter** in the distributed file (platform-agnostic per task.md §8).
3. **IDE-specific adaptation** is the user's responsibility at install time:
   - Cursor users rename to `SKILL.md` and may add frontmatter locally.
   - Content of skill.md remains identical across platforms.
4. **Repository-only files** (`README.md`, examples) stay in the repo and are not distributed.

---

## Consequences

### Positive

- Single source of truth for skill content
- Compatible with task.md requirements
- Works across IDEs without modification of content
- Clear separation: portable skill.md vs repo documentation

### Negative

- Cursor users must rename file manually
- Cursor auto-discovery may require frontmatter (user adds locally)
- Two naming conventions in the wild (skill.md vs SKILL.md)

### Mitigation

- Document install steps in [README.md](../README.md)
- README per skill includes Cursor-specific install note
- Future: install script (Stage 2) that copies and renames for target IDE

---

## Alternatives Considered

| Alternative | Rejected because |
|-------------|------------------|
| Use `SKILL.md` in repo | Breaks task.md §6, Cursor-specific |
| YAML frontmatter in repo | Platform-dependent, violates §8 |
| Two files (skill.md + SKILL.md) | Duplication, sync risk |
| Symlinks | Poor Windows support |

---

## References

- [task.md](../task.md) §6, §8
- [docs/SKILL_STANDARD.md](SKILL_STANDARD.md)
- [docs/ARCHITECTURE.md](ARCHITECTURE.md) §7
