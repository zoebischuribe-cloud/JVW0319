# 如何上传文档到 GitHub

## 方法 1：通过 GitHub 网页上传（最简单）

### 步骤：

1. **打开你的仓库**
   ```
   https://github.com/jiangbo19860/0319JVW
   ```

2. **创建新文件夹**
   - 点击 "Add file" → "Create new file"
   - 在文件名输入框中输入：`epilepsy_research/README.md`
   - 复制下方内容粘贴

3. **上传文档文件**
   - 点击 "Add file" → "Upload files"
   - 选择以下文件：
     - `epilepsy_research/README.md`
     - `epilepsy_research/docs/01_research_proposal.md`
     - `epilepsy_research/docs/02_resources_dataset.md`
   - 点击 "Commit changes"

---

## 方法 2：使用 Git 命令行（需要认证）

### 配置 Git（首次使用）

```bash
# 配置用户信息
git config --global user.email "your-email@example.com"
git config --global user.name "Your Name"

# 配置 GitHub 认证（二选一）

# 选项 1：使用 Personal Access Token
git config --global credential.helper store
# 然后第一次 push 时会提示输入用户名和 token

# 选项 2：使用 SSH（推荐）
ssh-keygen -t ed25519 -C "your-email@example.com"
# 然后将 ~/.ssh/id_ed25519.pub 的内容添加到 GitHub Settings → SSH and GPG keys
```

### 上传步骤

```bash
# 1. 进入项目目录
cd /home/admin/openclaw/workspace/epilepsy_research

# 2. 添加远程仓库（如果还没添加）
git remote add origin https://github.com/jiangbo19860/0319JVW.git

# 3. 推送到 GitHub
git push -u origin main
```

---

## 方法 3：使用 GitHub Desktop（图形界面）

1. **下载 GitHub Desktop**
   ```
   https://desktop.github.com/
   ```

2. **克隆仓库**
   - File → Clone repository
   - 选择 jiangbo19860/0319JVW
   - 选择本地路径

3. **复制文件**
   - 将 `epilepsy_research` 文件夹复制到克隆的仓库中

4. **提交并推送**
   - 在 GitHub Desktop 中 commit
   - 点击 Push origin

---

## 方法 4：使用 VS Code

1. **打开仓库文件夹**
   - File → Open Folder
   - 选择你的仓库目录

2. **复制文件**
   - 将 `epilepsy_research` 文件夹复制到仓库中

3. **使用 Source Control**
   - 点击左侧 Source Control 图标
   - 输入 commit 信息
   - 点击 "Publish Branch"

---

## 文件位置

所有文件已准备好，位于：

```
/home/admin/openclaw/workspace/epilepsy_research/
├── README.md                    # 项目主页（4.7KB）
└── docs/
    ├── 01_research_proposal.md  # 研究计划书（36KB）
    └── 02_resources_dataset.md  # 资源清单（13KB）
```

压缩包位置：
```
/home/admin/openclaw/workspace/epilepsy_research.tar.gz (59KB)
```

---

## 推荐方法

**最简单**：方法 1（网页上传）
- 无需配置
- 直观可见
- 适合少量文件

**最专业**：方法 2（Git 命令行）
- 版本控制
- 易于更新
- 适合长期维护

---

## 上传后验证

上传完成后，访问：
```
https://github.com/jiangbo19860/0319JVW/tree/main/epilepsy_research
```

应该能看到：
- ✅ README.md
- ✅ docs/01_research_proposal.md
- ✅ docs/02_resources_dataset.md

---

## 下载文档

上传后，其他人可以通过以下方式下载：

### 下载单个文件
- 点击文件 → 右上角 "Raw" → 右键保存

### 下载整个文件夹
```bash
# 使用 git clone
git clone https://github.com/jiangbo19860/0319JVW.git

# 或使用 GitHub 的 Download ZIP
# 仓库主页 → Code → Download ZIP
```

---

## 需要帮助？

如果遇到任何问题，请告诉我！
