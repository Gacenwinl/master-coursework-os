# Master Coursework OS (SOP 2.1)

UK master coursework **workflow template** — SOP, prompts, intake forms, and project scaffolding.  
**Not** a ghostwriting kit: you own the argument, sources, and submission.

> *AI may support my process, but brief interpretation, core argument, source verification, final judgement, and academic responsibility must remain mine.*

---

## Quick start

```powershell
git clone https://github.com/Gacenwinl/master-coursework-os.git
cd master-coursework-os
python create_coursework_project.py
```

Then open the **new assignment folder** in Cursor (or open this repo and work inside the generated subfolder).

| Step | File |
| --- | --- |
| 10 min guide | [Next_Assignment_Quickstart.md](Next_Assignment_Quickstart.md) |
| Main SOP | [02_SOP/Master_Coursework_SOP_2.0.md](02_SOP/Master_Coursework_SOP_2.0.md) |
| Distinction (70+) | [02_SOP/Distinction_Target_SOP.md](02_SOP/Distinction_Target_SOP.md) |
| Prompt index | [04_Prompt_Library/Prompt_Library_2.0.md](04_Prompt_Library/Prompt_Library_2.0.md) |
| Chinese overview | [00_README_如何使用.md](00_README_如何使用.md) |

---

## What you get

- **Module 0** AI policy gate (Modes A / B / C)
- **15-step SOP** + UK compliance + **Distinction five-gate overlay** (2.1)
- **ChatGPT prompt library** (intake → rubric → review → declaration)
- **Cursor bootstrap** + `.cursor/rules` for academic integrity
- **`create_coursework_project.py`** — scaffolds `01_Brief` … `06_Final`
- **`tools/verify_bib_keys.py`** — check `\cite{}` keys exist in `refs.bib`

---

## GitHub: use as template

On GitHub: **Settings → General → Template repository** ✓  
Next assignment: **Use this template** → new repo, or `git clone` again.

Keep **graded essays / brief PDFs / personal AI logs** in the **assignment repo** you generate — not in this template repo.

---

## Repo layout

```text
├── README.md                 ← you are here
├── AGENTS.md                 ← Cursor Agent entry
├── .cursor/rules/            ← integrity + LaTeX rules
├── create_coursework_project.py
├── tools/
├── 01_Intake_Form/
├── 02_SOP/
├── 03_Templates/
├── 04_Prompt_Library/
└── 05_Project_Template/
```

---

## License

MIT — see [LICENSE](LICENSE). Use and adapt for personal study; follow your university AI and integrity policies.
