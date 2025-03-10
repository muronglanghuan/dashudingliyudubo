import random
import matplotlib.pyplot as plt

# 设置参数
p_win = 18/38  # 获胜概率（红色）
win_amount = 1   # 获胜收益（净赚1元）
loss_amount = -1  # 失败亏损（净亏1元）
expected_value = (p_win * win_amount) + ((1 - p_win) * loss_amount)  # 期望值计算
num_trials = 10000  # 模拟次数

# 初始化变量
total_profit = 0
averages = []

# 执行模拟
for trial in range(1, num_trials + 1):
    # 模拟单次赌博结果
    if random.random() < p_win:
        result = win_amount
    else:
        result = loss_amount
    
    total_profit += result
    current_avg = total_profit / trial
    averages.append(current_avg)

# 可视化结果
plt.figure(figsize=(10, 6))
plt.plot(averages, label='实际平均收益')
plt.axhline(expected_value, color='red', linestyle='--', label='理论期望值')
plt.xlabel('试验次数', fontsize=12)
plt.ylabel('平均收益', fontsize=12)
plt.title('大数定律在赌博中的验证（轮盘赌红色下注）', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# 输出最终结果对比
print(f'理论期望值: {expected_value:.4f}')
print(f'实际平均收益: {averages[-1]:.4f}')
print(f'差值: {abs(averages[-1] - expected_value):.4f}')
