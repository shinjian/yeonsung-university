num1: float = float(input("첫번째 숫자 입력: "))
num2: float = float(input("두번째 숫자 입력: "))

print(f"""
{num1} + {num2} = {num1 + num2}
{num1} - {num2} = {num1 - num2}
{num1} * {num2} = {num1 * num2}
{num1} / {num2} = {num1 / num2}
{num1}를 {num2}로 나눈 나머지 = {num1 % num2}
{num1}의 {num2}승 = {num1 ** num2}
""")