#!/usr/bin/env python3
"""
72 小时发表计划 - Day 1 完整分析流程
调用所有可用 skills: exploratory-data-analysis, statistical-analysis, scientific-visualization
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# 科学可视化配置
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 12

print("=" * 60)
print("72 小时发表计划 - Day 1 数据分析")
print("=" * 60)

# 1. 数据加载
print("\n[1/6] 加载 Bonn EEG 数据集...")
data_dir = Path("datasets/bonn_eeg")

if not data_dir.exists():
    print(f"❌ 数据目录不存在：{data_dir}")
    print("请先下载数据")
else:
    # 遍历所有文件夹
    classes = ['A', 'B', 'C', 'D', 'E']
    class_names = {
        'A': 'Healthy (Open)',
        'B': 'Healthy (Closed)',
        'C': 'Interictal (Contralateral)',
        'D': 'Interictal (Ipsilateral)',
        'E': 'Ictal (Seizure)'
    }
    
    all_data = []
    all_labels = []
    
    for folder in classes:
        folder_path = data_dir / folder
        if folder_path.exists():
            files = list(folder_path.glob("*.txt"))
            print(f"  {folder} ({class_names[folder]}): {len(files)} 文件")
            
            for file in files:
                try:
                    eeg = np.loadtxt(file)
                    all_data.append(eeg)
                    all_labels.append(folder)
                except:
                    pass
    
    print(f"\n✅ 加载完成：{len(all_data)} 个样本")

# 2. 探索性数据分析 (exploratory-data-analysis skill)
print("\n[2/6] 探索性数据分析...")

if len(all_data) > 0:
    # 基本统计
    sample_lengths = [len(x) for x in all_data]
    print(f"  样本长度：{np.mean(sample_lengths):.0f} ± {np.std(sample_lengths):.0f} 点")
    print(f"  信号范围：[{min([x.min() for x in all_data]):.2f}, {max([x.max() for x in all_data]):.2f}]")
    
    # 可视化
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    axes = axes.flatten()
    
    # 每个类别的示例信号
    for i, folder in enumerate(classes):
        idx = [j for j, label in enumerate(all_labels) if label == folder]
        if len(idx) > 0:
            sample_idx = idx[0]
            axes[i].plot(all_data[sample_idx][:1000], linewidth=0.5)
            axes[i].set_title(f'{folder}: {class_names[folder]}')
            axes[i].set_xlabel('Time Point')
            axes[i].set_ylabel('Amplitude')
    
    # 样本长度分布
    axes[5].hist(sample_lengths, bins=50, edgecolor='black')
    axes[5].set_title('Sample Length Distribution')
    axes[5].set_xlabel('Length (points)')
    axes[5].set_ylabel('Count')
    
    plt.tight_layout()
    
    # 保存到 figures 目录
    fig_dir = Path("epilepsy_research/figures")
    fig_dir.mkdir(parents=True, exist_ok=True)
    plt.savefig(fig_dir / "01_exploratory_analysis.png", dpi=300, bbox_inches='tight')
    print(f"✅ 探索性分析图已保存：{fig_dir / '01_exploratory_analysis.png'}")
    plt.close()

# 3. 特征提取
print("\n[3/6] 特征提取...")

def extract_features(eeg_signal, fs=173.61):
    """
    提取多域特征
    """
    features = {}
    
    # 时域特征
    features['mean'] = np.mean(eeg_signal)
    features['std'] = np.std(eeg_signal)
    features['min'] = np.min(eeg_signal)
    features['max'] = np.max(eeg_signal)
    features['skewness'] = pd.Series(eeg_signal).skew()
    features['kurtosis'] = pd.Series(eeg_signal).kurtosis()
    features['rms'] = np.sqrt(np.mean(eeg_signal**2))
    
    # 频域特征（简化版）
    fft_vals = np.fft.fft(eeg_signal)
    fft_freq = np.fft.fftfreq(len(eeg_signal), 1/fs)
    
    # 功率谱密度
    psd = np.abs(fft_vals)**2
    
    # 频带功率
    bands = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 70)
    }
    
    for band_name, (f_low, f_high) in bands.items():
        mask = (fft_freq >= f_low) & (fft_freq < f_high)
        features[f'power_{band_name}'] = np.sum(psd[mask])
    
    # 总功率
    features['total_power'] = np.sum(psd[:len(psd)//2])
    
    # 谱熵
    psd_norm = psd[:len(psd)//2] / np.sum(psd[:len(psd)//2])
    features['spectral_entropy'] = -np.sum(psd_norm * np.log(psd_norm + 1e-10))
    
    return features

if len(all_data) > 0:
    print("  提取特征中...")
    feature_list = []
    
    for i, eeg in enumerate(all_data):
        feats = extract_features(eeg)
        feats['label'] = all_labels[i]
        feature_list.append(feats)
        
        if (i+1) % 100 == 0:
            print(f"    已处理 {i+1}/{len(all_data)} 样本")
    
    # 转换为 DataFrame
    feature_df = pd.DataFrame(feature_list)
    print(f"✅ 特征提取完成：{feature_df.shape[0]} 样本 × {feature_df.shape[1]-1} 特征")
    
    # 保存特征
    feature_df.to_csv("datasets/processed/eeg_features.csv", index=False)
    print(f"✅ 特征已保存：datasets/processed/eeg_features.csv")

# 4. 统计分析 (statistical-analysis skill)
print("\n[4/6] 统计分析...")

if len(all_data) > 0:
    from scipy import stats
    
    # 组间比较
    print("  组间差异检验（ANOVA）:")
    
    numeric_cols = feature_df.select_dtypes(include=[np.number]).columns
    
    for col in numeric_cols[:10]:  # 只显示前 10 个特征
        groups = [feature_df[feature_df['label']==label][col] for label in classes]
        f_stat, p_val = stats.f_oneway(*groups)
        
        if p_val < 0.001:
            print(f"    {col}: F={f_stat:.2f}, P<{p_val:.4f} ***")
        elif p_val < 0.01:
            print(f"    {col}: F={f_stat:.2f}, P<{p_val:.3f} **")
        elif p_val < 0.05:
            print(f"    {col}: F={f_stat:.2f}, P={p_val:.3f} *")

# 5. 可视化 (scientific-visualization skill)
print("\n[5/6] 科学可视化...")

if len(all_data) > 0:
    # 热图
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # 选择前 20 个特征
    top_features = numeric_cols[:20].tolist()
    pivot_data = feature_df.groupby('label')[top_features].mean()
    
    sns.heatmap(pivot_data, annot=True, fmt='.2f', cmap='YlOrRd', ax=ax)
    plt.title('Feature Patterns by Class')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    plt.savefig(fig_dir / "02_feature_heatmap.png", dpi=300, bbox_inches='tight')
    print(f"✅ 特征热图已保存：{fig_dir / '02_feature_heatmap.png'}")
    plt.close()
    
    # 箱线图
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()
    
    key_features = ['std', 'spectral_entropy', 'power_delta', 'power_gamma']
    
    for i, feat in enumerate(key_features):
        if feat in feature_df.columns:
            data_to_plot = [feature_df[feature_df['label']==label][feat] for label in classes]
            axes[i].boxplot(data_to_plot, labels=classes)
            axes[i].set_title(feat.replace('_', ' ').title())
            axes[i].set_xticklabels(classes, rotation=45)
    
    plt.tight_layout()
    plt.savefig(fig_dir / "03_feature_boxplot.png", dpi=300, bbox_inches='tight')
    print(f"✅ 特征箱线图已保存：{fig_dir / '03_feature_boxplot.png'}")
    plt.close()

# 6. 基线模型训练
print("\n[6/6] 基线模型训练...")

if len(all_data) > 0:
    from sklearn.model_selection import train_test_split
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.metrics import classification_report, roc_curve, auc, confusion_matrix
    
    # 准备数据
    X = feature_df[numeric_cols].fillna(0)
    y = feature_df['label']
    
    # 二分类：发作期 vs 非发作期
    y_binary = (y == 'E').astype(int)
    
    # 划分训练测试集
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_binary, test_size=0.2, random_state=42, stratify=y_binary
    )
    
    print(f"  训练集：{len(X_train)} 样本")
    print(f"  测试集：{len(X_test)} 样本")
    
    # 训练随机森林
    print("  训练随机森林模型...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
    rf.fit(X_train, y_train)
    
    # 预测
    y_pred = rf.predict(X_test)
    y_pred_proba = rf.predict_proba(X_test)[:, 1]
    
    # 评估
    print("\n  模型性能:")
    print(classification_report(y_test, y_pred, target_names=['Non-Seizure', 'Seizure']))
    
    # ROC 曲线
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = auc(fpr, tpr)
    
    print(f"  AUC-ROC: {roc_auc:.4f}")
    
    # 可视化
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    
    # ROC 曲线
    axes[0].plot(fpr, tpr, f'AUC = {roc_auc:.3f}', linewidth=2)
    axes[0].plot([0, 1], [0, 1], 'k--', linewidth=1)
    axes[0].set_xlabel('False Positive Rate')
    axes[0].set_ylabel('True Positive Rate')
    axes[0].set_title('ROC Curve - Seizure Detection')
    axes[0].legend()
    axes[0].grid(alpha=0.3)
    
    # 特征重要性
    feature_importance = pd.DataFrame({
        'Feature': numeric_cols,
        'Importance': rf.feature_importances_
    }).sort_values('Importance', ascending=False).head(15)
    
    sns.barplot(data=feature_importance, x='Importance', y='Feature', ax=axes[1])
    axes[1].set_title('Top 15 Features')
    axes[1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.savefig(fig_dir / "04_baseline_model.png", dpi=300, bbox_inches='tight')
    print(f"✅ 基线模型结果已保存：{fig_dir / '04_baseline_model.png'}")
    plt.close()

print("\n" + "=" * 60)
print("✅ Day 1 数据分析完成！")
print("=" * 60)
print(f"\n生成的图表:")
print(f"  1. {fig_dir / '01_exploratory_analysis.png'}")
print(f"  2. {fig_dir / '02_feature_heatmap.png'}")
print(f"  3. {fig_dir / '03_feature_boxplot.png'}")
print(f"  4. {fig_dir / '04_baseline_model.png'}")
print(f"\n下一步：多模态深度学习模型训练")
