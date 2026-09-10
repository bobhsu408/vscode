import random

def elementary_math_quiz():
    print("=" * 35)
    print("      歡迎來到國小數學挑戰賽！")
    print("=" * 35)
    
    score = 0
    total_questions = 5
    
    for i in range(1, total_questions + 1):
        op = random.choice(['+', '-', '*', '/'])
        
        # 根據運算符號隨機生成適合國小程度的數字
        if op == '+':
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            answer = a + b
            question_str = f"{a} + {b}"
        elif op == '-':
            a = random.randint(1, 50)
            b = random.randint(1, 50)
            if a < b:
                a, b = b, a  # 避免出現負數答案
            answer = a - b
            question_str = f"{a} - {b}"
        elif op == '*':
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            answer = a * b
            question_str = f"{a} × {b}"
        else:  # 除法
            b = random.randint(1, 9)
            multiplier = random.randint(1, 9)
            a = b * multiplier
            answer = multiplier
            question_str = f"{a} ÷ {b}"
            
        # 取得使用者輸入並防呆
        while True:
            try:
                user_input = input(f"\n第 {i} 題：{question_str} = ")
                user_answer = float(user_input)
                if user_answer.is_integer():
                    user_answer = int(user_answer)
                break
            except ValueError:
                print("⚠️ 請輸入有效的數字！")
        
        # 判斷對錯
        if user_answer == answer:
            print("答對了！太棒了！ 🎉")
            score += 1
        else:
            print(f"答錯囉～ 正確答案是 {answer} 💡")
            
    # 結算成績
    print("\n" + "=" * 35)
    print(f" 挑戰結束！你的總分是：{score} / {total_questions}")
    if score == total_questions:
        print(" 太神啦！完美滿分通關！ 🏆")
    elif score >= 3:
        print(" 做得很好！基礎很扎實！ 👍")
    else:
        print(" 別氣餒，多練習幾次就會更進步喔！ 💪")
    print("=" * 35)

if __name__ == "__main__":
    elementary_math_quiz()