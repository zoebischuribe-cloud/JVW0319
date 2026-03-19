# 📊 已下载数据完整清单

**更新时间**: 2026-03-19 10:54  
**存储位置**: `/home/admin/openclaw/workspace/datasets/`

---

## ✅ 已下载数据总览

| 数据集 | 周期 | 文件数 | 总大小 | 状态 |
|--------|------|--------|--------|------|
| **NHANES 2021-2022** | 最新 | 4 | 8.8 MB | ✅ 已下载 |
| **NHANES 2005-2006** | 旧 | 4 | 13.8 MB | ✅ 已下载 |
| **CHB-MIT EEG** | - | 0 | 0 MB | ⏳ 需下载 |
| **MIMIC-IV** | - | 0 | 0 MB | ⏳ 需下载 |

**总计**: 8 个文件，22.6 MB

---

## 📁 NHANES 2021-2022（最新）⭐推荐

**存储位置**: `/home/admin/openclaw/workspace/datasets/nhanes_2021_2022/`

### 文件清单（4 个）

| 文件名 | 大小 | 样本量 | 内容 | 官方下载链接 |
|--------|------|--------|------|-------------|
| **DEMO_L.XPT** | 2.5 MB | 11,933 | 人口学数据 | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT) |
| **CBC_L.XPT** | 1.6 MB | 8,727 | 血常规（炎症标志物） | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CBC_L.XPT) |
| **MCQ_L.XPT** | 3.2 MB | 11,744 | 医疗状况（含癫痫） | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.XPT) |
| **BMX_L.XPT** | 1.5 MB | 8,860 | 人体测量（含 BMI） | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT) |

**总大小**: 8.8 MB

### 官方来源

- **数据库**: NHANES (National Health and Nutrition Examination Survey)
- **周期**: 2021-2022 (Cycle L)
- **机构**: 美国 CDC
- **网址**: https://wwwn.cdc.gov/Nchs/Nhanes/ContinuousNhanes/Default.aspx?BeginYear=2021

### 一键下载脚本

```bash
#!/bin/bash
mkdir -p nhanes_2021_2022
cd nhanes_2021_2022

wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CBC_L.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT

echo "✅ NHANES 2021-2022 下载完成！"
```

---

## 📁 NHANES 2005-2006（旧）

**存储位置**: `/home/admin/openclaw/workspace/datasets/nhanes_inflammation/`

### 文件清单（4 个）

| 文件名 | 大小 | 样本量 | 内容 | 官方下载链接 |
|--------|------|--------|------|-------------|
| **DEMO_D.XPT** | 3.5 MB | 10,348 | 人口学数据 | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/DEMO_D.XPT) |
| **BIOPRO_D.XPT** | 2.0 MB | 6,980 | 生化标志物（含 CRP） | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/BIOPRO_D.XPT) |
| **CBC_D.XPT** | 1.6 MB | 9,440 | 血常规 | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/CBC_D.XPT) |
| **MCQ_D.XPT** | 6.7 MB | 9,822 | 医疗状况 | [下载](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.XPT) |

**总大小**: 13.8 MB

### 官方来源

- **数据库**: NHANES
- **周期**: 2005-2006 (Cycle D)
- **机构**: 美国 CDC
- **网址**: https://wwwn.cdc.gov/Nchs/Nhanes/ContinuousNhanes/Default.aspx?BeginYear=2005

### 一键下载脚本

```bash
#!/bin/bash
mkdir -p nhanes_inflammation
cd nhanes_inflammation

wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/DEMO_D.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/BIOPRO_D.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/CBC_D.XPT
wget https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.XPT

echo "✅ NHANES 2005-2006 下载完成！"
```

---

## ⏳ CHB-MIT EEG（待下载）

**存储位置**: `/home/admin/openclaw/workspace/datasets/chbmit_eeg/`

### 数据信息

| 特征 | 详情 |
|------|------|
| **数据库** | CHB-MIT Scalp EEG Database |
| **版本** | 1.0.0 |
| **样本量** | 22 名患者，664 个记录 |
| **数据量** | ~1.2 GB |
| **格式** | EDF (.edf) |
| **通道数** | 23-26 通道 |
| **采样率** | 256 Hz |

### 官方下载链接

- **主页**: https://physionet.org/content/chbmit/1.0.0/
- **直接下载**: https://physionet.org/files/chbmit/1.0.0/

### 下载步骤

1. **注册 PhysioNet 账号**（免费，5 分钟）
   - 访问：https://physionet.org/register/

2. **下载数据**
   ```bash
   wget -r -N -c -np --user YOUR_USERNAME --ask-password \
     https://physionet.org/files/chbmit/1.0.0/
   ```

3. **或使用浏览器下载**
   - 访问：https://physionet.org/content/chbmit/1.0.0/
   - 点击 "Download" → "Download all files"

### 本地说明文件

已创建：`datasets/chbmit_eeg/README.txt`

---

## ⏳ MIMIC-IV（待下载）

**存储位置**: `/home/admin/openclaw/workspace/datasets/mimic_iv/`

### 数据信息

| 特征 | 详情 |
|------|------|
| **数据库** | MIMIC-IV (Medical Information Mart for Intensive Care) |
| **版本** | 3.0 |
| **样本量** | 40,000+ 住院患者 |
| **数据量** | ~50 GB |
| **内容** | ICU 患者完整记录 |

### 官方下载链接

- **主页**: https://physionet.org/content/mimiciv/
- **申请**: https://physionet.org/settings/application/

### 下载步骤

1. **完成 CITI 培训**（约 2 小时）
   - 访问：https://www.citiprogram.org/
   - 选择 "Data or Specimens Only Research"

2. **申请访问权限**
   - 访问：https://physionet.org/settings/application/
   - 提交 CITI 证书
   - 签署数据使用协议

3. **等待审核**（1-2 天）

4. **下载数据**
   ```bash
   wget -r -N -c -np --user YOUR_USERNAME --ask-password \
     https://physionet.org/files/mimiciv/3.0/
   ```

### 本地说明文件

已创建：`datasets/mimic_iv/README.txt`

---

## 📥 完整下载脚本（一键下载所有）

### NHANES 数据（立即可下载）

```bash
#!/bin/bash
# download_all_nhanes.sh
# 下载所有 NHANES 数据

echo "=========================================="
echo "下载 NHANES 数据"
echo "=========================================="

# 2021-2022（最新）
echo -e "\n[1/2] 下载 NHANES 2021-2022（最新）..."
mkdir -p nhanes_2021_2022
cd nhanes_2021_2022

wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CBC_L.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT

echo "  ✅ 2021-2022 完成（4 个文件，8.8 MB）"
cd ..

# 2005-2006
echo -e "\n[2/2] 下载 NHANES 2005-2006..."
mkdir -p nhanes_inflammation
cd nhanes_inflammation

wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/DEMO_D.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/BIOPRO_D.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/CBC_D.XPT
wget -q https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.XPT

echo "  ✅ 2005-2006 完成（4 个文件，13.8 MB）"
cd ..

echo -e "\n=========================================="
echo "✅ 所有 NHANES 数据下载完成！"
echo "=========================================="
echo "总大小：22.6 MB"
echo "位置：$(pwd)"
```

---

## 📊 数据对比总结

### 已下载数据（立即可用）

| 数据集 | 文件 | 大小 | 样本量 | 状态 |
|--------|------|------|--------|------|
| **NHANES 2021-2022** | 4 | 8.8 MB | 11,933 | ✅ 本地 |
| **NHANES 2005-2006** | 4 | 13.8 MB | 10,348 | ✅ 本地 |

### 待下载数据

| 数据集 | 文件 | 大小 | 样本量 | 要求 |
|--------|------|------|--------|------|
| **CHB-MIT EEG** | ~40 | 1.2 GB | 664 记录 | PhysioNet 账号 |
| **MIMIC-IV** | ~100 | 50 GB | 40,000+ | CITI 培训 + 审核 |

---

## 🔗 快速访问链接

### NHANES 2021-2022（最新）⭐

- **总览**: https://wwwn.cdc.gov/Nchs/Nhanes/ContinuousNhanes/Default.aspx?BeginYear=2021
- **DEMO_L**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT
- **CBC_L**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CBC_L.XPT
- **MCQ_L**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.XPT
- **BMX_L**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT

### NHANES 2005-2006

- **总览**: https://wwwn.cdc.gov/Nchs/Nhanes/ContinuousNhanes/Default.aspx?BeginYear=2005
- **DEMO_D**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/DEMO_D.XPT
- **BIOPRO_D**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/BIOPRO_D.XPT
- **CBC_D**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/CBC_D.XPT
- **MCQ_D**: https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.XPT

### CHB-MIT EEG

- **主页**: https://physionet.org/content/chbmit/1.0.0/
- **下载**: https://physionet.org/files/chbmit/1.0.0/

### MIMIC-IV

- **主页**: https://physionet.org/content/mimiciv/
- **申请**: https://physionet.org/settings/application/

---

## 📂 本地路径

**工作目录**: `/home/admin/openclaw/workspace/datasets/`

```
datasets/
├── nhanes_2021_2022/          # ✅ 最新数据（推荐）
│   ├── DEMO_L.XPT            (2.5 MB)
│   ├── CBC_L.XPT             (1.6 MB)
│   ├── MCQ_L.XPT             (3.2 MB)
│   └── BMX_L.XPT             (1.5 MB)
├── nhanes_inflammation/       # ✅ 旧数据（对比用）
│   ├── DEMO_D.XPT            (3.5 MB)
│   ├── BIOPRO_D.XPT          (2.0 MB)
│   ├── CBC_D.XPT             (1.6 MB)
│   └── MCQ_D.XPT             (6.7 MB)
├── chbmit_eeg/               # ⏳ 待下载
│   └── README.txt
└── mimic_iv/                 # ⏳ 待下载
    └── README.txt
```

---

## ✅ 验证数据完整性

### MD5 校验（已下载文件）

| 文件 | MD5 | 验证 |
|------|-----|------|
| DEMO_L.XPT | - | ✅ 可读取 |
| CBC_L.XPT | - | ✅ 可读取 |
| MCQ_L.XPT | - | ✅ 可读取 |
| BMX_L.XPT | - | ✅ 可读取 |
| DEMO_D.XPT | `7d61923d...` | ✅ 已验证 |
| BIOPRO_D.XPT | `59dba4e9...` | ✅ 已验证 |
| CBC_D.XPT | `10bac2cd...` | ✅ 已验证 |
| MCQ_D.XPT | `1786c965...` | ✅ 已验证 |

---

## 🎯 推荐使用

**✅ 立即使用**: NHANES 2021-2022（最新，8.8 MB）
- 数据最新（2021-2022）
- 样本量大（11,933 人）
- 检测技术先进
- 后疫情时代数据

**⏳ 后续下载**: CHB-MIT EEG（1.2 GB）
- 需要 PhysioNet 账号
- 5 分钟注册即可完成

**⏳ 长期计划**: MIMIC-IV（50 GB）
- 需要 CITI 培训
- 2 小时培训 + 1-2 天审核

---

**所有数据已整理完成！**  
**可以立即开始分析！** 🚀
