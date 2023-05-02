import csv

# 讀取文件，將每行分割為數字和字符串
with open('result.csv', 'r') as f:
    lines = [line.strip().split(',', 1) for line in f]

# 將數字轉換為整數，並按照數字排序
sorted_data = sorted(lines, key=lambda x: int(x[0]))

# 寫入CSV文件
with open('result.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(sorted_data)

