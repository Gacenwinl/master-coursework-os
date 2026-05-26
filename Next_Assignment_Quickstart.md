# 下次作业 10 分钟启动指南

**Cursor**：克隆本仓库后自带 `.cursor/rules/`；`create_coursework_project.py` 也会复制到新建作业文件夹。Agent 见 `AGENTS.md`。

## 1. 复制模板

```powershell
cd Master_Coursework_OS
python create_coursework_project.py
# 或复制 05_Project_Template/ → YYYY_Module_AssignmentName/
```

## 2. 填写

- `01_Brief/Assignment_Intake_Form.md`  
- `01_Brief/Module0_AI_Policy_Gate.md` → 选 **Mode B**（除非 brief 另有规定）  
- 把 brief PDF 放入 `01_Brief/`

## 3. 先问自己 5 问（不用 AI）

1. 这门课 AI 允许到什么程度？  
2. 截止日期与时区？  
3. 到底交几个文件？  
4. 这道题要我 **prove** 什么？  
5. 哪些材料**不能**上传公共 AI？

## 4. 亲手写 1 句

`02_Notes/core_argument_paragraph.md` → *This assignment is asking me to…*

## 5. Cursor 第一条

复制：`04_Prompt_Library/08_cursor_project_bootstrap_prompt.md`

## 6. ChatGPT 第一条

复制：`04_Prompt_Library/00_chatgpt_session_opener.md` → 再贴 Intake + Module0 结论

## 7. 长期保留（每项目）

| 保留 |
| --- |
| `01_Brief/*` |
| `03_Literature/refs.bib` + 核查表 |
| `04_Draft/` 最终版源文件 |
| `06_Final/*.pdf` |
| `05_AI_Log/`（若 Mode B/C） |
| `99_Review/postmortem.md`（可选） |

## 8. 提交前 10 项

1. Module0 Mode 与 handbook 一致  
2. 能口头回答论点 + 3 篇文献  
3. Rubric 表主要行 ✓  
4. 字数/页数在范围内  
5. 引用样式统一；无 `[?]`  
6. 无占位符 / 教师批注残留  
7. AI declaration（若需要）已签  
8. 文件名符合 VLE  
9. PDF 能打开  
10. 提交成功截图（可选）

**主 SOP**：`02_SOP/Master_Coursework_SOP_2.0.md`
