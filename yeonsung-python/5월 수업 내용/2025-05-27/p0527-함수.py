# 중복되는 코드를 사용자 정의 함수로 구현

# 사용자 정의 함수 정의부
def sum_func() -> int:
    n1 = int(input("정수1 : "))
    n2 = int(input("정수2 : "))

    return n1 + n2

print(f"합 : {sum_func()}")