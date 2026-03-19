#!/usr/bin/env python3
"""
CNN-LSTM 癫痫发作检测模型
基于 Bonn EEG 数据集
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import numpy as np
from pathlib import Path
from tqdm import tqdm
import matplotlib.pyplot as plt

class CNN_LSTM_Epilepsy(nn.Module):
    """
    CNN-LSTM 癫痫检测模型
    
    架构:
    输入 → 1D 卷积 → LSTM → 全连接 → 输出
    """
    def __init__(self, input_size=4097, num_classes=5, cnn_channels=64, lstm_hidden=128):
        super(CNN_LSTM_Epilepsy, self).__init__()
        
        # 1D 卷积层 (特征提取)
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=cnn_channels, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm1d(cnn_channels)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)
        
        self.conv2 = nn.Conv1d(in_channels=cnn_channels, out_channels=cnn_channels*2, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm1d(cnn_channels*2)
        
        # LSTM 层 (时间序列建模)
        self.lstm = nn.LSTM(
            input_size=cnn_channels*2,
            hidden_size=lstm_hidden,
            num_layers=2,
            batch_first=True,
            dropout=0.3,
            bidirectional=True
        )
        
        # 全连接层 (分类)
        self.fc1 = nn.Linear(lstm_hidden*2, 64)  # *2 for bidirectional
        self.dropout = nn.Dropout(0.5)
        self.fc2 = nn.Linear(64, num_classes)
    
    def forward(self, x):
        # x shape: (batch, seq_len)
        x = x.unsqueeze(1)  # (batch, 1, seq_len)
        
        # 卷积层
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu(x)
        x = self.pool(x)
        
        # LSTM 输入需要 (batch, seq_len, features)
        x = x.permute(0, 2, 1)  # (batch, new_seq_len, features)
        
        # LSTM
        lstm_out, (h_n, c_n) = self.lstm(x)
        
        # 取最后一个时间步的输出
        # 双向 LSTM 需要拼接两个方向的隐藏状态
        h_forward = h_n[-2]
        h_backward = h_n[-1]
        h_concat = torch.cat((h_forward, h_backward), dim=1)
        
        # 全连接层
        x = self.fc1(h_concat)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.fc2(x)
        
        return x

def train_model(model, train_loader, criterion, optimizer, device, epochs=50):
    """
    训练模型
    """
    model.to(device)
    model.train()
    
    train_losses = []
    train_accs = []
    
    print(f"\n🚀 开始训练 (设备：{device})")
    print(f"  训练样本数：{len(train_loader.dataset)}")
    print(f"  批次大小：{train_loader.batch_size}")
    print(f"  训练轮数：{epochs}")
    print("-" * 60)
    
    for epoch in range(epochs):
        running_loss = 0.0
        correct = 0
        total = 0
        
        pbar = tqdm(train_loader, desc=f'Epoch {epoch+1}/{epochs}')
        
        for batch_data, batch_labels in pbar:
            batch_data = batch_data.to(device)
            batch_labels = batch_labels.to(device)
            
            # 前向传播
            optimizer.zero_grad()
            outputs = model(batch_data)
            loss = criterion(outputs, batch_labels)
            
            # 反向传播
            loss.backward()
            optimizer.step()
            
            # 统计
            running_loss += loss.item()
            _, predicted = torch.max(outputs.data, 1)
            total += batch_labels.size(0)
            correct += (predicted == batch_labels).sum().item()
            
            # 更新进度条
            pbar.set_postfix({
                'loss': f'{loss.item():.4f}',
                'acc': f'{100*correct/total:.2f}%'
            })
        
        # 计算 epoch 平均
        epoch_loss = running_loss / len(train_loader)
        epoch_acc = 100 * correct / total
        train_losses.append(epoch_loss)
        train_accs.append(epoch_acc)
        
        print(f"  Epoch [{epoch+1}/{epochs}] Loss: {epoch_loss:.4f} Acc: {epoch_acc:.2f}%")
    
    print("-" * 60)
    print(f"✅ 训练完成！")
    print(f"  最终训练准确率：{train_accs[-1]:.2f}%")
    print(f"  最终训练损失：{train_losses[-1]:.4f}")
    
    return train_losses, train_accs

def evaluate_model(model, test_loader, device, class_names=['A', 'B', 'C', 'D', 'E']):
    """
    评估模型
    """
    model.eval()
    model.to(device)
    
    all_preds = []
    all_labels = []
    
    print("\n📊 评估模型...")
    
    with torch.no_grad():
        for batch_data, batch_labels in tqdm(test_loader, desc='Evaluating'):
            batch_data = batch_data.to(device)
            batch_labels = batch_labels.to(device)
            
            outputs = model(batch_data)
            _, predicted = torch.max(outputs.data, 1)
            
            all_preds.extend(predicted.cpu().numpy())
            all_labels.extend(batch_labels.cpu().numpy())
    
    # 计算准确率
    all_preds = np.array(all_preds)
    all_labels = np.array(all_labels)
    accuracy = np.mean(all_preds == all_labels)
    
    print(f"\n✅ 评估完成！")
    print(f"  测试准确率：{accuracy*100:.2f}%")
    
    # 各类别准确率
    print("\n  各类别准确率:")
    for i, class_name in enumerate(class_names):
        mask = all_labels == i
        if mask.sum() > 0:
            class_acc = np.mean(all_preds[mask] == all_labels[mask])
            print(f"    {class_name}: {class_acc*100:.2f}% ({mask.sum()} 样本)")
    
    return accuracy, all_preds, all_labels

def save_model(model, model_path="models/cnn_lstm_epilepsy.pth"):
    """
    保存模型
    """
    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    
    torch.save({
        'model_state_dict': model.state_dict(),
        'model_config': {
            'input_size': 4097,
            'num_classes': 5,
            'cnn_channels': 64,
            'lstm_hidden': 128
        }
    }, model_path)
    
    print(f"✅ 模型已保存：{model_path}")

def main():
    # 配置
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f"🔧 使用设备：{device}")
    
    # 加载数据
    data_dir = Path("datasets/processed")
    if not data_dir.exists():
        print("❌ 预处理数据不存在，请先运行 02_preprocess_data.py")
        return
    
    X_train = np.load(data_dir / "X_train.npy")
    X_test = np.load(data_dir / "X_test.npy")
    y_train = np.load(data_dir / "y_train.npy")
    y_test = np.load(data_dir / "y_test.npy")
    
    print(f"✅ 数据加载完成")
    print(f"  训练集：{X_train.shape}")
    print(f"  测试集：{X_test.shape}")
    
    # 转换为 PyTorch 数据集
    train_dataset = TensorDataset(
        torch.FloatTensor(X_train),
        torch.LongTensor(y_train)
    )
    test_dataset = TensorDataset(
        torch.FloatTensor(X_test),
        torch.LongTensor(y_test)
    )
    
    train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=32, shuffle=False)
    
    # 创建模型
    model = CNN_LSTM_Epilepsy(
        input_size=X_train.shape[1],
        num_classes=5,
        cnn_channels=64,
        lstm_hidden=128
    )
    
    print(f"\n🏗️  模型架构:")
    print(model)
    
    # 损失函数和优化器
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-4)
    
    # 训练
    train_losses, train_accs = train_model(
        model, train_loader, criterion, optimizer, device, epochs=50
    )
    
    # 评估
    accuracy, preds, labels = evaluate_model(model, test_loader, device)
    
    # 保存模型
    save_model(model)
    
    # 可视化训练过程
    plt.figure(figsize=(12, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(train_losses, 'b-', label='Training Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.legend()
    plt.grid(True)
    
    plt.subplot(1, 2, 2)
    plt.plot(train_accs, 'r-', label='Training Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy (%)')
    plt.title('Training Accuracy')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('models/training_history.png', dpi=300, bbox_inches='tight')
    print(f"\n📈 训练历史已保存：models/training_history.png")
    
    plt.show()

if __name__ == "__main__":
    main()
