# 癫痫与免疫：多模态深度学习研究

## 项目文档索引

**创建日期**: 2026-03-19  
**研究方向**: 癫痫神经免疫学 + 多模态深度学习  
**目标期刊**: *Brain* (IF≈15) / *Epilepsia* (IF≈6) / *Nature Communications* (IF≈17)

---

## 📂 文档列表

### 核心文档

| 编号 | 文档 | 内容 | 大小 |
|------|------|------|------|
| **01** | [研究计划书](01_research_proposal.md) | 完整研究方案、方法、时间计划 | 36KB |
| **02** | [资源与数据集](02_resources_dataset.md) | 公开数据集、开源代码、文献清单 | 13KB |
| **03** | 数据预处理指南 | EEG 数据处理流程、代码示例 | 待创建 |
| **04** | 模型实现代码 | 多模态深度学习架构、训练脚本 | 待创建 |
| **05** | 实验结果 | 模型性能、图表、分析 | 待创建 |
| **06** | 论文初稿 | 完整论文草稿 | 待创建 |

---

## 🎯 项目概述

### 研究背景

- **癫痫**：影响全球 5000 万人，第四常见神经系统疾病
- **神经炎症假说**：炎症与癫痫发作双向关联
- **研究空白**：缺乏多模态深度学习整合研究

### 研究目标

1. **开发多模态深度学习模型** - 整合 EEG + 炎症标志物 + 临床数据
2. **识别癫痫免疫亚型** - 发现炎症介导的癫痫表型
3. **构建发作预测系统** - 提前预警癫痫发作
4. **发现新型生物标志物** - 用于诊断和预后评估

### 创新点

✅ 首个癫痫神经免疫多模态深度学习框架  
✅ 整合脑电生理 + 免疫学 + 临床表型  
✅ 可解释性 AI：发现新的免疫 - 癫痫关联  
✅ 开源工具包：推动领域发展

---

## 📊 可用数据集

| 数据集 | 类型 | 样本量 | 获取方式 | 状态 |
|--------|------|--------|----------|------|
| **CHB-MIT** | EEG | 664 记录 | PhysioNet | ✅ 可下载 |
| **Bonn** | EEG | 500 记录 | 直接下载 | ✅ 可下载 |
| **TUH EEG** | EEG | 30k+ 记录 | 申请 | ⏳ 需审批 |
| **OpenSeizureDB** | 多模态 | 10k+ 记录 | GitHub | ✅ 可下载 |
| **NHANES** | 临床 + 炎症 | 10k+/轮 | CDC | ✅ 可下载 |
| **MIMIC-IV** | 重症监护 | 40k+ 患者 | PhysioNet | ⏳ 需培训 |

---

## 💻 开源代码

| 项目 | Stars | 用途 | 推荐度 |
|------|-------|------|--------|
| **Epileptic-Seizure-Detection** | 65⭐ | ChronoNet + 小波 | ⭐⭐⭐⭐⭐ |
| **CHB-MIT-preprocessing** | 54⭐ | 数据预处理 | ⭐⭐⭐⭐⭐ |
| **epilepsy2bids** | 18⭐ | BIDS 标准化 | ⭐⭐⭐⭐ |
| **Non-EEG_Seizure_Detection** | 7⭐ | 多模态融合 | ⭐⭐⭐⭐ |
| **BEST Toolbox** | - | iEEG 工具 | ⭐⭐⭐⭐⭐ |

---

## ⏱️ 时间计划

### 14 周详细计划

| 阶段 | 周数 | 核心任务 | 交付物 |
|------|------|----------|--------|
| **准备** | 1-2 | 文献调研、数据申请、环境配置 | 文献库、数据集 |
| **数据** | 3-4 | 数据下载、预处理、质控 | 预处理后数据 |
| **基线** | 5-6 | 单模态模型、基线性能 | 基线代码 + 结果 |
| **多模态** | 7-9 | 融合模型开发、训练 | 多模态模型 |
| **优化** | 10-11 | 超参数调优、交叉验证 | 优化后模型 |
| **验证** | 12 | 外部验证、亚组分析 | 验证结果 |
| **解释** | 13 | 特征分析、生物学解释 | SHAP 分析、通路富集 |
| **写作** | 14 | 论文撰写、图表制作 | 论文初稿 |

---

## 🚀 快速开始

### 环境配置（10 分钟）

```bash
# 创建虚拟环境
python -m venv epilepsy_env
source epilepsy_env/bin/activate  # Linux/Mac

# 安装核心依赖
pip install torch torchvision torchaudio
pip install mne pyedflib eegnb
pip install scikit-learn scipy numpy
pip install matplotlib seaborn plotly
pip install tqdm wandb pywt
```

### 下载数据（30 分钟）

```bash
# 1. Bonn 数据集（最快）
wget http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3&changelang=3 -O bonn_eeg.zip
unzip bonn_eeg.zip

# 2. CHB-MIT 数据集
# 访问：https://physionet.org/content/chbmit/1.0.0/
# 需要注册免费账号

# 3. 克隆开源代码
git clone https://github.com/tothemoon10080/CHB-MIT-data-preprocessing-and-prediction.git
git clone https://github.com/Sharad24/Epileptic-Seizure-Detection.git
```

### 运行基线（1 小时）

```bash
# 使用 Bonn 数据集
cd Epileptic-Seizure-Detection
jupyter notebook

# 或使用预处理代码
cd CHB-MIT-data-preprocessing-and-prediction
pip install -r requirements.txt
python train.py
```

---

## 📚 关键文献

### 必读综述（5 篇）

1. **Vezzani A, et al.** Brain inflammation as a biomarker in epilepsy. *Biomark Med*. 2011.
2. **Rana A, Musto AE.** The role of inflammation in the development of epilepsy. *J Neuroinflammation*. 2018.
3. **Steriade C, et al.** Acute symptomatic seizures secondary to autoimmune encephalitis. *Epilepsia*. 2020.
4. **Mazarati AM, et al.** Neurobehavioral comorbidities of epilepsy: Role of inflammation. *Epilepsia*. 2017.
5. **Tsiouris KM, et al.** A Long Short-Term Memory Deep Learning Network for EEG-Based Epileptic Seizure Prediction. *IEEE Trans Biomed Eng*. 2018.

### 最新预印本（2025-2026）

- **ConvMambaNet** (2026-01) - CNN + Mamba 状态空间模型
- **PaperNet** (2025-12) - 时间卷积 + 通道注意力
- **Geometric-Stochastic Multimodal** (2025-12) - 多模态深度学习
- **DistilCLIP-EEG** (2025-10) - 多模态学习 + 知识蒸馏
- **Mentality** (2025-09) - Mamba 基础模型

---

## 📞 项目状态

| 任务 | 状态 | 完成度 |
|------|------|--------|
| 文献调研 | ✅ 完成 | 100% |
| 资源整理 | ✅ 完成 | 100% |
| 研究计划书 | ✅ 完成 | 100% |
| 数据下载 | ⏳ 进行中 | 0% |
| 环境配置 | ⏳ 待开始 | 0% |
| 模型实现 | ⏳ 待开始 | 0% |
| 实验运行 | ⏳ 待开始 | 0% |
| 论文写作 | ⏳ 待开始 | 0% |

---

## 📝 更新日志

| 日期 | 更新内容 | 文档 |
|------|----------|------|
| 2026-03-19 | 创建项目仓库 | README.md |
| 2026-03-19 | 完成研究计划书 | 01_research_proposal.md |
| 2026-03-19 | 完成资源清单 | 02_resources_dataset.md |
| 待更新 | 数据预处理指南 | 03_data_preprocessing.md |
| 待更新 | 模型代码 | 04_model_implementation.md |
| 待更新 | 实验结果 | 05_results.md |
| 待更新 | 论文初稿 | 06_manuscript.md |

---

## 🎯 下一步行动

1. **下载数据集** - CHB-MIT 和 Bonn
2. **配置环境** - 安装所有依赖
3. **运行基线** - 复现开源代码结果
4. **开始实验** - 实现多模态模型

---

## 📧 联系与协作

**GitHub 仓库**: https://github.com/jiangbo19860/0319JVW

**问题反馈**: 请在 GitHub Issues 中提出

**协作欢迎**: 欢迎任何形式的贡献（代码、数据、文档）

---

**最后更新**: 2026-03-19  
**项目状态**: 🟡 准备阶段

---

> **所有文档已整理完毕，可以通过 GitHub 下载！**
