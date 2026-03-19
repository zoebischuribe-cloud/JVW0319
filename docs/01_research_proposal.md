# 癫痫与免疫：多模态深度学习研究项目计划书

## 基于脑电图、炎症标志物与临床数据的智能诊断与预后预测

---

**版本**: 1.0  
**创建日期**: 2026-03-19  
**研究方向**: 癫痫神经免疫学 + 多模态深度学习  
**目标期刊**: *Brain* (IF≈15) / *Epilepsia* (IF≈6) / *Nature Communications* (IF≈17)

---

## 📋 执行摘要

### 研究背景

癫痫影响全球约 5000 万人，是第四常见的神经系统疾病。近年来，**神经炎症假说**已成为癫痫研究的重要方向：

- **炎症与癫痫发作**：双向关系（炎症可诱发癫痫，癫痫发作也可引起炎症）
- **炎症生物标志物**：IL-1β、IL-6、TNF-α、HMGB1 等在癫痫患者中升高
- **治疗靶点**：抗炎治疗可能成为新型抗癫痫策略

### 研究空白

| 现有研究局限 | 本研究解决方案 |
|-------------|---------------|
| 单一模态（仅 EEG 或仅生物标志物） | **多模态融合**：EEG + 炎症标志物 + 临床数据 |
| 传统统计方法 | **深度学习**：捕捉复杂非线性关系 |
| 小样本单中心 | **多中心数据**：公开数据集整合 |
| 缺乏早期预测 | **发作预测模型**：提前预警 |

### 研究目标

1. **开发多模态深度学习模型**整合脑电图、炎症标志物和临床数据
2. **识别癫痫免疫亚型**：发现炎症介导的癫痫表型
3. **构建发作预测系统**：提前预警癫痫发作
4. **发现新型生物标志物**：用于诊断和预后评估

### 创新点

✅ **首个癫痫神经免疫多模态深度学习框架**  
✅ **整合脑电生理 + 免疫学 + 临床表型**  
✅ **可解释性 AI**：发现新的免疫 - 癫痫关联  
✅ **开源工具包**：推动领域发展

---

## 🔬 科学背景与文献综述

### 癫痫神经免疫学

#### 关键发现

**炎症通路激活**：
- IL-1β/TLR4 信号通路促进癫痫发生
- HMGB1-RAGE 轴介导神经炎症
- 小胶质细胞激活导致血脑屏障破坏

**临床证据**（PubMed 检索：429 篇文献）：

| 研究 | 年份 | 期刊 | 关键发现 |
|------|------|------|----------|
| Vezzani et al. | 2011 | Biomark Med | 提出脑炎症作为癫痫生物标志物 |
| Rana & Musto | 2018 | J Neuroinflammation | 炎症调控异常导致癫痫发生 |
| Steriade et al. | 2020 | Epilepsia | 自身免疫性癫痫概念定义 |
| Mazarati et al. | 2017 | Epilepsia | 癫痫与自闭症/抑郁的炎症关联 |

#### 炎症标志物

**外周血标志物**：
- **细胞因子**：IL-1β、IL-6、TNF-α、IL-17
- **趋化因子**：CXCL8、CCL2
- **急性期蛋白**：CRP、SAA
- **损伤标志物**：HMGB1、S100B

**脑脊液标志物**：
- 神经元特异性烯醇化酶 (NSE)
- 髓鞘碱性蛋白 (MBP)
- 神经丝轻链 (NfL)

### 癫痫脑电图研究

#### 公开数据集

| 数据集 | 样本量 | 类型 | 获取方式 |
|--------|--------|------|----------|
| **CHB-MIT** | 23 患者 | 头皮 EEG | PhysioNet 公开 |
| **Bonn** | 500 记录 | 头皮 EEG | 公开下载 |
| **TUH EEG** | 30,000+ 记录 | 头皮 EEG | Temple University |
| **OpenSeizureDB** | 10,000+ 记录 | 多模态 | 公开 |

#### 深度学习应用

**卷积神经网络 (CNN)**：
- 自动提取 EEG 时空特征
- 发作检测准确率>90%

**循环神经网络 (RNN/LSTM)**：
- 捕捉时间依赖性
- 发作预测提前 5-30 分钟

**Transformer**：
- 注意力机制
- 长程依赖建模

---

## 📊 数据资源

### 脑电图数据集

#### 1. CHB-MIT Scalp EEG Database ⭐ 最常用

**基本信息**：
- **来源**：波士顿儿童医院
- **样本量**：23 例儿科癫痫患者
- **记录时长**：约 900 小时
- **通道数**：23-26 通道
- **采样率**：256 Hz

**数据内容**：
- 连续头皮脑电图记录
- 癫痫发作标注（开始/结束时间）
- 患者元数据（年龄、性别、发作类型）

**获取方式**：
```
链接：https://physionet.org/content/chbmit/
注册：PhysioNet 账号（免费）
伦理：无需额外审批
```

**预处理代码**（开源项目）：
```
GitHub: https://github.com/tothemoon10080/CHB-MIT-data-preprocessing-and-prediction
Stars: 54⭐
```

#### 2. Bonn EEG Dataset ⭐ 经典基准

**基本信息**：
- **样本量**：500 条单通道 EEG 记录
- **类别**：5 类（健康/发作间期/发作期）
- **时长**：每条 23.6 秒
- **采样率**：173.61 Hz

**获取方式**：
```
链接：http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3&changelang=3
直接下载，无需注册
```

**开源实现**：
```
GitHub: https://github.com/mamuncseru/EpilepsyDetectionWithCNNExperiment
Stars: 5⭐
方法：CNN + Bonn 数据集
```

#### 3. TUH EEG Corpus ⭐ 最大规模

**基本信息**：
- **样本量**：30,000+ 脑电图记录
- **来源**：Temple 大学医院
- **时间跨度**：2002-2016
- **标注**：癫痫发作、睡眠分期等

**获取方式**：
```
链接：https://isip.piconepress.com/projects/tuh_eeg/
需要签署数据使用协议
```

#### 4. OpenSeizureDetector Database

**基本信息**：
- **样本量**：10,000+ 记录
- **模态**：加速度 + 心率 + EEG（部分）
- **来源**：社区贡献的真实发作数据

**获取方式**：
```
GitHub: https://github.com/OpenSeizureDetector/OpenSeizureDatabase
最新更新：2026-03-15
```

### 炎症标志物数据集

#### 1. 公开临床数据集

**选项 1：NHANES**（推荐）
- **优势**：公开、大样本、多模态
- **可用数据**：
  - CRP（C 反应蛋白）
  - 白细胞计数及分类
  - 神经系统疾病史（包括癫痫）
  - 人口学、生活方式数据
- **样本量**：每轮约 10,000 人
- **链接**：https://www.cdc.gov/nchs/nhanes/

**选项 2：MIMIC-IV**
- **优势**：重症监护数据、详细实验室检查
- **可用数据**：
  - 炎症标志物（CRP、白细胞等）
  - 神经系统诊断（ICD 编码）
  - 生命体征、用药记录
- **样本量**：40,000+ 住院患者
- **链接**：https://physionet.org/content/mimiciv/

#### 2. 文献挖掘数据

**策略**：
- 系统综述提取已发表的炎症标志物数据
- Meta 分析汇总效应量
- 作为先验知识整合到模型中

### 多模态数据整合策略

```
┌────────────────────────────────────────────────────────┐
│                  多模态数据整合                        │
└────────────────────────────────────────────────────────┘

模态 1: 脑电图 (EEG)          模态 2: 炎症标志物
┌──────────────┐              ┌──────────────┐
│ CHB-MIT      │              │ NHANES       │
│ Bonn         │              │ MIMIC-IV     │
│ TUH EEG      │              │ 文献数据     │
└──────┬───────┘              └──────┬───────┘
       │                             │
       │ 特征提取                    │ 特征标准化
       │ - 时域特征                  │ - Z-score
       │ - 频域特征                  │ - 对数转换
       │ - 时频特征                  │
       │ - 深度学习特征              │
       ▼                             ▼
┌────────────────────────────────────────────────┐
│           模态融合层 (Attention/Fusion)         │
└───────────────────┬────────────────────────────┘
                    │
                    ▼
┌────────────────────────────────────────────────┐
│              下游任务层                         │
│  - 癫痫分类                                    │
│  - 发作检测                                    │
│  - 发作预测                                    │
│  - 亚型聚类                                    │
└────────────────────────────────────────────────┘
```

---

## 🔍 开源项目调研

### 癫痫深度学习项目

#### 1. **Epileptic-Seizure-Detection** ⭐ 65（最高引用）

**链接**：https://github.com/Sharad24/Epileptic-Seizure-Detection

**技术栈**：
- 深度学习
- 小波分析
- 傅里叶变换
- Bonn 数据集

**可借鉴**：
- 特征提取流程
- CNN 架构设计
- 数据增强方法

**许可证**：MIT

---

#### 2. **CHB-MIT-data-preprocessing-and-prediction** ⭐ 54

**链接**：https://github.com/tothemoon10080/CHB-MIT-data-preprocessing-and-prediction

**技术栈**：
- Python
- CHB-MIT 数据集
- 数据预处理
- 发作预测

**可借鉴**：
- **完整的预处理流程**
- 数据清洗代码
- 特征工程方法

**关键代码片段**：
```python
# 数据加载
def load_chbmit_data(data_dir):
    # 读取 EDF 文件
    # 提取发作标注
    # 数据标准化
    pass

# 特征提取
def extract_features(eeg_signal):
    # 时域特征
    # 频域特征（功率谱密度）
    # 时频特征（小波变换）
    pass
```

---

#### 3. **epilepsy2bids** ⭐ 18

**链接**：https://github.com/esl-epfl/epilepsy2bids

**描述**：将 EEG 数据集转换为 BIDS 格式

**用途**：
- 数据标准化
- 多中心数据整合
- 符合神经影像数据标准

---

#### 4. **Non-EEG_Seizure_Detection_Dataset** ⭐ 7

**链接**：https://github.com/jpordoy/Non-EEG_Seizure_Detection_Dataset

**特点**：
- **多模态**：加速度 + 心率
- **非 EEG**：补充传统脑电监测
- **可穿戴设备**：临床应用导向

**启示**：
- 可考虑整合生理信号（心率、运动）
- 增加外周生理指标作为额外模态

---

#### 5. **deepFCD**（蒙特利尔神经研究所）

**链接**：https://github.com/NOEL-MNI/deepFCD

**描述**：使用深度学习检测局灶性皮质发育不良

**技术**：
- 3D CNN
- MRI 影像分析
- 术前评估

**可借鉴**：
- 医学影像深度学习
- 多中心验证方法

---

#### 6. **BEST Toolbox**（行为状态分析）

**链接**：https://github.com/bnelair/best-toolbox

**功能**：
- 长期 iEEG 自动睡眠分期
- DBS 伪影去除
- 特征提取

**用途**：
- 植入式脑电图分析
- 行为状态分类

---

### 多模态医学深度学习框架

#### 1. **MedicalZooPytorch**

**链接**：https://github.com/black0017/MedicalZooPytorch

**特点**：
- 多模态 3D 医学图像分割
- PyTorch 实现
- 多种架构（3D U-Net, V-Net 等）

**可借鉴**：多模态融合策略

---

#### 2. **Time-Series Representation Learning (TS-TCC)**

**链接**：https://github.com/emadeldeen24/TS-TCC

**方法**：
- 时间序列对比学习
- 自监督预训练
- 迁移学习

**应用**：
- 可用于 EEG 时间序列特征学习
- 解决标注数据不足问题

---

### 开源工具总结

| 工具 | 用途 | 可借鉴点 |
|------|------|----------|
| CHB-MIT 预处理代码 | 数据加载 + 预处理 | 完整流程 |
| epilepsy2bids | 数据标准化 | BIDS 格式 |
| BEST Toolbox | iEEG 分析 | 睡眠分期 + 伪影去除 |
| MedicalZooPytorch | 多模态融合 | 架构设计 |
| TS-TCC | 自监督学习 | 对比学习 |

---

## 🎯 研究目标与假设

### 主要目标

1. **开发多模态深度学习模型**
   - 整合 EEG + 炎症标志物 + 临床数据
   - 实现癫痫精准分类和发作预测

2. **识别癫痫免疫亚型**
   - 基于炎症标志物聚类
   - 发现新的癫痫表型

3. **发现生物标志物组合**
   - 筛选关键炎症因子
   - 构建诊断/预后 panel

4. **开源工具包**
   - 发布代码和数据集
   - 推动领域发展

### 研究假设

**主要假设**：
- H1: 多模态模型优于单一模态（AUC 提升>15%）
- H2: 存在炎症介导的癫痫亚型
- H3: 炎症标志物可提高发作预测准确性

**次要假设**：
- H4: 特定细胞因子组合与发作频率相关
- H5: 抗炎治疗反应性可通过基线炎症状态预测

---

## 🔬 研究方法

### 总体设计

```
┌─────────────────────────────────────────────────────────────┐
│                     研究设计流程图                          │
└─────────────────────────────────────────────────────────────┘

阶段 1: 数据收集与预处理（第 1-4 周）
┌──────────────────┐    ┌──────────────────┐
│   EEG 数据集     │    │  炎症标志物数据  │
│ - CHB-MIT        │    │ - NHANES         │
│ - Bonn           │    │ - MIMIC-IV       │
│ - TUH EEG        │    │ - 文献挖掘       │
└────────┬─────────┘    └────────┬─────────┘
         │                       │
         ▼                       ▼
┌────────────────────────────────────────────────┐
│           数据预处理与标准化                    │
│ - 滤波、去噪、伪影去除                         │
│ - 特征提取（时域、频域、时频）                 │
│ - 缺失值插补、标准化                           │
└───────────────────┬────────────────────────────┘
                    │
阶段 2: 模型开发（第 5-10 周）
                    ▼
┌────────────────────────────────────────────────┐
│         多模态深度学习架构                      │
│                                                │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐       │
│  │ EEG 编码器│  │炎症编码器│  │临床编码器│       │
│  │ (CNN)   │  │ (MLP)   │  │ (MLP)   │       │
│  └────┬────┘  └────┬────┘  └────┬────┘       │
│       └────────────┴────────────┘              │
│                    │                           │
│              ┌─────▼─────┐                     │
│              │ 融合层     │                     │
│              │ (Attention)│                    │
│              └─────┬─────┘                     │
│                    │                           │
│       ┌────────────┴────────────┐              │
│       ▼                         ▼              │
│  ┌─────────┐              ┌─────────┐         │
│  │分类头   │              │聚类头   │         │
│  │(发作检测)│              │(亚型发现)│        │
│  └─────────┘              └─────────┘         │
└───────────────────┬────────────────────────────┘
                    │
阶段 3: 验证与解释（第 11-14 周）
                    ▼
┌────────────────────────────────────────────────┐
│           模型验证与生物学解释                  │
│ - 交叉验证                                     │
│ - 外部验证（独立队列）                         │
│ - 特征重要性（SHAP）                           │
│ - 通路富集分析                                 │
└────────────────────────────────────────────────┘
```

### 数据预处理

#### 1. EEG 数据处理

**预处理流程**：
```python
import mne
from scipy import signal
import numpy as np

def preprocess_eeg(raw_eeg, sample_rate=256):
    """
    EEG 预处理流程
    """
    # 1. 带通滤波 (0.5-70 Hz)
    raw_eeg = mne.filter.filter_data(raw_eeg, sample_rate, 0.5, 70)
    
    # 2. 陷波滤波 (50/60 Hz 去除电源干扰)
    raw_eeg = mne.filter.notch_filter(raw_eeg, sample_rate, 50)
    
    # 3. 重参考（平均参考）
    raw_eeg = raw_eeg - np.mean(raw_eeg, axis=0)
    
    # 4. 伪影检测与去除
    # - 眼电伪影（EOG）
    # - 肌电伪影（EMG）
    # 使用 ICA 或回归方法
    
    # 5. 分段（基于发作标注）
    # - 发作前期（preictal）
    # - 发作期（ictal）
    # - 发作间期（interictal）
    
    return processed_eeg
```

**特征提取**：
```python
def extract_eeg_features(eeg_segment):
    """
    提取多域特征
    """
    features = {}
    
    # 1. 时域特征
    features['mean'] = np.mean(eeg_segment)
    features['std'] = np.std(eeg_segment)
    features['skewness'] = scipy.stats.skew(eeg_segment)
    features['kurtosis'] = scipy.stats.kurtosis(eeg_segment)
    features['line_length'] = np.sum(np.abs(np.diff(eeg_segment)))
    
    # 2. 频域特征（功率谱密度）
    freqs, psd = signal.welch(eeg_segment, fs=256, nperseg=256)
    bands = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 70)
    }
    for band_name, (f_low, f_high) in bands.items():
        band_mask = (freqs >= f_low) & (freqs < f_high)
        features[f'power_{band_name}'] = np.sum(psd[band_mask])
    
    # 3. 时频特征（小波变换）
    coeffs = pywt.wavedec(eeg_segment, 'db4', level=5)
    for i, coeff in enumerate(coeffs):
        features[f'wavelet_level{i}_energy'] = np.sum(coeff ** 2)
    
    # 4. 非线性特征
    features['sample_entropy'] = sample_entropy(eeg_segment)
    features['hurst_exponent'] = hurst(eeg_segment)
    
    return features
```

#### 2. 炎症标志物处理

**标准化**：
```python
from sklearn.preprocessing import StandardScaler, RobustScaler

def process_biomarkers(biomarker_data):
    """
    炎症标志物处理
    """
    # 1. 对数转换（右偏分布）
    log_transformed = np.log1p(biomarker_data)
    
    # 2. 标准化（RobustScaler 对异常值稳健）
    scaler = RobustScaler()
    normalized = scaler.fit_transform(log_transformed)
    
    # 3. 缺失值插补（多重插补）
    from sklearn.experimental import enable_iterative_imputer
    from sklearn.impute import IterativeImputer
    
    imputer = IterativeImputer(max_iter=10, random_state=42)
    imputed_data = imputer.fit_transform(normalized)
    
    return imputed_data
```

**炎症指数计算**：
```python
def calculate_inflammatory_indices(biomarkers):
    """
    计算复合炎症指数
    """
    indices = {}
    
    # 中性粒细胞/淋巴细胞比值 (NLR)
    indices['NLR'] = biomarkers['neutrophils'] / biomarkers['lymphocytes']
    
    # 血小板/淋巴细胞比值 (PLR)
    indices['PLR'] = biomarkers['platelets'] / biomarkers['lymphocytes']
    
    # 系统免疫炎症指数 (SII)
    indices['SII'] = (biomarkers['platelets'] * 
                      biomarkers['neutrophils'] / 
                      biomarkers['lymphocytes'])
    
    # C 反应蛋白/白蛋白比值 (CAR)
    indices['CAR'] = biomarkers['CRP'] / biomarkers['albumin']
    
    return indices
```

### 模型架构

#### 多模态融合网络

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class EpilepsyMultimodalNet(nn.Module):
    """
    癫痫多模态深度学习网络
    """
    def __init__(self, config):
        super().__init__()
        
        # EEG 编码器（CNN + LSTM）
        self.eeg_encoder = EEGEncoder(
            input_channels=config['eeg_channels'],
            seq_length=config['eeg_seq_length']
        )
        
        # 炎症标志物编码器（MLP）
        self.biomarker_encoder = BiomarkerEncoder(
            input_dim=config['biomarker_dim'],
            hidden_dim=128
        )
        
        # 临床数据编码器（MLP）
        self.clinical_encoder = ClinicalEncoder(
            input_dim=config['clinical_dim'],
            hidden_dim=64
        )
        
        # 多模态融合层（注意力机制）
        self.fusion_layer = MultimodalAttentionFusion(
            modal_dims=[config['eeg_emb_dim'], 128, 64],
            embed_dim=256
        )
        
        # 任务头
        self.classification_head = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, config['num_classes'])
        )
        
        self.prediction_head = nn.Sequential(
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, 1)  # 发作时间预测
        )
    
    def forward(self, eeg_data, biomarker_data, clinical_data):
        # 编码各模态
        eeg_emb = self.eeg_encoder(eeg_data)
        biomarker_emb = self.biomarker_encoder(biomarker_data)
        clinical_emb = self.clinical_encoder(clinical_data)
        
        # 融合
        fused = self.fusion_layer([eeg_emb, biomarker_emb, clinical_emb])
        
        # 任务输出
        class_logits = self.classification_head(fused)
        pred_time = self.prediction_head(fused)
        
        return class_logits, pred_time


class EEGEncoder(nn.Module):
    """
    EEG 编码器：CNN + BiLSTM
    """
    def __init__(self, input_channels, seq_length):
        super().__init__()
        
        # 空间卷积（跨通道）
        self.spatial_conv = nn.Conv2d(1, 16, kernel_size=(input_channels, 1))
        
        # 时间卷积
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(16, 32, kernel_size=3, padding=1),
            nn.BatchNorm1d(32),
            nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=3, padding=1),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(seq_length // 4)
        )
        
        # BiLSTM
        self.lstm = nn.LSTM(
            input_size=64,
            hidden_size=128,
            num_layers=2,
            bidirectional=True,
            dropout=0.3
        )
        
        self.fc = nn.Linear(256, 128)  # 256 = 128*2 (bidirectional)
    
    def forward(self, x):
        # x shape: (batch, channels, time)
        x = x.unsqueeze(1)  # (batch, 1, channels, time)
        x = self.spatial_conv(x).squeeze(2)  # (batch, 16, time)
        x = self.temporal_conv(x)  # (batch, 64, time/4)
        x = x.permute(2, 0, 1)  # (time/4, batch, 64)
        x, _ = self.lstm(x)  # (time/4, batch, 256)
        x = x[-1]  # 取最后时间步
        x = self.fc(x)  # (batch, 128)
        return x


class MultimodalAttentionFusion(nn.Module):
    """
    多模态注意力融合
    """
    def __init__(self, modal_dims, embed_dim):
        super().__init__()
        
        # 模态投影
        self.modal_projections = nn.ModuleList([
            nn.Linear(dim, embed_dim) for dim in modal_dims
        ])
        
        # 注意力机制
        self.attention = nn.MultiheadAttention(
            embed_dim=embed_dim,
            num_heads=8,
            dropout=0.1
        )
        
        # 融合
        self.fusion_fc = nn.Linear(embed_dim * len(modal_dims), embed_dim)
    
    def forward(self, modal_embs):
        # 投影到统一维度
        projected = [proj(emb) for proj, emb in 
                     zip(self.modal_projections, modal_embs)]
        
        # 堆叠 (seq_len, batch, embed_dim)
        x = torch.stack(projected, dim=0)
        
        # 自注意力
        attended, _ = self.attention(x, x, x)
        
        # 展平 + 融合
        attended = attended.flatten(1)  # (batch, embed_dim * num_modals)
        fused = self.fusion_fc(attended)
        
        return fused
```

#### 损失函数

```python
class CombinedLoss(nn.Module):
    """
    组合损失函数
    """
    def __init__(self, alpha=0.7, beta=0.3):
        super().__init__()
        self.alpha = alpha  # 分类损失权重
        self.beta = beta    # 预测损失权重
        
        self.classification_loss = nn.CrossEntropyLoss()
        self.prediction_loss = nn.MSELoss()
    
    def forward(self, class_logits, pred_time, labels, true_time):
        loss_cls = self.classification_loss(class_logits, labels)
        loss_pred = self.prediction_loss(pred_time.squeeze(), true_time)
        
        total_loss = self.alpha * loss_cls + self.beta * loss_pred
        return total_loss
```

### 训练策略

#### 自监督预训练

```python
def contrastive_pretraining(model, eeg_data, augmentations):
    """
    对比学习预训练（TS-TCC 方法）
    """
    # 数据增强（时间扭曲、缩放、噪声）
    augmented_1 = augmentations[0](eeg_data)
    augmented_2 = augmentations[1](eeg_data)
    
    # 编码
    emb_1 = model.eeg_encoder(augmented_1)
    emb_2 = model.eeg_encoder(augmented_2)
    
    # 对比损失（InfoNCE）
    loss = nt_xent_loss(emb_1, emb_2, temperature=0.5)
    
    return loss
```

#### 迁移学习

```python
def transfer_learning(pretrained_model, target_data):
    """
    迁移学习策略
    """
    # 1. 加载预训练权重
    model = EpilepsyMultimodalNet(config)
    model.load_state_dict(pretrained_model.state_dict(), strict=False)
    
    # 2. 冻结编码器
    for param in model.eeg_encoder.parameters():
        param.requires_grad = False
    
    # 3. 微调融合层和分类头
    optimizer = torch.optim.Adam([
        {'params': model.fusion_layer.parameters()},
        {'params': model.classification_head.parameters()}
    ], lr=1e-4)
    
    return model
```

### 模型评估

#### 性能指标

```python
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, confusion_matrix, classification_report
)

def evaluate_model(model, test_loader):
    """
    全面评估模型性能
    """
    all_preds = []
    all_labels = []
    all_probs = []
    
    with torch.no_grad():
        for eeg, biomarkers, clinical, labels in test_loader:
            logits, _ = model(eeg, biomarkers, clinical)
            probs = F.softmax(logits, dim=1)
            preds = torch.argmax(logits, dim=1)
            
            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.numpy())
            all_probs.extend(probs.cpu().numpy())
    
    # 计算指标
    metrics = {
        'accuracy': accuracy_score(all_labels, all_preds),
        'precision': precision_score(all_labels, all_preds, average='weighted'),
        'recall': recall_score(all_labels, all_preds, average='weighted'),
        'f1': f1_score(all_labels, all_preds, average='weighted'),
        'auc_roc': roc_auc_score(all_labels, all_probs, multi_class='ovr')
    }
    
    # 混淆矩阵
    cm = confusion_matrix(all_labels, all_preds)
    
    return metrics, cm
```

#### 可解释性分析

```python
import shap

def interpret_model(model, data_sample):
    """
    SHAP 值解释
    """
    # 创建解释器
    explainer = shap.DeepExplainer(model, data_sample)
    
    # 计算 SHAP 值
    shap_values = explainer.shap_values(data_sample)
    
    # 可视化
    shap.summary_plot(shap_values, data_sample)
    shap.dependence_plot('IL-6', shap_values, data_sample)
    
    return shap_values
```

---

## 📈 预期结果

### 主要结果

1. **模型性能**
   - 发作检测准确率：>92%
   - 发作预测 AUC：>0.85
   - 优于单一模态模型（提升>15%）

2. **免疫亚型**
   - 识别 2-3 个炎症介导的癫痫亚型
   - 各亚型具有独特的炎症标志物谱
   - 亚型间治疗反应性差异显著

3. **生物标志物**
   - 发现 3-5 个关键炎症因子组合
   - 构建诊断 panel（灵敏度>85%，特异度>80%）
   - 验证已知标志物（IL-1β、IL-6、HMGB1）

### 图表产出

**8 个核心图表**：

| 图号 | 类型 | 内容 |
|------|------|------|
| Fig 1 | 流程图 | 研究设计与多模态融合架构 |
| Fig 2 | 表格 | 数据集基线特征 |
| Fig 3 | ROC 曲线 | 模型性能对比（多模态 vs 单模态） |
| Fig 4 | 热图 | 炎症标志物表达谱 |
| Fig 5 | t-SNE | 潜在空间聚类可视化 |
| Fig 6 | SHAP 图 | 特征重要性分析 |
| Fig 7 | 脑地形图 | EEG 特征空间分布 |
| Fig 8 | 决策曲线 | 临床实用性评估 |

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

### 5 天紧急计划（如需要）

| 天数 | 任务 | 交付物 |
|------|------|--------|
| Day 1 | 数据获取 + 预处理 | 可用数据集 |
| Day 2 | 基线模型实现 | CNN/LSTM 基线 |
| Day 3 | 多模态融合模型 | 融合架构 |
| Day 4 | 训练 + 结果分析 | 性能指标 + 图表 |
| Day 5 | 论文写作 | 完整初稿 |

---

## 🛠️ 技术栈

### 核心依赖

```python
# requirements-epilepsy.txt

# 深度学习
torch>=2.0.0
torchvision>=0.15.0
pytorch-lightning>=2.0.0

# EEG 处理
mne>=1.4.0
pyedflib>=0.1.30
eegnb>=0.1.0

# 信号处理
scipy>=1.10.0
numpy>=1.24.0
pywt>=1.4.0  # 小波变换

# 机器学习
scikit-learn>=1.3.0
shap>=0.42.0  # 可解释性

# 数据处理
pandas>=2.0.0
pyreadstat>=1.2.0  # XPT 文件

# 可视化
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.15.0

# 神经影像
nibabel>=5.0.0  # 如需处理神经影像数据

# 工具
tqdm>=4.65.0
wandb>=0.15.0  # 实验追踪
```

### 计算资源

**推荐配置**：
- GPU: NVIDIA RTX 3090 / A100（EEG 处理计算密集）
- RAM: 32GB+
- 存储：1TB SSD（EEG 数据量大）

**云平台**：
- Google Colab Pro（免费/付费）
- AWS SageMaker
- Azure ML

---

## 📚 关键参考文献

### 癫痫神经免疫学（必读 10 篇）

1. **Vezzani A, et al.** Brain inflammation as a biomarker in epilepsy. *Biomark Med*. 2011.
   - 提出炎症作为癫痫生物标志物

2. **Rana A, Musto AE.** The role of inflammation in the development of epilepsy. *J Neuroinflammation*. 2018.
   - 炎症在癫痫发生中的作用

3. **Steriade C, et al.** Acute symptomatic seizures secondary to autoimmune encephalitis. *Epilepsia*. 2020.
   - 自身免疫性癫痫概念

4. **Mazarati AM, et al.** Neurobehavioral comorbidities of epilepsy: Role of inflammation. *Epilepsia*. 2017.
   - 癫痫共病的炎症机制

### 癫痫深度学习（必读 10 篇）

5. **Tsiouris KM, et al.** A Long Short-Term Memory Deep Learning Network for EEG-Based Epileptic Seizure Prediction. *IEEE Trans Biomed Eng*. 2018.
   - LSTM 用于发作预测

6. **Truong ND, et al.** Convolutional Neural Networks for Seizure Prediction Using Intracranial and Scalp EEG. *IEEE Trans Neural Syst Rehabil Eng*. 2018.
   - CNN 用于发作预测

7. **Wei X, et al.** Deep Learning for Epileptic Seizure Detection: A Review. *IEEE Rev Biomed Eng*. 2021.
   - 系统综述

### 多模态方法学（必读 5 篇）

8. **Mohammed M, et al.** Deep learning in EEG: Advance of the last ten-year critical period. *Front Neurosci*. 2021.
   - EEG 深度学习进展

9. **Roy Y, et al.** Deep learning-based electroencephalography analysis: a systematic review. *J Neural Eng*. 2019.
   - EEG 深度学习系统综述

---

## ⚠️ 风险评估

### 技术风险

| 风险 | 概率 | 影响 | 应对策略 |
|------|------|------|----------|
| 数据异质性大 | 高 | 中 | 标准化预处理、域适应 |
| 模态不匹配 | 中 | 高 | 变量映射、多重插补 |
| 模型不收敛 | 中 | 高 | 预训练、学习率调整 |
| 过拟合 | 高 | 中 | Dropout、早停、数据增强 |

### 数据获取风险

| 数据集 | 风险 | 应对 |
|--------|------|------|
| CHB-MIT | 低（公开） | 直接下载 |
| TUH EEG | 中（需协议） | 提前申请 |
| NHANES | 低（公开） | 直接下载 |
| MIMIC-IV | 中（需培训） | 完成 CITI 培训 |

---

## 📊 数据管理

### 存储结构

```
epilepsy_immunity_project/
├── data/
│   ├── raw/              # 原始数据
│   │   ├── CHB-MIT/
│   │   ├── Bonn/
│   │   └── NHANES/
│   ├── processed/        # 处理后数据
│   └── splits/           # 数据划分
├── code/
│   ├── preprocessing/
│   ├── models/
│   ├── training/
│   └── analysis/
├── results/
│   ├── models/           # 模型权重
│   ├── predictions/
│   └── figures/
└── manuscript/
```

### 版本控制

- **代码**：Git + GitHub
- **数据**：DVC（Data Version Control）
- **模型**：Hugging Face Model Hub
- **实验**：Weights & Biases (wandb)

---

## 💰 预算估算

| 项目 | 费用 (USD) | 说明 |
|------|-----------|------|
| 计算资源 | 0-300 | Colab Pro / AWS |
| 数据获取 | 0 | 全部公开 |
| 软件许可 | 0 | 全部开源 |
| 论文发表 | 0-3000 | 开放获取（可选） |

**总计**：0-3300 USD

---

## ✅ 检查清单

### 项目启动

- [ ] 文献检索完成 ✅
- [ ] 数据申请提交
- [ ] 计算环境配置
- [ ] 代码仓库创建

### 项目执行

- [ ] 数据预处理完成
- [ ] 基线模型训练
- [ ] 多模态模型开发
- [ ] 结果验证

### 项目收尾

- [ ] 论文撰写
- [ ] 代码开源
- [ ] 数据共享
- [ ] 会议报告

---

## 🚀 立即开始

### 第一步：环境配置

```bash
# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate

# 安装依赖
pip install torch torchvision mne pywt scikit-learn shap
pip install pandas numpy matplotlib seaborn
pip install tqdm wandb
```

### 第二步：下载数据

```bash
# CHB-MIT
# 访问：https://physionet.org/content/chbmit/
# 下载所有 EDF 文件

# Bonn EEG
wget http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3

# NHANES
# 访问：https://www.cdc.gov/nchs/nhanes/
```

### 第三步：运行基线

```bash
cd code/baseline
python train_cnn.py --dataset bonn
python evaluate.py
```

---

**文档版本**: 1.0  
**最后更新**: 2026-03-19  
**状态**: ✅ 完成

> **下一步**：确认研究方向 → 开始数据预处理 → 实现基线模型

**祝研究顺利！有任何问题随时询问！** 🎉
