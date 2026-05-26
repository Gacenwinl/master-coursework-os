# 上传到 GitHub（一次性）

**只推送 `Master_Coursework_OS/` 这一层**，不要把整个 `马彦朝论文` 或 `Galison_Assignment/` 推上去（含已交作业与个人路径）。

## 1. 在本机初始化（PowerShell）

```powershell
cd "c:\Users\13555\SynologyDrive\260525-马彦朝论文\Master_Coursework_OS"
git init
git add .
git status
git commit -m "Initial commit: Master Coursework OS SOP 2.0 template"
```

## 2. 在 GitHub 建空仓库

- 名称建议：`master-coursework-os`（或你喜欢的英文名）
- **不要**勾选 “Add a README” / license（本地已有）
- 可见性：**Private** 推荐（含你的 Prompt 与工作流；若公开需自行删去任何个人信息）

## 3. 推送

```powershell
git branch -M main
git remote add origin https://github.com/Gacenwinl/master-coursework-os.git
git push -u origin main
```

若已安装 GitHub CLI：

```powershell
gh repo create master-coursework-os --private --source=. --remote=origin --push
```

## 4. 设为 Template（可选但推荐）

GitHub 仓库 → **Settings** → **General** → **Template repository** ✓

之后新课程：**Use this template** → 得到独立仓库，再 `git clone` 到本地。

---

## 以后每次新作业（两种用法）

### A. Template 新仓库（作业与 OS 分开，推荐）

1. GitHub：**Use this template** → 例如 `2026_MODULE_Essay1`
2. `git clone` 该作业仓库到本地
3. 在克隆根目录运行 `python create_coursework_project.py`  
   或在模板仓库里直接填 `05_Project_Template/` 结构（二选一）

### B. 只 clone OS，作业文件夹本地生成（最简单）

```powershell
git clone https://github.com/Gacenwinl/master-coursework-os.git coursework-os
cd coursework-os
python create_coursework_project.py
# 生成 2026_MODULE_AssignmentName/ 子文件夹
```

用 Cursor **打开生成的作业文件夹**；`.cursor/rules` 已由脚本复制进去。

---

## 与 Synology 工作区的关系

| 位置 | 用途 |
| --- | --- |
| Synology `马彦朝论文/` | 个人全集（含 Galison 归档） |
| GitHub `master-coursework-os` | 可复用模板，无已交论文 |

两边可并存：模板在 GitHub 更新后，`git pull` 同步；Galison 留在 Synology 即可。
