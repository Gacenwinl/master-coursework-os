# Master Coursework SOP 2.0（英国 Master 主流程）

> **唯一主 SOP**。v1：`Academic_Task_SOP.md`（保留作细节参考）。  
> **前置必读**：`Module0_AI_Policy_Gate.md`、`UK_Compliance_and_Modes.md`、`Effort_Levels.md`。  
> **冲 Distinction（70+）**：叠加 `Distinction_Target_SOP.md`（OS 2.1）。

## 3.1 总原则

1. **AI 辅助流程，不替代判断** — planning / critique / format OK；ghostwriting NO（Mode B）。  
2. **永远属于你**：brief 理解、core argument、文献 Verified、final judgement、提交责任。  
3. **每课先查 module AI policy** — 无查清不进写作 prompt。  
4. **按 Mode A/B/C 与投入档位调节** — 非每次满配。  
5. **固定句**：*AI may support my process, but the brief interpretation, core argument, source verification, final judgement, and academic responsibility must remain mine.*

---

## 3.2 三种工作模式（摘要）

| | Mode A | Mode B（默认） | Mode C |
| --- | --- | --- | --- |
| **场景** | 禁 AI / exam | essay, report, lit review | 强制 AI 记录/反思 |
| **AI 可做** | 几乎无 | 规划、critique、润色片段 | + 长 log、比例声明 |
| **AI 不可** | 生成正文 | 定论点、生成书目、代写核心段 | 编造交互/文献 |
| **AI log** | 无 | 轻量（建议） | 完整 |
| **Declaration** | 按 brief | 按 brief | 必须 |
| **Workflow** | 步骤 1–2,6–7,11–14 | 全流程 | 全流程 + §5 扩写 |

详见 `UK_Compliance_and_Modes.md`。

---

## 3.3 标准执行流程（15 步）

图例：**A**=你 · **B**=ChatGPT · **C**=Cursor · **D**=你核查 · **保留**=项目内文件 · **自动**=脚本/Cursor

| # | 步骤 | A | B | C | 产出 | 保留 | 自动 |
| ---: | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Intake** | 粘贴 brief/rubric | 解析清单 | 建项/复制模板 | `01_Brief/Assignment_Intake_Form.md` | ✓ | 部分 |
| 2 | **AI policy check** | 读 handbook | — | 复制 Module0 | `01_Brief/Module0_AI_Policy_Gate.md` | ✓ | 模板 |
| 3 | **Rubric mapping** | 确认行 | 生成表 | 写入 md | `rubric_mapping_table.md` | ✓ | 骨架 |
| 4 | **Task plan** | 选档位/日期 | 建议分配 | 生成 md | `task_plan.md` | ✓ | 部分 |
| 5 | **Literature strategy** | — | 关键词/类型 | — | 检索计划（可并入 plan） | 可选 | 否 |
| 6 | **Reading notes** | 读+笔记 | 解释概念 | — | `02_Notes/reading_notes.md` | ✓ | 否 |
| 7 | **Argument design** | **写 core argument** | 评可选方案 | — | `02_Notes/core_argument_paragraph.md` | ✓ | 否 |
| 8 | **Drafting** | **写正文** | 润色已有段 | md→tex | `04_Draft/draft.md` | ✓ | 部分 |
| 9 | **AI critique** | 采纳/拒 | 严师表 | 改稿 | 审稿笔记 | 可选 | 否 |
| 10 | **Source verification** | **Verified** | 风险扫描 | 更新 bib | `03_Literature/*` | ✓ | 否 |
| 11 | **Formatting** | 目视 PDF | — | LaTeX/Word | `06_Final/*.pdf` | ✓ | 部分 |
| 12 | **Final checklist** | 勾选 | 对照 brief | validate 脚本 | `06_Final/final_submission_checklist.md` | ✓ | 部分 |
| 13 | **AI declaration** | **诚实签署** | 草稿 | 排版 | `06_Final/ai_declaration.md` | 若要求 | 模板 |
| 14 | **Submission archive** | 上传 VLE | — | 备份清单 | `06_Final/` + 截图 | ✓ | 否 |
| 15 | **Post-task review** | 写复盘 | — | 归档 | `99_Review/postmortem.md` | 可选 | 模板 |

**Mode A 跳过**：5,8,9 的 B；**Mode C 加强**：9 后增 AI log 定稿（`05_AI_Log/`）。

---

## 3.4 作业类型调整

| 类型 | 重点 | 加强步骤 | 可简化 | AI 风险 | 终检重点 |
| --- | --- | --- | --- | --- | --- |
| **Essay** | 论点+文献 | 7,9,10 | 11 若 Word | 代写正文 | 是否答题 |
| **Report** | 结构+证据 | 4,8 | — | 虚构数据 | 图表/附录 |
| **Reflective** | 真实经历 | 7（亲手） | 5,10 若少引用 | AI 编造经历 | 真实性 |
| **Lit review** | 文献矩阵 | 5,6,10 | 8 少原创实验 | 假文献 | 综述结构 |
| **Technical paper** | 格式+图 | 11,C compile | — | 设备百科 | IEEE/页码/缩略语 |
| **Coding/data** | 可复现 | 10 数据出处 | 8  prose 少 | AI 改结果 | 政策+repo |
| **Group** | 分工 | Module0 Q6 | 共用上载 AI | collusion | 贡献声明 |
| **Dissertation proposal** | RQ+gap | 5,7 | 11 | 过度野心 | 方法与文献 |

---

## 3.5 与 Galison 项目差异

| Galison | 英硕默认 |
| --- | --- |
| Mode **C** | Mode **B** |
| 双 PDF 50/50 | 常单 PDF + 短 declaration |
| 8×600 字交互 | 3–5 条轻 log 或零 |
| IEEE 6–8 页 | 按 brief |

Galison 文件留在 `Galison_Assignment/` 作范例，**不要**整夹复制为新课项目。

---

## 3.6 10 分钟启动（见 `Next_Assignment_Quickstart.md`）

## 3.7 Prompt 与自动化

- Prompt：`04_Prompt_Library/Prompt_Library_2.0.md`（主索引）+ `01`–`15` 单文件  
- 自动化：`Automation_Opportunities.md`  
- 脚本：`create_coursework_project.py`

---

## 3.8 Distinction 叠加（Target grade = Distinction）

**不增加 SOP 步骤编号**；在步骤 7–12 之间插入五关卡（详见 `Distinction_Target_SOP.md`）：

| 关卡 | 插入位置 | 产出 |
| --- | --- | --- |
| A 可反驳论点 | 步骤 7 前后 | `thesis_objection_worksheet.md` |
| B 文献配额 | 步骤 6–10 | reading notes + verification |
| C Red team | 步骤 9（第一轮） | `15_distinction_red_team` + 正文 3 处回应 |
| D 去模板段 | 步骤 8–9 之间 | 修订 draft |
| E 口头预演 | 步骤 12 前 | `oral_defence_prep.md` |

终检：`03_Templates/distinction_checklist.md`（≥8/10）+ `final_submission_checklist.md`。  
档位：**High**（`Effort_Levels.md`）。模式：**Mode B** 优先。
