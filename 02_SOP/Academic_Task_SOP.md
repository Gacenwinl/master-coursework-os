# Academic Task SOP（Coursework 可复用标准流程）

> **Master_Coursework_OS** 核心 SOP。提炼自 Galison_Assignment 实证；适用于英国 master coursework 通用骨架，具体 rubric 以每门课 brief 为准。项目文件夹结构见 `05_Project_Template/`。

---

## 0. 启动前（30–60 分钟）

| 步骤 | 动作 | 产出物 |
| --- | --- | --- |
| 0.1 | 下载/保存 **官方 brief**（PDF/HTML/VLE） | `00_input/official/` |
| 0.2 | 标出 **交付物清单**（几个文件、格式、字数、占比） | `RUBRIC_MAPPING.md` 初表 |
| 0.3 | 标 **deadline 反推**（终检 15%、AI 记录 20%、初稿 40%、文献 25%） | `TASK_BOARD.md` |
| 0.4 | 定 **单一真相源**（md 或 tex，二选一） | README 写明 |
| 0.5 | 建文件夹：`input / control / logs / notes / refs / draft / final / review_assets` | 同本项目结构 |

**禁止**：未读 brief 就让 AI「写一篇高分 essay」。

---

## 1. 读题与 Rubric 拆解

| 步骤 | 人工 | AI 可做 |
| --- | --- | --- |
| 1.1 | 通读 brief 全文一遍 | 把 brief 转成检查表（**必须**标「未能确认」项） |
| 1.2 | 划出 **硬性指标**（字数、格式、引用数、必含章节） | 按章节映射到「证据文件」列 |
| 1.3 | 划出 **软性指标**（批判性、原创性、反思深度） | 给出「高分 vs 及格」行为差异 |
| 1.4 | 识别 **学术诚信条款**（AI 披露、文献零容忍） | 列出禁止 AI 代劳项 |
| 1.5 | 写 **中心研究问题** 一句话（自己写） | 仅评价是否可回答、是否过宽 |

**产出**：`RUBRIC_MAPPING.md`（要求 | 完成方式 | 证据位置 | 状态）。

**本项目范例**：议题三 + IEEE 6–8 页 + 21 文献 + 8 条 AI 交互 → `01_project_control/RUBRIC_MAPPING.md`。

---

## 2. 文献检索与核查

| 步骤 | 动作 | 工具 |
| --- | --- | --- |
| 2.1 | 按 **文献类型配额** 列清单（专著/期刊/会议/报告） | `literature_candidates.md` |
| 2.2 | 数据库检索（IEEE Xplore、出版社、Google Scholar） | **人工** |
| 2.3 | 每条写入核查表，状态 `Candidate Only` | `REFERENCE_VERIFICATION.md` |
| 2.4 | AI 仅允许：分类建议、检索关键词、**相关性判断** | 禁止输出完整书目 |
| 2.5 | 人工 Verified 后入 `refs.bib` / EndNote | 生成 citekey |
| 2.6 | 正文写作只用已 Verified 的 key | `CITATION_MAP.md` 可选 |

**状态机**：`Candidate → In refs.bib → Verified → Cited in draft`。

**本项目**：21 条；Colinge/ITRS citekey 与年份不一致时用「改字段不改 key」策略。

---

## 3. AI 辅助使用（嵌入全流程）

见 `AI_Workflow_For_Master.md`。此处只列 SOP 插入点：

| 阶段 | 允许 | 禁止 |
| --- | --- | --- |
| 规划 | rubric 拆解、时间预算 | 代写结论 |
| 理论 | 概念对照、误用清单 | 编造页码/引文 |
| 案例 | red team、文献**类型**建议 | 生成假文献 |
| 大纲 | 结构、篇幅分配 | 整篇正文 |
| 审稿 | 问题—建议表 | 整篇重写 |
| 排版 | LaTeX 语法、模板 | 改论点 |

**日志**：每轮 meaningful 交互 → `02_ai_logs/I-xx.md`（或未来课程的 reflective log）。

---

## 4. 初稿写作

| 步骤 | 说明 |
| --- | --- |
| 4.1 | 先 **大纲**（节标题 + 每节 2–3 句论点 + 文献类型） |
| 4.2 | 先写 **理论框架节**（有原著则先锚定直接引） |
| 4.3 | 再写 **案例分析节**（每节一个主案例，避免百科） |
| 4.4 | 再写 Discussion（边界、局限、反例） |
| 4.5 | 最后 Introduction / Conclusion（避免重复正文） |
| 4.6 | Abstract / Keywords **在全文稳定后**再写（防缩略语不一致） |

**语言**：英国课程若为英文，可用 AI 润色 **你已写好的段落**，而非从零生成。

---

## 5. 批判性 Review

| 轮次 | 审查者 | 输入 | 输出 |
| --- | --- | --- | --- |
| R1 自检 | 自己 | rubric 表 | 勾选缺口 |
| R2 AI 严师 | ChatGPT | 初稿 + brief | 问题—严重程度—建议表 |
| R3 同伴/导师 | 人 | 可选 | 意见摘录 |
| R4 格式审 | Cursor / 脚本 | PDF + brief | 页码、图表、引用 |

**规则**：AI 审稿 **不得** 整篇重写；只输出可执行修改项。

**本项目**：I-05 表 → 修 G2、补 Table I/Fig.1、扩文献至 21。

---

## 6. 引用与参考文献管理

| 步骤 | 动作 |
| --- | --- |
| 6.1 | 统一引用样式（IEEE / Harvard / APA）以 brief 为准 |
| 6.2 | 文中 `\cite{}` / 脚注与 bib 同步 |
| 6.3 | 直接引：作者 PDF **逐字** + 页码 |
| 6.4 | 编译后检查 `[?]`、未定义引用 |
| 6.5 | 终检：Index Terms 字母序、Abstract 缩略语全称（若指南要求） |

---

## 7. 最终提交前 Checklist（通用）

复制到每门课 `SUBMISSION_CHECKLIST.md`：

- [ ] 交付物数量与命名符合 VLE 要求  
- [ ] 主文档页数/字数在区间内  
- [ ] 引用样式与参考文献条数达标  
- [ ] 直接引文已与原文核对  
- [ ] 图表 ≥ 要求数量且正文有引用  
- [ ] AI 披露/协作记录（若需要）已独立成文件、已签名  
- [ ] 作者姓名、学号、单位与注册系统一致  
- [ ] PDF 可打开、无 `[?]`、无乱码  
- [ ] 文件名无特殊字符导致上传失败  
- [ ] 已在 deadline 前留 2h buffer  

**本项目额外项**：双 PDF；Galison ≥3 直接引；AI 记录 ≥6000 汉字。

---

## 8. 按作业类型的调整

| 类型 | 调整重点 |
| --- | --- |
| **Essay**（无格式模板） | 弱化 LaTeX；强化论点链与文献批判；AI 记录可缩短 |
| **Report**（实验/项目） | 增加方法、结果、附录；图表与数据真实性人工负责 |
| **Reflective task** | 主文即第一人称反思；AI 用于结构建议，禁止虚构经历 |
| **Technical paper**（IEEE/ACM） | 强化 template、图表、引用；本 SOP 默认模式 |
| **双交付（文+AI log）** | Phase 6 与 Phase 4 **并行**，不要最后 1 天补 log |
| **开卷/闭卷考试** | **本 SOP 不适用** AI 辅助（除非课程明确允许） |

---

## 9. 时间预算参考（可缩放）

| 规模 | 总时长 | 文献 | 写作 | 格式 | 记录/反思 | 终检 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 短 essay 2–3k | 8–12h | 2h | 4h | 1h | 1h | 1h |
| 本项目中论文 | 25h | 4h | 6h | 3.5h | 5h | 2h |
| 硕士 dissertation 章 | 40–80h | 比例上调 | 比例上调 | 固定留 10% | 视校规 | 10% |

---

## 10. 与本项目的文件映射

| SOP 步骤 | 本项目文件 |
| --- | --- |
| Rubric | `01_project_control/RUBRIC_MAPPING.md` |
| 文献 | `04_references/REFERENCE_VERIFICATION.md` |
| 日志 | `02_ai_logs/I-01`–`I-08` |
| 初稿 | `05_paper/paper_draft.md` |
| 终稿 | `07_final/*.pdf`（已提交） |
| Prompt | `01_project_control/CURSOR_PROMPTS.md`、`99_Project_Review_Assets/Prompt_Library.md` |
