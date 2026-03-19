#!/usr/bin/env python3
"""
Bonn EEG 数据集下载脚本
数据集链接：http://epileptologie-bonn.de/
"""

import os
import urllib.request
import zipfile
from pathlib import Path

def download_bonn_dataset(download_dir="datasets/bonn_eeg"):
    """
    下载 Bonn EEG 数据集
    """
    download_path = Path(download_dir)
    download_path.mkdir(parents=True, exist_ok=True)
    
    # 数据集 URL
    dataset_url = "http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3&changelang=3"
    zip_file = download_path / "bonn_eeg.zip"
    
    print("📥 正在下载 Bonn EEG 数据集...")
    print(f"下载路径：{download_path}")
    
    # 检查是否已下载
    if zip_file.exists():
        print("✅ 数据集已下载，跳过下载步骤")
    else:
        try:
            # 使用 urllib 下载
            urllib.request.urlretrieve(dataset_url, zip_file)
            print("✅ 下载完成")
        except Exception as e:
            print(f"❌ 下载失败：{e}")
            print("\n请手动下载：")
            print("1. 访问：http://epileptologie-bonn.de/cms/front_content.php?idcat=193&lang=3&changelang=3")
            print("2. 保存 ZIP 文件到：", download_path)
            return False
    
    # 解压
    print("\n📦 正在解压数据集...")
    try:
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(download_path)
        print("✅ 解压完成")
    except Exception as e:
        print(f"❌ 解压失败：{e}")
        return False
    
    # 显示数据集结构
    print("\n📂 数据集结构:")
    for folder in sorted(download_path.iterdir()):
        if folder.is_dir():
            n_files = len(list(folder.glob("*.txt")))
            print(f"  {folder.name}/ - {n_files} 个文件")
    
    print("\n✅ Bonn EEG 数据集准备完成！")
    return True

if __name__ == "__main__":
    success = download_bonn_dataset()
    if success:
        print("\n🎉 数据集已就绪，可以开始预处理！")
    else:
        print("\n⚠️ 请检查下载问题后重试")
