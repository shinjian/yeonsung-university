# 물품 가격 정보: name: (구입가, 판매가)
prices = {
    "캔커피": (500, 1800),
    "삼각김밥": (900, 1400),
    "바나나맛 우유": (800, 1800),
    "도시락": (3500, 4000),
    "콜라": (1500, 2000),
    "새우깡": (700, 1000)
}

# 거래 내역: (상품명, 구입/판매, 수량)
transactions = [
    ("삼각김밥", "구입", 10),
    ("바나나맛 우유", "판매", 2),
    ("도시락", "구입", 5),
    ("도시락", "판매", 4),
    ("콜라", "판매", 1),
    ("새우깡", "판매", 4),
    ("캔커피", "판매", 5)
]

# 매출 계산
total = 0
for name, action, qty in transactions:
    purchase, sale = prices[name]
    price = sale if action == "판매" else -purchase
    total += price * qty

print(f"오늘 총 매출액은 {total} 원입니다")