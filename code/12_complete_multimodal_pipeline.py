#!/usr/bin/env python3
"""
多模态癫痫预测模型 - 完整版本
整合 EEG + 炎症标志物 + 临床数据
72 小时发表计划核心代码
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# 配置
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 300

print("=" * 70)
print("多模态癫痫预测模型 - 完整流程")
print("=" * 70)

# ============================================================
# 1. 模拟数据生成（真实数据下载后替换）
# ============================================================
print("\n[1/6] 生成模拟数据（演示用，真实数据需下载）...")

np.random.seed(42)
n_samples = 1000

# EEG 特征（来自 CHB-MIT）
eeg_features = {
    'eeg_mean': np.random.normal(0, 50, n_samples),
    'eeg_std': np.random.lognormal(3, 0.5, n_samples),
    'eeg_skewness': np.random.normal(0, 1, n_samples),
    'eeg_kurtosis': np.random.normal(3, 2, n_samples),
    'power_delta': np.random.lognormal(5, 0.6, n_samples),
    'power_theta': np.random.lognormal(4.5, 0.5, n_samples),
    'power_alpha': np.random.lognormal(4, 0.5, n_samples),
    'power_beta': np.random.lognormal(3.5, 0.5, n_samples),
    'power_gamma': np.random.lognormal(3, 0.5, n_samples),
    'spectral_entropy': np.random.normal(4, 0.5, n_samples),
    'sample_entropy': np.random.normal(1, 0.3, n_samples),
    'hurst_exponent': np.random.normal(0.7, 0.1, n_samples),
    'fractal_dim': np.random.normal(1.3, 0.1, n_samples),
}

# 炎症标志物（来自 NHANES）
inflammation_features = {
    'CRP': np.random.lognormal(0, 1.5, n_samples),
    'WBC': np.random.normal(7.5, 2.5, n_samples),
    'NLR': np.random.lognormal(0.6, 0.6, n_samples),
    'PLR': np.random.lognormal(2.2, 0.4, n_samples),
    'SII': np.random.lognormal(5.5, 0.6, n_samples),
}

# 临床数据
clinical_features = {
    'Age': np.random.normal(45, 18, n_samples).clip(20, 85),
    'Sex': np.random.randint(0, 2, n_samples),
    'BMI': np.random.normal(28, 6, n_samples).clip(15, 50),
    'Diabetes': np.random.randint(0, 2, n_samples),
    'Hypertension': np.random.randint(0, 2, n_samples),
}

# 生成标签（基于多模态特征）
risk_score = (
    0.3 * np.random.rand(n_samples) +
    0.4 * (inflammation_features['NLR'] / np.max(inflammation_features['NLR'])) +
    0.3 * (eeg_features['spectral_entropy'] / np.max(eeg_features['spectral_entropy']))
)
epilepsy_prob = 0.1 + 0.6 * risk_score
epilepsy_label = (np.random.rand(n_samples) < epilepsy_prob).astype(int)

# 合并数据
df_eeg = pd.DataFrame(eeg_features)
df_inflam = pd.DataFrame(inflammation_features)
df_clinical = pd.DataFrame(clinical_features)
df_labels = pd.Series(epilepsy_label, name='Epilepsy')

print(f"  EEG 特征：{df_eeg.shape[1]} 个")
print(f"  炎症特征：{df_inflam.shape[1]} 个")
print(f"  临床特征：{df_clinical.shape[1]} 个")
print(f"  总样本量：{n_samples}")
print(f"  癫痫阳性：{epilepsy_label.sum()} ({epilepsy_label.mean()*100:.1f}%)")

# ============================================================
# 2. 数据预处理
# ============================================================
print("\n[2/6] 数据预处理...")

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer

# 合并所有特征
X_eeg = df_eeg.values
X_inflam = df_inflam.values
X_clinical = df_clinical.values
y = df_labels.values

# 标准化
scaler_eeg = StandardScaler()
scaler_inflam = StandardScaler()
scaler_clinical = StandardScaler()

X_eeg_scaled = scaler_eeg.fit_transform(X_eeg)
X_inflam_scaled = scaler_inflam.fit_transform(X_inflam)
X_clinical_scaled = scaler_clinical.fit_transform(X_clinical)

# 划分数据集
X_eeg_train, X_eeg_test, y_train, y_test = train_test_split(
    X_eeg_scaled, y, test_size=0.2, random_state=42, stratify=y
)
X_inflam_train, X_inflam_test = train_test_split(
    X_inflam_scaled, test_size=0.2, random_state=42
)
X_clinical_train, X_clinical_test = train_test_split(
    X_clinical_scaled, test_size=0.2, random_state=42
)

print(f"  训练集：{len(X_eeg_train)} 样本")
print(f"  测试集：{len(X_eeg_test)} 样本")

# ============================================================
# 3. 多模态融合模型
# ============================================================
print("\n[3/6] 训练多模态融合模型...")

from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc, classification_report, confusion_matrix

# 单模态基线
print("\n  单模态基线:")

# EEG only
rf_eeg = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_eeg.fit(X_eeg_train, y_train)
y_pred_eeg = rf_eeg.predict_proba(X_eeg_test)[:, 1]
fpr_eeg, tpr_eeg, _ = roc_curve(y_test, y_pred_eeg)
auc_eeg = auc(fpr_eeg, tpr_eeg)
print(f"    EEG only: AUC = {auc_eeg:.4f}")

# Inflammation only
rf_inflam = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_inflam.fit(X_inflam_train, y_train)
y_pred_inflam = rf_inflam.predict_proba(X_inflam_test)[:, 1]
fpr_inflam, tpr_inflam, _ = roc_curve(y_test, y_pred_inflam)
auc_inflam = auc(fpr_inflam, tpr_inflam)
print(f"    Inflammation only: AUC = {auc_inflam:.4f}")

# Clinical only
rf_clinical = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_clinical.fit(X_clinical_train, y_train)
y_pred_clinical = rf_clinical.predict_proba(X_clinical_test)[:, 1]
fpr_clinical, tpr_clinical, _ = roc_curve(y_test, y_pred_clinical)
auc_clinical = auc(fpr_clinical, tpr_clinical)
print(f"    Clinical only: AUC = {auc_clinical:.4f}")

# 多模态融合（早期融合）
print("\n  多模态融合:")
X_multimodal_train = np.hstack([X_eeg_train, X_inflam_train, X_clinical_train])
X_multimodal_test = np.hstack([X_eeg_test, X_inflam_test, X_clinical_test])

rf_multimodal = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42, n_jobs=-1)
rf_multimodal.fit(X_multimodal_train, y_train)
y_pred_multimodal = rf_multimodal.predict_proba(X_multimodal_test)[:, 1]
fpr_multi, tpr_multi, _ = roc_curve(y_test, y_pred_multimodal)
auc_multi = auc(fpr_multi, tpr_multi)
print(f"    Multimodal (Early Fusion): AUC = {auc_multi:.4f}")

# 性能提升
print(f"\n  性能提升:")
print(f"    vs EEG only: +{(auc_multi - auc_eeg)/auc_eeg*100:.1f}%")
print(f"    vs Inflammation only: +{(auc_multi - auc_inflam)/auc_inflam*100:.1f}%")
print(f"    vs Clinical only: +{(auc_multi - auc_clinical)/auc_clinical*100:.1f}%")

# ============================================================
# 4. 生成图表
# ============================================================
print("\n[4/6] 生成图表...")

fig_dir = Path("epilepsy_research/figures")
fig_dir.mkdir(parents=True, exist_ok=True)

# 图 1: ROC 曲线对比
fig, ax = plt.subplots(figsize=(10, 8))
ax.plot(fpr_eeg, tpr_eeg, linewidth=2, color='#3498db', label=f'EEG only (AUC={auc_eeg:.4f})')
ax.plot(fpr_inflam, tpr_inflam, linewidth=2, color='#e74c3c', label=f'Inflammation only (AUC={auc_inflam:.4f})')
ax.plot(fpr_clinical, tpr_clinical, linewidth=2, color='#2ecc71', label=f'Clinical only (AUC={auc_clinical:.4f})')
ax.plot(fpr_multi, tpr_multi, linewidth=2, color='#9b59b6', label=f'Multimodal (AUC={auc_multi:.4f})')
ax.plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5)
ax.set_xlabel('False Positive Rate')
ax.set_ylabel('True Positive Rate')
ax.set_title('ROC Curve Comparison - Multimodal Epilepsy Prediction')
ax.legend(loc='lower right')
ax.grid(alpha=0.3)
plt.savefig(fig_dir / '22_multimodal_roc.png', dpi=300, bbox_inches='tight')
print(f"  ✅ ROC 曲线：{fig_dir / '22_multimodal_roc.png'}")
plt.close()

# 图 2: AUC 对比柱状图
fig, ax = plt.subplots(figsize=(10, 6))
models = ['EEG', 'Inflammation', 'Clinical', 'Multimodal']
aucs = [auc_eeg, auc_inflam, auc_clinical, auc_multi]
colors = ['#3498db', '#e74c3c', '#2ecc71', '#9b59b6']
bars = ax.bar(models, aucs, color=colors)
ax.set_ylabel('AUC-ROC')
ax.set_title('Model Performance Comparison')
ax.set_ylim(0, 1)
ax.grid(alpha=0.3, axis='y')

# 添加数值标签
for bar, auc_val in zip(bars, aucs):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
            f'{auc_val:.4f}', ha='center', va='bottom', fontsize=12)
plt.savefig(fig_dir / '23_auc_comparison.png', dpi=300, bbox_inches='tight')
print(f"  ✅ AUC 对比：{fig_dir / '23_auc_comparison.png'}")
plt.close()

# 图 3: 特征重要性
feature_names = (
    list(df_eeg.columns) +
    list(df_inflam.columns) +
    list(df_clinical.columns)
)
importance = rf_multimodal.feature_importances_
feature_importance = pd.DataFrame({
    'Feature': feature_names,
    'Importance': importance
}).sort_values('Importance', ascending=False).head(20)

fig, ax = plt.subplots(figsize=(10, 12))
ax.barh(range(len(feature_importance)), feature_importance['Importance'].values)
ax.set_yticks(range(len(feature_importance)))
ax.set_yticklabels(feature_importance['Feature'])
ax.invert_yaxis()
ax.set_xlabel('Importance')
ax.set_title('Top 20 Feature Importance - Multimodal Model')
plt.savefig(fig_dir / '24_feature_importance_multimodal.png', dpi=300, bbox_inches='tight')
print(f"  ✅ 特征重要性：{fig_dir / '24_feature_importance_multimodal.png'}")
plt.close()

# 图 4: 混淆矩阵
fig, ax = plt.subplots(figsize=(8, 6))
y_pred_class = rf_multimodal.predict(X_multimodal_test)
cm = confusion_matrix(y_test, y_pred_class)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
            xticklabels=['No Epilepsy', 'Epilepsy'],
            yticklabels=['No Epilepsy', 'Epilepsy'])
ax.set_xlabel('Predicted')
ax.set_ylabel('Actual')
ax.set_title(f'Confusion Matrix - Multimodal Model (AUC={auc_multi:.4f})')
plt.savefig(fig_dir / '25_confusion_matrix_multimodal.png', dpi=300, bbox_inches='tight')
print(f"  ✅ 混淆矩阵：{fig_dir / '25_confusion_matrix_multimodal.png'}")
plt.close()

# ============================================================
# 5. 保存结果
# ============================================================
print("\n[5/6] 保存结果...")

results = {
    'auc_eeg': auc_eeg,
    'auc_inflam': auc_inflam,
    'auc_clinical': auc_clinical,
    'auc_multimodal': auc_multi,
    'improvement_vs_eeg': (auc_multi - auc_eeg) / auc_eeg * 100,
    'improvement_vs_inflam': (auc_multi - auc_inflam) / auc_inflam * 100,
    'improvement_vs_clinical': (auc_multi - auc_clinical) / auc_clinical * 100,
}

results_df = pd.DataFrame([results])
results_df.to_csv('epilepsy_research/results/multimodal_results.csv', index=False)
print(f"  ✅ 结果已保存：epilepsy_research/results/multimodal_results.csv")

# 保存分类报告
report = classification_report(y_test, y_pred_class, target_names=['No Epilepsy', 'Epilepsy'])
with open('epilepsy_research/results/classification_report.txt', 'w') as f:
    f.write(report)
print(f"  ✅ 分类报告已保存：epilepsy_research/results/classification_report.txt")

# ============================================================
# 6. 总结
# ============================================================
print("\n[6/6] 总结...")

print("\n" + "=" * 70)
print("多模态癫痫预测模型 - 完成！")
print("=" * 70)

print(f"\n关键结果:")
print(f"  EEG only: AUC = {auc_eeg:.4f}")
print(f"  Inflammation only: AUC = {auc_inflam:.4f}")
print(f"  Clinical only: AUC = {auc_clinical:.4f}")
print(f"  Multimodal: AUC = {auc_multi:.4f} ⭐")
print(f"\n性能提升:")
print(f"  vs EEG: +{results['improvement_vs_eeg']:.1f}%")
print(f"  vs Inflammation: +{results['improvement_vs_inflam']:.1f}%")
print(f"  vs Clinical: +{results['improvement_vs_clinical']:.1f}%")

print(f"\n生成的图表:")
for f in fig_dir.glob("*.png"):
    if f.name.startswith('2'):
        print(f"  ✅ {f.name}")

print(f"\n保存的文件:")
print(f"  - epilepsy_research/results/multimodal_results.csv")
print(f"  - epilepsy_research/results/classification_report.txt")

print("\n" + "=" * 70)
print("下一步:")
print("1. 下载真实数据（CHB-MIT + NHANES）")
print("2. 替换模拟数据")
print("3. 重新训练模型")
print("4. 撰写论文")
print("=" * 70)
