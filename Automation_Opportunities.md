# Automation Opportunities（Cursor / 脚本）

**约束**：提高效率 ≠ 外包学术责任（见 `SOP_Diagnosis.md` §2.5）。

---

## 6.1 可立即自动化

| 任务 | 实现 | Galison 证据 |
| --- | --- | --- |
| 创建项目目录 | `create_coursework_project.py` | 已做 |
| 复制 Intake / Module0 / 模板 | 同上 | 已做 |
| 生成空 rubric / task_plan / checklist | bootstrap prompt + 脚本 | CURSOR 可生成骨架 |
| 初始化 README | 脚本 patch 模块名 | 已做 |
| md → tex 同步 | `md_to_body.py` | compile.ps1 调用；**注意覆盖** |
| LaTeX 编译 | `compile.ps1` | TEMP 目录防 Synology 截断 |
| PDF 验证 | `validate_pdf.py` | 页数、引用 |
| AI log 空表 | 复制 csv/md | — |
| pandoc → docx（AI 记录） | `export_ai_record.ps1` | Galison Phase 6 |
| 批量更新路径引用 | Cursor 搜索替换 | 目录整理时 |

**已实现**：`tools/verify_bib_keys.py` — 检查 `\cite{}` 是否存在于 `refs.bib`（stdlib）。

---

## 6.2 不应完全自动化

| 任务 | 原因 |
| --- | --- |
| 中心论点选择 | Independent thinking |
| 文献是否存在/准确 | Hallucination 风险 |
| 直接引文逐字 | Integrity |
| AI declaration 比例 | 诚信 |
| 是否提交 | 责任 |
| Module AI policy 解释 | 需 handbook 权威 |
| 合并 ChatGPT 导出为「交互记录」 | 易造假 |

---

## 6.3 半自动（AI 起草 + 你改）

| 任务 | 模式 |
| --- | --- |
| Rubric 表 | B 生成 → 你删行 |
| Task plan | B 生成 → 你改日期 |
| Outline | B 生成 → 你改论点 |
| Declaration | B 草稿 → 你重写 |
| Critique 表 | B 生成 → 你选 fix |

---

## 6.4 `create_coursework_project.py`（已有）

- **无外部依赖**  
- **不生成** 作业正文  
- 2.0 建议增加：`reading_notes_template.md` 复制（待下一版脚本小改）

---

## 6.5 Cursor 专属工作流

| 触发 | 动作 |
| --- | --- |
| 每日打开项目 | 读 `task_plan.md` 下一项（可扩展 daily prompt） |
| ChatGPT 输出返回 | `02_ai_logs` 归档 prompt（来自 Galison CURSOR_PROMPTS §2） |
| 编译失败 | `13_cursor_formatting_prompt` 仅修语法 |

**未能从项目文件确认**：是否实现 automated git commit；建议 **不自动 commit** 以免误交草稿。
