# AI Workflow for UK Master（安全、高效、合规）

> **Master_Coursework_OS** 核心 SOP。基于 Galison_Assignment 实证；英国各校 AI policy 不同，**每门课以 module handbook 为准**。本文不构成任何学校的官方政策解释。  
> **英硕必读前置**：`Module0_AI_Policy_Gate.md`、`UK_Compliance_and_Modes.md`。

**核心原则**：

> AI may support my process, but the brief interpretation, core argument, source verification, final judgement, and academic responsibility must remain mine.

---

## 0. 英硕与 Galison 课程作业的区别

| | Galison 南邮（Mode C） | 英硕默认（Mode B） |
| --- | --- | --- |
| AI 记录 | 常占高分、长文 | 可能只需短 declaration |
| 上传材料 | 可对照指南 PDF | 慎上传全文 slides / 保密数据 |
| AI 角色 | 规划+草稿+记录 | **critique > ghostwrite** |
| 第一步 | 拆 rubric | **先查 AI policy** |

---

## 1. AI 适合做什么

| 类别 | 示例（本项目已验证） |
| --- | --- |
| **Brief 结构化** | 把 PDF 要求拆成检查表、识别双交付 |
| **概念地图** | instrumental continuity / intercalated periodization 三层区分 |
| **Risk review** | 案例是否会被批为类比过度、设备百科 |
| **大纲与篇幅** | 6–8 页双栏节分配、图表插入点 |
| **批判清单** | 「问题—严重程度—修改建议」审稿表 |
| **语言润色** | 在你已有英文段落上改语法（非代写论点） |
| **格式劳动** | LaTeX 骨架、BibTeX 挂载、编译错误 |
| **终检辅助** | 对照已上传 brief + 你的 PDF 查 Index Terms、章节 |
| **反思脚手架** | AI log 的 (d)(f) 段提问清单 |

---

## 2. AI 不应该做什么

| 禁止项 | 本项目教训 |
| --- | --- |
| 生成完整参考文献 | 课程零容忍；本项目 Phase 3 起禁止 |
| 编造页码、引文、DOI | ChatGPT 曾拒绝填 G1–G4，正确行为 |
| 一次性生成终稿 | 评分看批判性使用，非篇幅 |
| 替你做结论与价值判断 | 诚信声明比例须诚实 |
| 声称「已核实文献/原著」 | I-07：AI 只能查版式，不能背书 |
| 伪造 AI 交互记录 | 八条 log 须对应真实会话 |
| 闭卷考试答题 | 除非政策明确允许 |

---

## 3. 如何写 Prompt（通用公式）

```
[角色] + [任务] + [输入材料] + [硬约束] + [输出格式] + [禁止项]
```

**硬约束范例**（本项目反复使用）：

- 不要编造页码 / 参考文献  
- 不要写完整正文 / 不要整篇重写  
- 区分：原著含义 / 你的解释 / 迁移用法  

**输出格式范例**：

- 表格：问题 | 严重程度 | 建议 | 状态  
- 六段式：Context / Prompt / Output / Critical / Revision / Reflection  

---

## 4. 让 AI 做 Critique 而非代写

| 做法 | 反例 |
| --- | --- |
| 「请列出 10 个可被质疑的论点」 | 「请帮我写一篇 Discussion」 |
| 「用教师视角审稿，表格输出，不要重写」 | 「请优化全文使其满分」 |
| 「指出哪些句子像 AI 写作」 | 「请改成更学术的英文」 |
| 「对照 rubric 标不满足项」 | 「请直接改成满足 rubric 的版本」 |

**本项目 Prompt C（I-05）** 即标准 critique prompt → 见 `Prompt_Library.md`。

---

## 5. 避免 AI 幻觉文献

1. **流程**：AI 只给「文献类型 + 检索式」→ 你下载/核对 → 入表 → 入 bib。  
2. **表中状态**：未 Verified 禁止 `\cite{}`。  
3. **交叉验证**：至少两个来源（出版社页 + DOI）。  
4. **剔除**：领域不符条目（如 `boo2012ionimplant`）。  
5. **citekey 策略**：宁可保留旧 key 改字段，避免全文断链。  
6. **终检话术**：对 AI 说「不能声称已核实，只能标需作者核对」。

---

## 6. 如何保留 AI 使用记录

| 层级 | 做法 |
| --- | --- |
| **最低** | 截图 + 日期 + Prompt |
| **推荐** | 每轮导出 ChatGPT → `chatgpt_exports/` + `I-xx` 摘要 |
| **高分** | 独立 PDF：结构化 log + 诚信声明 + 签名 |
| **索引** | `AI_LOG_INDEX.md`、`CHATGPT_EXPORT_INDEX.md` |
| **分享链接** | 可选备查（课程若要求） |

**时间戳**：保留 `# you asked` / `message time`（本项目导出含）。

---

## 7. 如何写 AI Declaration

**英国常见要素**（具体以课程为准）：

1. 哪些工具（ChatGPT 版本、Cursor、翻译等）  
2. 用于哪些阶段（规划 / 草稿 / 润色 / 排版）  
3. **三类比例**（直接采用 / 修改后采用 / 仅启发）— 本项目 §4 范例  
4. 文献与核心论点由本人负责  
5. 记录真实、无编造交互  
6. 签名 + 日期  

**避免**：比例明显失真；声称「未用 AI」却交 AI log 课程。

**模板**：`Reusable_Templates.md` § AI declaration。

---

## 8. Academic Integrity 风险下的使用策略

| 风险 | 缓解 |
| --- | --- |
| 被指代写 | 保留修改痕迹；log 里写清 (e) Revision |
| 虚假文献 | 核查表 + 不用 AI 书目 |
| 虚假引文 | 原著 PDF 旁注 |
| 过度依赖 | Discussion 写你自己反对 AI 的论点 |
| 政策变动 | 每 module 第一周读 AI policy 一页纸 |
| 小组作业 | 披露范围须含组员共识（本项目为个人作业） |

**曼大 / 英国 master 一般原则**（未能从本项目文件确认曼大 2026 具体条文）：倾向 **透明披露 + 人类责任**；本项目的双 PDF 设计本身就是 **process grade** 训练。

---

## 9. 三工具分工（推荐默认）

| 工具 | 角色 |
| --- | --- |
| **ChatGPT** | 概念、结构、critique、英文草稿片段 |
| **Cursor** | 仓库、日志、LaTeX、合规表、脚本 |
| **你** | 原著、文献、论点、签名、提交 |

---

## 10. 本项目可复制的「安全句」

粘贴到每个新会话首条：

```text
这是英国/中国研究生课程作业。请遵守：
1. 不要编造参考文献、页码、DOI、引文原文；
2. 不要代写最终提交正文，只提供结构、critique、待我核实草稿；
3. 不确定处写「需作者人工核对」；
4. 输出表格化、可执行建议。
```
