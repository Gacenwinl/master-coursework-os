# Prompt Library 2.0（主索引）

> 单文件完整 prompt 见各 `NN_*.md`。会话开场：`00_chatgpt_session_opener.md`。  
> **原则**：减少重复劳动；**不**自动化论点、Verified、签署。

---

## 使用顺序（Mode B 默认）

**Merit（默认）**：`00` → `02` → `01` → `02` rubric → `09` plan → `03` → `03b` → `04b` → `04` outline → [你写作] → `05` → `05b` → `06` → `13` → `07` → `12` → `14`

**Distinction 叠加**：在 `04b` 后填 **关卡 A** worksheet → [你写作] → **`15` red team** → `05` → 改稿 → **关卡 D/E** → 其余同上

---

## 1. Assignment brief analysis

| 项 | 内容 |
| --- | --- |
| **文件** | `01_assignment_intake_prompt.md` |
| **场景** | Intake 填完后 |
| **输入** | Intake Form + brief 摘要 |
| **输出** | 显性/隐性要求、风险、分工 A/B/C/D |
| **风险** | 直接写正文 |
| **变体** | Essay 强调 thesis；Report 加 methods；Reflective 禁虚构经历 |

---

## 2. AI policy check

| 项 | 内容 |
| --- | --- |
| **文件** | `02_ai_policy_check_prompt.md` |
| **场景** | **Step 1，早于一切写作 prompt** |
| **输出** | Mode A/B/C + 上传规则 |
| **风险** | 跳过→ integrity |
| **变体** | Exam → 强制 Mode A |

---

## 3. Rubric mapping

| 项 | 内容 |
| --- | --- |
| **文件** | `02_rubric_mapping_prompt.md` |
| **Galison** | RUBRIC_MAPPING + COMPLIANCE 有效 |

---

## 4. Task planning

| 项 | 内容 |
| --- | --- |
| **文件** | `09_task_planning_prompt.md` |
| **输出** | `task_plan.md` |

---

## 5. Literature strategy

| 项 | 内容 |
| --- | --- |
| **文件** | `03_literature_planning_prompt.md` |
| **禁止** | 具体书目列表 |

---

## 6. Concept explanation

| 项 | 内容 |
| --- | --- |
| **文件** | `03b_concept_explanation_prompt.md` |
| **Galison** | I-02 三层区分 |

---

## 7. Argument design

| 项 | 内容 |
| --- | --- |
| **文件** | `04b_argument_design_prompt.md` |
| **关键** | 只给选项；你写 `core_argument_paragraph.md` |

---

## 8. Outline

| 项 | 内容 |
| --- | --- |
| **文件** | `04_outline_prompt.md` |
| **变体** | Technical → 加 Fig/Table 计划 |

---

## 9. Draft review (strict marker)

| 项 | 内容 |
| --- | --- |
| **文件** | `05_draft_review_prompt.md` |
| **Galison** | I-05 表格式最有效 |

---

## 10. Counterargument

| 项 | 内容 |
| --- | --- |
| **文件** | `05b_counterargument_prompt.md` |

---

## 10b. Distinction red team

| 项 | 内容 |
| --- | --- |
| **文件** | `15_distinction_red_team_prompt.md` |
| **场景** | Target = Distinction；初稿/大纲后 |
| **输出** | 6 条 Merit 封顶弱点 + 须在正文回应 ≥3 |
| **风险** | 与 `05` 混为一轮 → 结构问题修不好 |

---

## 11. Reference hallucination risk

| 项 | 内容 |
| --- | --- |
| **文件** | `06_reference_risk_prompt.md` |

---

## 12. Final submission readiness

| 项 | 内容 |
| --- | --- |
| **文件** | `07_final_check_prompt.md` |
| **Galison** | 检出 Index Terms、Abstract 缩略语 |

---

## 13. AI declaration drafting

| 项 | 内容 |
| --- | --- |
| **文件** | `12_ai_declaration_drafting_prompt.md` |
| **你** | 必须改写到真实 |

---

## 14. Cursor bootstrap

| 项 | 内容 |
| --- | --- |
| **文件** | `08_cursor_project_bootstrap_prompt.md` |
| **Galison** | 等效 CURSOR_PROMPTS + 目录搭建 |

---

## 15. Cursor formatting

| 项 | 内容 |
| --- | --- |
| **文件** | `13_cursor_formatting_prompt.md` |

---

## 16. Post-task review

| 项 | 内容 |
| --- | --- |
| **文件** | `14_post_task_review_prompt.md` |

---

## ChatGPT session opener（每次新会话）

见 `00_chatgpt_session_opener.md` — 含 Mode 与合规约束。

---

## 维护规则

- 某 prompt 连续两门课无用 → 标 `deprecated` 移入 `04_Prompt_Library/archive/`  
- 有效新 prompt → 加编号文件 + 更新本索引  
- **勿**鼓励「一次 prompt 写全文」
