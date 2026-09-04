# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding="utf-8")

# test_demo.py
print("==== Python环境测试 ====")
a = 10
b = 20
c = a + b
print(f"10 + 20 = {c}")

msg = "Hello Python!"
print(msg)

for i in range(3):
    print(f"循环输出：{i}")

print("测试执行完成")
