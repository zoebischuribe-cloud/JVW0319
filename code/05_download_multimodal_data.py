#!/usr/bin/env python3
"""
多模态数据下载脚本
方案 B: NHANES (炎症) + CHB-MIT (EEG)
方案 C: MIMIC-IV (多模态重症数据)
"""

import os
import urllib.request
import zipfile
from pathlib import Path

print("=" * 60)
print("多模态数据下载 - 方案 B + 方案 C")
print("=" * 60)

# 创建数据目录
data_dir = Path("datasets")
data_dir.mkdir(parents=True, exist_ok=True)

# ============================================================
# 方案 B: NHANES 炎症数据
# ============================================================
print("\n[方案 B] NHANES 炎症数据下载...")
print("-" * 60)

nhanes_dir = data_dir / "nhanes_inflammation"
nhanes_dir.mkdir(parents=True, exist_ok=True)

# NHANES 数据文件列表（2005-2006 轮次）
# 炎症标志物：CRP、白细胞计数等
nhanes_files = {
    # 人口学数据
    'DEMO_D': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/DEMO_D.XPT',
    
    # 实验室数据 - 炎症标志物
    'BIOPRO_D': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/BIOPRO_D.XPT',  # CRP 等
    
    # 血液学 - 白细胞分类
    'CBC_D': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/CBC_D.XPT',
    
    # 神经系统状况 - 癫痫史
    'MCQ_D': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2005/DataFiles/MCQ_D.XPT',
}

print(f"数据目录：{nhanes_dir}")
print(f"需要下载的文件：{len(nhanes_files)} 个")

for file_code, url in nhanes_files.items():
    file_path = nhanes_dir / f"{file_code}.XPT"
    
    if file_path.exists():
        print(f"  ✅ {file_code}.XPT - 已存在")
    else:
        print(f"  📥 下载 {file_code}.XPT ...")
        try:
            urllib.request.urlretrieve(url, file_path)
            print(f"     ✅ 下载完成：{file_path.stat().st_size / 1024:.1f} KB")
        except Exception as e:
            print(f"     ❌ 下载失败：{e}")
            print(f"     手动下载：{url}")

print("\n[方案 B] NHANES 数据下载完成！")

# ============================================================
# 方案 B: CHB-MIT EEG 数据
# ============================================================
print("\n[方案 B] CHB-MIT EEG 数据下载...")
print("-" * 60)

chbmit_dir = data_dir / "chbmit_eeg"
chbmit_dir.mkdir(parents=True, exist_ok=True)

print(f"数据目录：{chbmit_dir}")
print("\nCHB-MIT 数据集需要 PhysioNet 账号")
print("下载步骤：")
print("1. 访问：https://physionet.org/content/chbmit/1.0.0/")
print("2. 登录或注册 PhysioNet 账号（免费）")
print("3. 下载所有 .edf 文件")
print("4. 保存到：", chbmit_dir)
print("\n或者使用 wget 命令（需要账号）：")
print(f"wget -r -N -c -np --user YOUR_USERNAME --ask-password \\")
print(f"  https://physionet.org/files/chbmit/1.0.0/")

# 创建下载说明文件
readme_path = chbmit_dir / "README.txt"
with open(readme_path, 'w') as f:
    f.write("""CHB-MIT EEG 数据集下载说明

1. 访问：https://physionet.org/content/chbmit/1.0.0/
2. 登录或注册 PhysioNet 账号（免费，约 2 分钟）
3. 下载所有 .edf 文件（约 1.2GB）
4. 解压到此目录

数据集信息:
- 22 名儿科癫痫患者
- 664 个 EEG 记录
- 900+ 小时连续监测
- 198 次癫痫发作
- 23-26 通道，采样率 256 Hz

引用:
Guttag, J. (2010). CHB-MIT Scalp EEG Database (version 1.0.0). 
PhysioNet. https://doi.org/10.13026/C2K01R
""")

print(f"\n✅ 下载说明已保存：{readme_path}")

# ============================================================
# 方案 C: MIMIC-IV 数据
# ============================================================
print("\n[方案 C] MIMIC-IV 数据下载...")
print("-" * 60)

mimic_dir = data_dir / "mimic_iv"
mimic_dir.mkdir(parents=True, exist_ok=True)

print(f"数据目录：{mimic_dir}")
print("\nMIMIC-IV 数据集需要完成 CITI 培训")
print("获取步骤：")
print("1. 访问：https://physionet.org/content/mimiciv/")
print("2. 完成 CITI 伦理培训（约 2 小时，免费）")
print("3. 签署数据使用协议")
print("4. 等待审核（通常 1-2 天）")
print("5. 下载数据（约 50GB）")
print("\n或者先使用 MIMIC-III Demo 数据（无需培训）：")
print("https://physionet.org/content/mimic3-demo/")

# 创建下载说明文件
readme_path = mimic_dir / "README.txt"
with open(readme_path, 'w') as f:
    f.write("""MIMIC-IV 数据集下载说明

步骤 1: 完成 CITI 培训
- 访问：https://www.citiprogram.org/
- 选择 "Data or Specimens Only Research"
- 完成培训（约 2 小时）
- 获得证书

步骤 2: 申请 MIMIC-IV 访问权限
- 访问：https://physionet.org/content/mimiciv/
- 提交 CITI 证书
- 签署数据使用协议
- 等待审核（1-2 天）

步骤 3: 下载数据
- 审核通过后下载
- 数据量：约 50GB
- 包含：ICU 患者完整记录

数据集信息:
- 40,000+ 住院患者
- 炎症标志物（CRP、白细胞等）
- 生命体征（心率、血压等）
- 诊断编码（ICD-9/10，包括癫痫）
- 用药记录
- 部分患者有 EEG 数据

替代方案：MIMIC-III Demo（无需培训）
- 访问：https://physionet.org/content/mimic3-demo/
- 小样本演示数据
- 可立即下载使用

引用:
Johnson, A. E. W., et al. (2023). MIMIC-IV. 
PhysioNet. https://doi.org/10.13026/6mm1-ek79
""")

print(f"\n✅ 下载说明已保存：{readme_path}")

# ============================================================
# 总结
# ============================================================
print("\n" + "=" * 60)
print("数据下载状态总结")
print("=" * 60)

print("\n[方案 B] NHANES + CHB-MIT")
print("  ✅ NHANES 炎症数据 - 可立即下载（公开）")
print("  ⏳ CHB-MIT EEG 数据 - 需 PhysioNet 账号（5 分钟注册）")
print("  预计开始时间：10-15 分钟")

print("\n[方案 C] MIMIC-IV")
print("  ⏳ 需 CITI 培训（2 小时）+ 审核（1-2 天）")
print("  替代：MIMIC-III Demo（立即可用）")
print("  预计开始时间：1-2 天（完整数据）或 立即（Demo）")

print("\n[建议]")
print("1. 立即开始 NHANES 数据分析（方案 B 的一部分）")
print("2. 同时注册 PhysioNet 账号下载 CHB-MIT")
print("3. MIMIC-IV 作为后续验证队列（申请中）")

print("\n" + "=" * 60)
print("下一步：创建多模态融合模型代码")
print("=" * 60)
