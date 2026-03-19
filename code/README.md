# CNN-LSTM 癫痫发作检测模型

基于 Bonn EEG 数据集的深度学习实现

## 环境要求

```bash
pip install torch torchvision torchaudio mne scikit-learn scipy numpy matplotlib tqdm
```

## 使用方法

```bash
# 1. 下载数据
python download_bonn_dataset.py

# 2. 预处理数据
python preprocess_data.py

# 3. 训练模型
python train.py

# 4. 评估模型
python evaluate.py
```

## 模型架构

```
输入 (EEG 信号)
    ↓
卷积层 (特征提取)
    ↓
LSTM 层 (时间序列建模)
    ↓
全连接层 (分类)
    ↓
输出 (5 类：A-E)
```

## 预期性能

- 准确率：>95% (二分类)
- 准确率：>90% (五分类)
- 训练时间：~10 分钟 (CPU)
