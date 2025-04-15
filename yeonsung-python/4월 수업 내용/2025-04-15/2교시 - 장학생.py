import random

# 0~100 사이 랜덤 점수
score = random.randint(0, 100)
print(f"뽑힌 점수 : {score}")

# 결과 판별
if score >= 90:
    print("장학생입니다.")
elif score >= 60:
    print("합격입니다.")
else:
    print("불합격입니다.")