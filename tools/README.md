# Tools（stdlib，无安装依赖）

## verify_bib_keys.py

检查正文中的 `\cite{key}` 是否都在 `refs.bib` 里。

```powershell
# 若 `python` 不可用，用本机路径，例如 C:\Python314\python.exe
python Master_Coursework_OS/tools/verify_bib_keys.py Galison_Assignment/05_paper/latex/paper_body.tex Galison_Assignment/04_references/refs.bib
```

退出码 `0` = 通过；`1` = 有缺失 key。

Galison 为只读范例；新课程项目在 `04_Draft/` + `03_Literature/refs.bib` 上运行。
