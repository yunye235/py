# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")
# test_demo.py
a = 10
b = 20
c = a + b
print(f"10 + 20 = {c}")

# 新增运算
d = b - a
print(f"20 - 10 = {d}")

e = a * b
print(f"10 * 20 = {e}")

f = b / a
print(f"20 / 10 = {f}")

msg = "Hello Python!"
print(msg)

for i in range(3):
    print(f"循环输出：{i}")

# 新增 if 判断
num = 15
if num > 10:
    print(f"{num} 大于10")
else:
    print(f"{num} 小于等于10")

# 新增列表
my_list = [2, 4, 6, 8]
print("列表内容：", my_list)
for item in my_list:
    print(f"列表元素：{item}")

# while循环
count = 1
print("while循环：")
while count <= 3:
    print(f"count = {count}")
    count = count + 1

print("测试执行完成")
