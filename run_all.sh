#!/bin/bash
# 癫痫研究项目 - 一键执行脚本

echo "========================================"
echo "  癫痫与免疫：多模态深度学习研究"
echo "  一键执行脚本"
echo "========================================"
echo ""

# 1. 检查 Python 环境
echo "📋 步骤 1: 检查 Python 环境..."
python3 --version
if [ $? -ne 0 ]; then
    echo "❌ Python3 未安装，请先安装 Python 3.8+"
    exit 1
fi
echo "✅ Python 环境正常"
echo ""

# 2. 安装依赖
echo "📦 步骤 2: 安装依赖包..."
pip3 install -r code/requirements.txt -q
if [ $? -ne 0 ]; then
    echo "⚠️  依赖安装可能有问题，但继续执行..."
fi
echo "✅ 依赖安装完成"
echo ""

# 3. 下载数据集
echo "📥 步骤 3: 下载 Bonn EEG 数据集..."
python3 code/01_download_bonn.py
if [ $? -ne 0 ]; then
    echo "⚠️  数据集下载失败，请检查网络连接"
    echo "   可手动下载：http://epileptologie-bonn.de/"
fi
echo ""

# 4. 数据预处理
echo "🔧 步骤 4: 数据预处理..."
python3 code/02_preprocess_data.py
if [ $? -ne 0 ]; then
    echo "❌ 数据预处理失败"
    exit 1
fi
echo ""

# 5. 训练模型
echo "🚀 步骤 5: 训练 CNN-LSTM 模型..."
python3 code/03_train_model.py
if [ $? -ne 0 ]; then
    echo "❌ 模型训练失败"
    exit 1
fi
echo ""

echo "========================================"
echo "  ✅ 所有步骤完成！"
echo "========================================"
echo ""
echo "📂 结果位置:"
echo "  - 预处理数据：datasets/processed/"
echo "  - 模型文件：models/cnn_lstm_epilepsy.pth"
echo "  - 训练历史：models/training_history.png"
echo ""
echo "🎉 可以开始分析了！"
