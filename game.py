import random

a = random.randint(1, 50)
b = random.randint(1, 50)

print(f"{a} + {b} = ?")
answer = int(input("你的答案："))

if answer == a + b:
    print("答對了！🎉")
else:
    print(f"答錯囉～ 正確答案是 {a + b}")
