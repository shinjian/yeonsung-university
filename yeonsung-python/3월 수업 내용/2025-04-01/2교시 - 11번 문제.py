num1: float = float(input("숫자1 입력: "))
num2: float = float(input("숫자2 입력: "))

print(f"""
{num1} / {num2} = {round(num1 / num2, 2)}
{num1} % {num2} = {num1 % num2}
{num1} // {num2} = {num1 // num2}
{num1} ** {num2} = {num1 ** num2}
""")