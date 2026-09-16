## 🎯 Pull Request Summary

### Description
<!-- Briefly describe the changes introduced by this PR. Include motivation, context, and archetype affected. -->

---

## 🛠️ Type of Change
- [ ] 🐛 Bugfix (non-breaking change fixing an issue)
- [ ] 🚀 New Feature / Archetype (non-breaking expansion)
- [ ] ⚠️ Breaking Change (fix or feature that would cause existing templates to render differently)
- [ ] 📝 Documentation Update (README, CONTRIBUTING, guides)
- [ ] 🔧 Toolchain / CI / Maintainer Task update

---

## ✅ Quality Checklist
Before requesting review, please confirm:
- [ ] I have read the [CONTRIBUTING.md](CONTRIBUTING.md) guide.
- [ ] I have executed `task test:render:all` locally and all 6 archetypes render successfully.
- [ ] If modifying an archetype, I tested a rendered project with `task setup` and `task check:all`.
- [ ] Jinja syntax conforms to standard trimming practices (`{%-` / `-%}`).
- [ ] All new dependencies added have zero critical/high CVEs (`uv run pip-audit`).
- [ ] My commits follow [Conventional Commits](https://www.conventionalcommits.org/).
