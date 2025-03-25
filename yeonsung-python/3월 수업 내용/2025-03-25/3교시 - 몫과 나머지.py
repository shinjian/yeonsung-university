num1: float = float(input("숫자1 입력: "))
num2: float = float(input("숫자2 입력: "))

# num1 나누기 num2
# num1을 num2로 나눈 몫
# num1을 num2로 나눈 나머지
# num1의 num2승

print(f"""
{num1} / {num2} = {round(num1 / num2, 2)}
{num1} // {num2} = {round(num1 // num2, 2)}
{num1} % {num2} = {round(num1 % num2, 2)}
{num1} ** {num2} = {round(num1 ** num2, 2)}
""")