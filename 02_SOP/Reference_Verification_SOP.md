# Reference Verification SOP

> 目标：**零 AI 虚构文献**。适用于 essay / report / technical paper。

---

## 状态机

```
Candidate → In_Bib → Verified → Cited_in_Draft
                ↘ Remove
```

| 状态 | 含义 | 能否 `\cite` / 正文引用 |
| --- | --- | --- |
| **Candidate** | 待查，仅标题/作者猜测 | 否 |
| **In_Bib** | 已入 .bib / 参考文献表，字段未终检 | 否（或标 TODO） |
| **Verified** | 人工核对 DOI/出版社/卷期页 | 是 |
| **Remove** | 剔除 | 否 |

---

## 流程（每门课重复）

| 步 | 动作 | 工具 |
| ---: | --- | --- |
| 1 | AI 只输出：**关键词 + 数据库 + 文献类型配额** | Prompt `03_literature_planning` |
| 2 | 你在 IEEE Xplore / Google Scholar / 图书馆检索 | 人工 |
| 3 | 每条写入 `literature_table` / `reference_verification_table` | csv 或 md |
| 4 | 核对至少 2 个来源（出版社页 + DOI） | 人工 |
| 5 | Verified 后写入 `refs.bib` 或 Word 参考文献 | Cursor 可协助格式 |
| 6 | 正文只引用 Verified | `CITATION_MAP` 可选 |
| 7 | 编译/排版后检查 `[?]`、未定义引用 | Cursor |

---

## AI 禁止项

- 输出完整参考书目列表当作「已存在」  
- 编造 DOI、卷期页、页码  
- 把综述里的二手引用当一手  

---

## 直接引文（原著 / 一手）

| 类型 | 要求 |
| --- | --- |
| 书名/论文直接引 | 打开 PDF **逐字**核对 + 页码 |
| 引文措辞 | AI paraphrase ≠ direct quote |
| 课堂读本 | 以 module 指定版本为准 |

---

## citekey 策略

若发现年份/作者错误但正文已大量 `\cite{oldkey}`：

- **优先**：改 bib 字段，**保留 citekey**  
- **其次**：全局替换 citekey（仅在你确认无遗漏时）

---

## 终检抽样

- [ ] 每条参考文献至少核对过题名 + 年份 + 来源  
- [ ] 正文每个关键事实句有可对应引用  
- [ ] 无「待查」条目仍被引用  
- [ ] AI 未声称「已帮你核实文献」

---

## 模板文件

`03_Templates/reference_verification_table.csv`  
`03_Templates/literature_table.csv`
