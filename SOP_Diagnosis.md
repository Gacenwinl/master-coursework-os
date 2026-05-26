# SOP 诊断报告（v1 → v2.0）

**依据**：`Project_Evidence_Map.md`、`Galison_Assignment/` 执行痕迹、`Master_Coursework_OS/` 现有文件。  
**原则**：不美化；未确认项已标注。

---

## 2.1 当前 SOP 的优点

| 维度 | 证据 | 评价 |
| --- | --- | --- |
| **Rubric-first** | `RUBRIC_MAPPING`、`COMPLIANCE`、ChatGPT 终检对照指南 | 非常适合英硕；应保留为 Step 2 |
| **AI 协作管理** | `02_ai_logs` I-01–I08、`ai_collaboration_record` | Mode C 强；Mode B 可降为轻量 log |
| **文献风险** | `REFERENCE_VERIFICATION`、`PHASE3_LITERATURE_AI` | 有效；AI 不生成书目已制度化 |
| **LaTeX / 格式** | `compile.ps1`、`validate_pdf.py`、IEEEtran | 技术类作业高价值 |
| **Deadline** | 25h `task_plan`、Phase 分块 | 可缩放为 8h/20h/40h **投入档位** |
| **Cursor 可执行** | `CURSOR_PROMPTS` 归档/LaTeX 指令 | 比纯 ChatGPT SOP 更可落地 |
| **合规层（v1.5）** | `Module0`、`UK_Compliance` | 补上英硕最大短板 |

---

## 2.2 冗余步骤（未来不必每次重做）

| 冗余 | 原因 | 2.0 处理 |
| --- | --- | --- |
| 双份执行指南 | workflow + archive 根目录副本 | 只保留 OS；项目内单份 `task_plan` |
| 6000 行 ChatGPT 导出进工作流 | 检索难 | 导出放 `01_Brief/exports/` 备查，不进入每日路径 |
| I-xx 与 `ai_collaboration_record` 双写 | 末期补 6000 字 | **边写边记**；Mode B 用短 log |
| `md_to_body` 每次 compile 覆盖 | 改 tex 未改 md 会丢 | 冻结后关闭同步或单向 md→tex |
| 过多 project_control md | TASK_BOARD + STATE + COMPLIANCE 重叠 | 合并为 `task_plan` + `final_checklist` |
| 11 个独立 prompt 文件 + 长总册 | 查找成本 | `Prompt_Library_2.0` 索引 + 按步编号 |
| 手动建 8 目录 | 重复 | `create_coursework_project.py`（已有） |

**可合并的表**：`literature_table` + `reference_verification` → 一张表三列状态即可（2.0 仍提供双表选项，默认合并版 csv）。

---

## 2.3 风险（英硕语境）

| 风险 | 本项目表现 | 2.0 缓解 |
| --- | --- | --- |
| **Academic integrity** | 南邮明确鼓励 AI + 50 分记录 | **Module 0** 每课查 policy；Mode A/B/C |
| **AI 过度介入** | ChatGPT 英文段落草稿多 | Mode B：critique only；`core_argument_paragraph` 亲手 |
| **流程=学会** | 25h 走完但 oral 未强制 | Learning checkpoint §0.4 |
| **上传课程材料** | 指南 PDF 给 ChatGPT 终检 | 优先摘要；学校工具；不上传 slides 全文 |
| **Group / 隐私** | 本项目 individual | Module 0 Q6；不上传组员文稿 |
| **虚假文献** | 已用核查表 | 保持 Verified 门禁 |
| **无 declaration** | 南邮有 §4 | `AI_Declaration_SOP`；brief 无则简短声明 |

---

## 2.4 缺口（v1 已部分补，v2.0 固化）

| 缺口 | v1 状态 | v2.0 |
| --- | --- | --- |
| AI policy check | 已加 Module0 | 升格为 Step 1；独立 prompt |
| Learning checkpoint | 已加 | 写入 Final checklist + core_argument |
| Source verification | 有 REFERENCE_VERIFICATION | 独立 SOP + 合并表选项 |
| Oral self-check | 仅文字提示 | Quickstart 5 问 + checkpoint |
| 作业类型分支 | UK_Compliance 表 | SOP 2.0 §3.4 专节 |
| 低/中/高投入 | 仅 25h | `Effort_Levels.md` 三档 |
| Argument design 独立步 | 混在大纲 prompt | 独立 prompt + `core_argument_paragraph` |
| Post-task 迭代 | Postmortem 在 Galison 99 | `99_Review` + `post_task_review` prompt |

---

## 2.5 Cursor 视角：最有效的自动化边界

**宜自动化（Cursor/脚本）**：建目录、复制模板、从 Intake 生成 task_plan 骨架、rubric 空表、compile、validate_pdf、导出 docx、更新 PROJECT_STATE 式单行状态。

**不宜自动化**：论点选择、文献 Verified、诚信比例、是否提交、policy 解释、直接引文核对。

**曾高效的人工+Cursor 组合**：I-05 审稿表 → 直接改 LaTeX；比「ChatGPT 重写全文」快且安全。
