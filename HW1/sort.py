import re
import csv

input_file = 'result.txt'
output_file = 'result.csv'

# 讀取文本文件
with open(input_file, 'r', encoding='utf-8') as f:
    text = f.read()

# 使用正則表達式在每行文本的第一個數字後面添加逗號
text = re.sub(r'(\d+)\s', r'\1,', text)

# 將文本轉換為行列表
lines = text.strip().split('\n')

# 將每行文本轉換為列表
data = []
for line in lines:
    row = line.split(',')
    data.append(row)

# 將列表寫入CSV文件
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(data)

