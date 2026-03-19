#!/usr/bin/env python3
"""
下载最新的 NHANES 数据 (2021-2022)
"""
import urllib.request
import os
from pathlib import Path

print("=" * 70)
print("下载最新的 NHANES 数据")
print("=" * 70)

# 创建目录
nhanes_new_dir = Path("datasets/nhanes_2021_2022")
nhanes_new_dir.mkdir(parents=True, exist_ok=True)

# 2021-2022 周期数据文件
# 来源：https://wwwn.cdc.gov/nchs/nhanes/continuousnhanes/default.aspx?BeginYear=2021
files_2021_2022 = {
    # 人口学数据
    'DEMO_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/DEMO_L.XPT',
    
    # 炎症标志物 - 全血细胞计数
    'CBC_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CBC_L.XPT',
    
    # 炎症标志物 - C 反应蛋白
    'CRP_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/CRP_L.XPT',
    
    # 炎症标志物 - 纤维蛋白原
    'FIB_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/FIB_L.XPT',
    
    # 医疗状况 - 包括癫痫
    'MCQ_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/MCQ_L.XPT',
    
    # 人体测量数据（包括 BMI）
    'BMX_L': 'https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2021/DataFiles/BMX_L.XPT',
}

print(f"\n目标目录：{nhanes_new_dir}")
print(f"需要下载的文件：{len(files_2021_2022)} 个")
print(f"数据周期：2021-2022 (最新)")

downloaded = 0
failed = 0

for file_code, url in files_2021_2022.items():
    file_path = nhanes_new_dir / f"{file_code}.XPT"
    
    if file_path.exists():
        print(f"\n  ✅ {file_code}.XPT - 已存在")
        downloaded += 1
    else:
        print(f"\n  📥 下载 {file_code}.XPT ...")
        print(f"     来源：{url}")
        try:
            urllib.request.urlretrieve(url, file_path)
            size_mb = file_path.stat().st_size / (1024 * 1024)
            print(f"     ✅ 下载完成：{size_mb:.2f} MB")
            downloaded += 1
        except Exception as e:
            print(f"     ❌ 下载失败：{e}")
            failed += 1

print("\n" + "=" * 70)
print("下载完成")
print("=" * 70)
print(f"成功：{downloaded}/{len(files_2021_2022)}")
print(f"失败：{failed}/{len(files_2021_2022)}")

if downloaded > 0:
    print(f"\n数据位置：{nhanes_new_dir.absolute()}")
    print("\n下一步:")
    print("  1. 验证数据文件")
    print("  2. 加载并分析数据")
    print("  3. 与 2005-2006 数据对比")
