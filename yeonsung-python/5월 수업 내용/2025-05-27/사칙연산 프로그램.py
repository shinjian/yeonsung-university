def calc(v1: int, v2: int, op: str) -> float:
    match op:
        case '+':
            return v1 + v2
        case '-':
            return v1 - v2
        case '*':
            return v1 * v2
        case '/':
            if v2 == 0:
                raise ValueError("0으로 나눌 수 없습니다.")
            return v1 / v2
        case _:
            raise ValueError("지원하지 않는 연산자입니다.")

while True:
    oper = input("연산자 입력(+,-,*,/) : ")

    if oper == 'q':
        break

    var1 = int(input("정수1 입력 : "))
    var2 = int(input("정수2 입력 : "))

    result = calc(var1, var2, oper)
    print(f"계산({oper}) 결과 {result}")

print("프로그램 종료")