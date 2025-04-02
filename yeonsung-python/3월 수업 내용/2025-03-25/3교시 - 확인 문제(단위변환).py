POUND_TO_KG = 0.453592
KG_TO_POUND = 2.204623

def pound_to_kg(pound: float) -> float:
    return round(pound * POUND_TO_KG, 2)

def kg_to_pound(kg: float) -> float:
    return round(kg * KG_TO_POUND, 2)

pound = float(input("파운드 입력: "))
print(f"{pound}lb 는 {pound_to_kg(pound)}kg 입니다.")

kg = float(input("킬로그램 입력: "))
print(f"{kg}kg 는 {kg_to_pound(kg)}lb 입니다.")