# Project Evidence Map（基于仓库扫描）

**扫描日期**：2026-05-26  
**证据来源**：`Galison_Assignment/`（南邮 Galison 作业，已交付）+ `Master_Coursework_OS/`（从本项目抽象的 OS v1/v1.5）  
**说明**：工作区 glob **未能索引** `*.pdf` 二进制；终稿 PDF 存在性依据 `PROJECT_STATE.md`、用户确认及 `07_final/` 说明文件。

---

## 1. 关键文件与流程作用

| 路径 | 流程阶段 | 作用 | 未来 |
| --- | --- | --- | --- |
| `Galison_Assignment/00_input/official/课程论文指南.html` | Intake | 官方 rubric（无独立 PDF 在库） | 模板：每课 `01_Brief/brief.html\|pdf` |
| `00_input/chatgpt_exports/策略规划.md` | Phase 1 | ChatGPT 会话 0 全文（~6000 行） | 备查；**不复制进 OS**（过大） |
| `00_input/chatgpt_exports/A：论文生产.md` | Phase 2–5 | 会话 A：理论/案例/大纲/草稿/终检对话 | 备查 |
| `00_input/workflow/执行指南报告.md` | Phase 1 | 25h 路线图（ChatGPT 生成） | 抽象为 `task_plan` 逻辑 |
| `01_project_control/RUBRIC_MAPPING.md` | Intake | 评分映射 | → `rubric_mapping_table.md` |
| `01_project_control/CURSOR_PROMPTS.md` | 全程 | **Cursor 实际执行指令库**（每日启动、归档、LaTeX） | → OS `04_Prompt_Library` + bootstrap |
| `01_project_control/SUBMISSION_CHECKLIST.md` | Phase 7 | 终检勾选 | → `final_submission_checklist` |
| `01_project_control/COMPLIANCE_*.md` | Phase 7 | 对照指南 | → Final checklist SOP |
| `02_ai_logs/I-01`–`I-08` | Phase 1–8 | 八条交互摘要（部分 (b) 曾外链导出） | → `ai_log` 模板 |
| `03_notes/Galison_notes.md` | Phase 2 | **人工** G1–G4 锚点 | → `reading_notes` + 原著笔记 |
| `03_notes/semiconductor_case_notes.md` | Phase 3 | 案例边界 | → 学科 notes |
| `04_references/REFERENCE_VERIFICATION.md` | Phase 3–7 | 文献状态机 | → `reference_verification_table` |
| `04_references/refs.bib` | Phase 3–5 | 21 条 BibTeX | 每项目独立 bib |
| `05_paper/paper_draft.md` | Phase 4 | Markdown 内容源 | → `04_Draft/draft.md` |
| `05_paper/latex/main.tex` | Phase 5 | IEEEtran 壳 + Abstract/Keywords | 技术课 LaTeX |
| `05_paper/latex/md_to_body.py` | Phase 5 | **compile 前同步** body | 自动化候选；注意覆盖风险 |
| `05_paper/latex/compile.ps1` | Phase 5 | pdflatex+bibtex；TEMP 编译防 Synology 截断 | 项目级脚本模板 |
| `05_paper/latex/validate_pdf.py` | Phase 5 | 页数/引用检查 | 终检自动化 |
| `06_ai_report/ai_collaboration_record.md` | Phase 6 | AI 记录终稿（~6700 字） | Mode C 才需要 |
| `07_final/*.pdf`（命名见 README） | 交付 | 双 PDF 提交 | `06_Final/` |
| `99_Project_Review_Assets/*` | 复盘 | Postmortem、初版 SOP | 不进入每课项目 |
| `Master_Coursework_OS/*` | 元层 | OS v1 + 合规层 | **SOP 2.0 主维护区** |

---

## 2. Cursor 实际执行过的痕迹（可确认）

| 操作 | 证据 |
| --- | --- |
| 项目结构搭建 | `Galison_Assignment/README`、多目录 |
| I-05 审稿表 → 修补 draft/LaTeX | `I-05_draft_review.md`；`paper_body` 含 Table I / Fig.1 |
| LaTeX 工程 | `main.tex`、`figures/`、`tables/`、`ieee_section_format.tex` |
| 编译流水线 | `compile.ps1`（含 md→body 同步、TEMP build） |
| AI 记录汇总扩写 | `ai_collaboration_record.md` 修订（对话记录） |
| 合规/终检 md | `COMPLIANCE_课程论文指南.md` |
| 目录整理 | `00_input` 分子目录（official/chatgpt_exports/workflow） |
| OS 母项目 | `Master_Coursework_OS/` 全套 |
| ChatGPT 终检后小修 | Abstract/Keywords/Conclusion（`main.tex` / `paper_draft` 修订） |

**未能从文件确认**：每次 ChatGPT 轮次是否均由用户手动粘贴归档（部分 I-xx 写「见导出」）。

---

## 3. 人工介入最多的环节（推断自文件形态）

| 环节 | 证据 | 结论 |
| --- | --- | --- |
| Galison G1–G4 直接引 | `Galison_notes.md`；ChatGPT 拒绝编造 | **必须人工** |
| 文献 Verified | `REFERENCE_VERIFICATION` 作者终检表 | **必须人工** |
| 论点与案例取舍 | `writing_decisions.md`、大纲 | **必须人工** |
| 英文正文实质改写 | 草稿与 ChatGPT 导出差异 | **人工为主** |
| AI 记录后期扩写至 6000 字 | Postmortem 记载 | 曾**低效集中**；2.0 改为并行写 log |
| PDF 目视终检 | `PROJECT_STATE` | **必须人工** |

---

## 4. 临时产物 vs 长期保留

| 临时 / 可再生成 | 长期保留 |
| --- | --- |
| `main.log`, `main.aux`, `main.bbl` | `refs.bib`, `main.tex`, `paper_draft.md` |
| `texput.log` | `Galison_notes.md`, `REFERENCE_VERIFICATION.md` |
| `00_input/archive/执行指南_根目录副本` | `chatgpt_exports`（可选压缩归档） |
| 多次 `demo*.pdf` 试编译 | `07_final` 正式命名 PDF |
| `literature_candidates.md`（若已并入 bib） | 已交付 PDF + AI 记录 PDF |

---

## 5. 可抽象为通用模板

| Galison 实例 | OS 模板 |
| --- | --- |
| RUBRIC_MAPPING | `rubric_mapping_table.md` |
| REFERENCE_VERIFICATION | `reference_verification_table.csv` |
| I-xx 六段式 | `ai_log.md` |
| CURSOR_PROMPTS §2 归档 | bootstrap + 日志更新协议 |
| SUBMISSION_CHECKLIST | `final_submission_checklist.md` |
| PAPER_OUTLINE | `draft_structure.md` |
| compile.ps1 模式 | `Automation_Opportunities.md` §脚本 |
| Module0（后加） | `Module0_AI_Policy_Gate.md` |

---

## 6. 冗余 / 重复（SOP 2.0 应合并）

| 重复项 | 建议 |
| --- | --- |
| `Academic_Task_SOP` + 将写的 `Master_Coursework_SOP_2.0` | **2.0 为唯一主 SOP**；旧版只保留链接 |
| `99_Project_Review_Assets` 与 `Master_Coursework_OS` | 前者=历史复盘；后者=执行 |
| `01_Intake_Form` vs 用户规格 `01_Intake` | 保留文件夹名 `01_Intake_Form`，README 注明别名 |
| `task_plan.md` vs `task_plan_template.md` | 2.0 统一命名 `task_plan_template.md` + 项目内复制为 `task_plan.md` |
| Prompt v1 编号文件 + `Prompt_Library_2.0.md` | v1 保留；2.0 为总册；新 prompt 增量入 v1 文件 |
