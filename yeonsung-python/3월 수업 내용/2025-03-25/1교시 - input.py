# num1: int = int(input("첫번째 숫자 입력: "))
# num2: int = int(input("두번째 숫자 입력: "))

# print(num1 + num2)

# username = input("이름: ")
# phone = input("전화번호: ")

# print(f"제 이름은 {username}이고, 전화번호는 {phone} 입니다.")

recipient: str = input("받는 사람: ")
address: str = input("주소: ")
weight: float = float(input("무게(g): "))

shipping_fee: int = int(weight * 5)

print(f"""
** 받는 사 람 : {recipient}
** 주소      : {address}
** 배송비    : {shipping_fee}원
""")