# Superpowers — placeholder / referencja

Ten folder na razie **nie zawiera skopiowanego kodu**. Trzyma tylko licencję na
przyszłość, na wypadek gdyby zaszła potrzeba skopiowania i sfinetunowania
jednego lub więcej skilli z frameworka [obra/superpowers](https://github.com/obra/superpowers).

Stan od 2026-08-07: plugin jest **faktycznie zainstalowany** (v6.2.0, scope
`project`, z oficjalnego marketplace'u `claude-plugins-official`) i deklarowany
w `.claude/settings.json` → `enabledPlugins`. Jego kod mieszka w cache
użytkownika (`~/.claude/plugins/cache/…`), **nie tutaj** — nie kopiuj go do tego
folderu „dla porządku". Szczegóły: `issues/claude-code-pluginy.md`.

Licencja: MIT (Jesse Vincent), patrz `LICENSE` w tym folderze — dotyczy tylko
tego, co ewentualnie tu wyląduje, nie reszty repo matematykazen.

Gdy faktycznie skopiujesz jakiś skill (np. `skills/brainstorming/`), wrzuć go
jako podfolder tutaj, np. `vendor/superpowers/brainstorming/`, obok tego pliku
LICENSE.
