# SOP 2.0 升级报告

**执行方**：Cursor（基于 `Galison_Assignment` 实际执行痕迹）  
**日期**：2026-05-26  
**未修改**：Galison 已提交 PDF / 终稿 LaTeX；未删除任何原始文件。

---

## 做了哪些升级

| 区域 | v1 / v1.5 | v2.0 |
| --- | --- | --- |
| 主流程 | `Academic_Task_SOP` + 分散 md | **`Master_Coursework_SOP_2.0.md`**（15 步 + A/B/C/D） |
| 合规 | 后加 Module0 | **Step 1 强制** + `AI_Policy_Check_SOP` |
| 主体性 | 原则句散落 | `core_argument_paragraph` + Learning checkpoint |
| Prompt | 8 文件 | **16+ 文件** + `Prompt_Library_2.0` 索引 |
| 投入 | 固定 25h | **`Effort_Levels`** Low/Med/High |
| 诊断 | Postmortem 在 Galison | **`SOP_Diagnosis` + Evidence Map** 在 OS |
| 启动 | 新作业流程 md | **`Next_Assignment_Quickstart`** 10 分钟 |
| 模板 | 已有 | + `reading_notes`、policy/declaration SOP |
| 自动化 | 脚本 v1 | **`Automation_Opportunities`** 明确边界 |

**未盲目覆盖**：v1 的 `01`–`08` prompt、`Academic_Task_SOP`、`Reference_Verification_SOP` 均保留。

---

## 为何适合英国 Master

- 默认 **Mode B**（critique > ghostwrite），非 Galison Mode C  
- **Module 0** 每课查 AI policy（手册差异大）  
- 上传材料保守规则（brief 摘要、禁 slides 全文）  
- Rubric / 文献核查 / 终检 — 与 marking criteria 文化一致  
- 保留 **learning checkpoint**，防「流程走完=学会」

---

## 降低的风险

| 风险 | 机制 |
| --- | --- |
| Integrity | Module0、Mode、declaration SOP |
| 过度 AI 写作 | 04b 只选论点；05 只审稿 |
| 假文献 | 06 + Reference SOP |
| 隐私 | Module0 Q4–Q7 |
| 重复劳动 | 脚本 + bootstrap + Quickstart |

---

## 自动化的部分

见 `Automation_Opportunities.md`：建项、模板、编译、validate、docx 导出。  
**未自动化**：论点、Verified、签署、提交决定。

---

## 保留的人工判断

Brief 理解 · Mode 选择 · Thesis · 文献 Verified · 采纳 critique · 诚信比例 · 终检提交 · Oral checkpoint

---

## 你下次怎么用

1. 只打开 **`Master_Coursework_OS/`**，不要复制整个 Galison  
2. `Next_Assignment_Quickstart.md` → `create_coursework_project.py`  
3. 跟 **`Master_Coursework_SOP_2.0.md`** 15 步  
4. Prompt 用 **`Prompt_Library_2.0`** 顺序  
5. 交完后 `14_post_task_review` + `99_Review/postmortem.md`

---

## 未来可迭代

- [x] `tools/verify_bib_keys.py`（stdlib）  
- [x] 脚本复制 `reading_notes_template`  
- [x] Cursor rules + `AGENTS.md`（工作区根目录）  
- [ ] `01_Intake` 文件夹别名（当前 `01_Intake_Form`）  
- [ ] 合并 literature + verification 单 csv 默认版  

---

## 文件导航（2.0 新增/主文件）

| 文件 |
| --- |
| `Project_Evidence_Map.md` |
| `SOP_Diagnosis.md` |
| `02_SOP/Master_Coursework_SOP_2.0.md` |
| `04_Prompt_Library/Prompt_Library_2.0.md` |
| `Next_Assignment_Quickstart.md` |
| `Automation_Opportunities.md` |
| 本报告 |
