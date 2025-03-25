POUND_TO_KG: float = 0.453592
KG_TO_POUND: float = 2.204623

pound: float = float(input("파운드 입력: "))
print(f"{pound}는 {round(pound * POUND_TO_KG, 2)}kg")

kg: float = float(input("킬로그램 입력: "))
print(f"{kg}는 {round(kg * KG_TO_POUND, 2)}lb")