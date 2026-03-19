# ⚙️ 项目配置与永久要求

**创建时间**: 2026-03-19 09:37  
**最后更新**: 2026-03-19 09:37  
**优先级**: 🔴 最高优先级（必须遵守）

---

## 🎯 核心要求（必须遵守）

### 1. GitHub 仓库配置

**主仓库**：
```
URL: https://github.com/zoebischuribe-cloud/JVW0319
分支：main
认证：已配置（通过 Git credential 或环境变量）
```

**要求**：
- ✅ **所有生成的文档必须上传到此仓库**
- ✅ **同时发送给用户一份**
- ✅ **创建下载链接**

---

## 📁 仓库结构

```
JVW0319/
├── epilepsy_research/          # 癫痫研究项目
│   ├── README.md
│   ├── docs/                   # 文档
│   │   ├── 01_research_proposal.md
│   │   ├── 02_resources_dataset.md
│   │   └── 03_upload_guide.md
│   └── code/                   # 代码
│       ├── 01_download_bonn.py
│       ├── 02_preprocess_data.py
│       ├── 03_train_model.py
│       └── requirements.txt
├── future_projects/            # 未来项目（预留）
└── CONFIG_AND_REQUIREMENTS.md  # 本文档
```

---

## 🔐 认证配置

**Git 用户配置**：
```bash
git config user.email "jiangbo19860@users.noreply.github.com"
git config user.name "jiangbo19860"
```

**认证方式**：
- Personal Access Token（已配置）
- 通过 Git credential 存储
- 或环境变量 `GITHUB_TOKEN`

**重要**：Token 不直接写在文档中，通过安全方式存储和使用

---

## 📋 上传流程（标准操作）

### 自动生成文档后：

1. **保存到本地**
   ```bash
   /home/admin/openclaw/workspace/[项目名]/
   ```

2. **初始化 Git（如需要）**
   ```bash
   cd /home/admin/openclaw/workspace/[项目名]
   git init
   git config user.email "jiangbo19860@users.noreply.github.com"
   git config user.name "jiangbo19860"
   git add -A
   git commit -m "feat: [项目描述]"
   git branch -M main
   ```

3. **配置远程仓库**
   ```bash
   git remote add origin https://github.com/zoebischuribe-cloud/JVW0319.git
   ```

4. **推送到 GitHub**
   ```bash
   git push -u origin main
   # 认证通过 credential 或环境变量自动处理
   ```

5. **通知用户**
   - 发送下载链接
   - 确认上传成功

---

## 🚨 重要提醒

### 必须做到的事项：

1. **所有文档必须上传** 🔴
   - 研究计划书
   - 代码
   - 数据
   - 结果
   - 论文草稿

2. **同时发送给用户** 🟡
   - 通过对话发送
   - 提供下载链接

3. **使用正确的仓库** 🔴
   - ✅ `zoebischuribe-cloud/JVW0319`
   - ❌ 不要使用其他仓库

4. **保持文档更新** 🟡
   - 每次生成新内容后更新
   - 维护文件索引

5. **保护敏感信息** 🔴
   - 不将 Token 写入文档
   - 使用 credential 或环境变量
   - 遵守 GitHub 安全规则

---

## 📂 当前项目列表

### 1. 癫痫与免疫多模态深度学习研究

**状态**: ✅ 已上传  
**位置**: `epilepsy_research/`  
**文件数**: 13  
**总大小**: ~80KB

**核心文档**：
- `docs/01_research_proposal.md` (35KB) - 研究计划书
- `docs/02_resources_dataset.md` (19KB) - 资源清单
- `code/03_train_model.py` (8.6KB) - CNN-LSTM 模型

---

## 🔧 快速命令参考

### 上传新文档
```bash
cd /path/to/new/project
git init
git config user.email "jiangbo19860@users.noreply.github.com"
git config user.name "jiangbo19860"
git add -A
git commit -m "feat: 添加新项目"
git branch -M main
git remote add origin https://github.com/zoebischuribe-cloud/JVW0319.git
git push -u origin main
```

### 更新现有文档
```bash
cd /path/to/existing/project
git add -A
git commit -m "docs: 更新文档"
git push origin main
```

### 检查状态
```bash
git status
git log --oneline
git remote -v
```

---

## 📞 故障排查

### 问题 1: 推送失败
```bash
# 解决方案
git pull origin main --allow-unrelated-histories
git push origin main
```

### 问题 2: 认证失败
```bash
# 检查 Token 是否有效
# 重新配置远程仓库
git remote remove origin
git remote add origin https://github.com/zoebischuribe-cloud/JVW0319.git
```

### 问题 3: 分支冲突
```bash
# 强制推送（谨慎使用）
git push origin main --force
```

### 问题 4: GitHub 安全检测
```bash
# 如果包含敏感信息（如 Token），推送会被拒绝
# 解决方案：
# 1. 从文档中移除敏感信息
# 2. 使用 git filter-branch 或 BFG 清理历史
# 3. 重新推送
```

---

## 📝 检查清单

### 每次生成内容后：

- [ ] 文档已保存到本地
- [ ] Git 已初始化
- [ ] 文件已 add 和 commit
- [ ] 远程仓库已配置
- [ ] 已推送到 GitHub
- [ ] 已通知用户
- [ ] 下载链接已提供
- [ ] 文档中无敏感信息（Token、密码等）

---

## 🎯 未来扩展

### 新项目创建流程：

1. 创建项目文件夹
2. 编写项目文档
3. 实现代码
4. 上传到 GitHub（子文件夹）
5. 更新本文档

### 自动化脚本（待创建）：

```bash
#!/bin/bash
# auto_upload.sh
# 自动上传新项目的脚本
```

---

## 🔒 安全最佳实践

1. **永远不要**在文档中明文存储 Token
2. **始终使用** Git credential 或环境变量
3. **定期检查**文档中是否有敏感信息
4. **遵守** GitHub 的 Secret Scanning 规则

---

**最后更新**: 2026-03-19 09:37  
**下次检查**: 每次生成新内容时  
**维护者**: OpenClaw Agent

---

> ⚠️ **切记：所有数据必须上传到 zoebischuribe-cloud/JVW0319 仓库！**  
> 🔒 **切记：不要将 Token 等敏感信息写入文档！**
