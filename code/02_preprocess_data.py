#!/usr/bin/env python3
"""
Bonn EEG 数据集预处理
加载数据、标准化、划分训练/测试集
"""

import os
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pickle

def load_bonn_data(data_dir="datasets/bonn_eeg"):
    """
    加载 Bonn EEG 数据集
    
    数据集包含 5 个文件夹 (A-E):
    - A: 健康志愿者 (睁眼)
    - B: 健康志愿者 (闭眼)
    - C: 发作间期 (对侧海马)
    - D: 发作间期 (同侧海马)
    - E: 发作期
    """
    data_path = Path(data_dir)
    
    # 类别映射
    class_map = {
        'A': 0,  # 健康 (睁眼)
        'B': 1,  # 健康 (闭眼)
        'C': 2,  # 发作间期 (对侧)
        'D': 3,  # 发作间期 (同侧)
        'E': 4   # 发作期
    }
    
    all_data = []
    all_labels = []
    
    print("📂 加载 Bonn EEG 数据...")
    
    # 遍历每个类别
    for folder, label in class_map.items():
        folder_path = data_path / folder
        if not folder_path.exists():
            print(f"  ⚠️  文件夹不存在：{folder}")
            continue
        
        # 读取该类别下的所有文件
        files = list(folder_path.glob("*.txt"))
        print(f"  加载 {folder}/ - {len(files)} 个文件")
        
        for file in files:
            try:
                # 读取 EEG 信号
                eeg_signal = np.loadtxt(file)
                all_data.append(eeg_signal)
                all_labels.append(label)
            except Exception as e:
                print(f"    ⚠️  读取失败：{file.name}")
    
    # 转换为 numpy 数组
    X = np.array(all_data)
    y = np.array(all_labels)
    
    print(f"\n✅ 数据加载完成:")
    print(f"  样本数：{len(X)}")
    print(f"  序列长度：{X.shape[1]}")
    print(f"  类别数：{len(np.unique(y))}")
    
    return X, y, class_map

def preprocess_data(X, y, test_size=0.2, random_state=42):
    """
    数据预处理：标准化、划分训练/测试集
    """
    print("\n🔧 数据预处理...")
    
    # 标准化（每个样本独立标准化）
    print("  标准化...")
    scaler = StandardScaler()
    X_scaled = np.array([scaler.fit_transform(x.reshape(-1, 1)).flatten() for x in X])
    
    # 划分训练/测试集
    print(f"  划分训练/测试集 (测试集比例：{test_size})...")
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"\n✅ 预处理完成:")
    print(f"  训练集：{len(X_train)} 样本")
    print(f"  测试集：{len(X_test)} 样本")
    
    return X_train, X_test, y_train, y_test, scaler

def save_preprocessed_data(output_dir="datasets/processed"):
    """
    保存预处理后的数据
    """
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # 加载和预处理
    X, y, class_map = load_bonn_data()
    X_train, X_test, y_train, y_test, scaler = preprocess_data(X, y)
    
    # 保存数据
    print("\n💾 保存预处理后的数据...")
    
    np.save(output_path / "X_train.npy", X_train)
    np.save(output_path / "X_test.npy", X_test)
    np.save(output_path / "y_train.npy", y_train)
    np.save(output_path / "y_test.npy", y_test)
    
    # 保存类别映射
    with open(output_path / "class_map.pkl", 'wb') as f:
        pickle.dump(class_map, f)
    
    # 保存标准化器
    with open(output_path / "scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
    
    print(f"✅ 数据已保存到：{output_path}")
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    # 运行预处理
    X_train, X_test, y_train, y_test = save_preprocessed_data()
    print("\n🎉 预处理完成！可以开始训练模型了！")
