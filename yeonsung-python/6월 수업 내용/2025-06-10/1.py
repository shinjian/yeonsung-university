# 리스트를 이용한 고객정보, 진료과정보, 약국정보, 편의시설정보를 입력
# 딕셔너리 member_list, medical_loaction, drugstore_list, facilities_list
member_list = {
    "1111": ["12보3456", 7890],
    "1112": ["356구7890", 7890],
    "1113": ["789라0123", 0],
    "1114": ["", 0]
}
medical_location = {
    "호흡기내과": "1층 3구역",
    "신장내과": "1층 9구역",
    "안과": "2층1구역"
}
drugstore_list = {
    "연세약국": "연세빌딩 1층 5",
    "열린약국": "DK빌딩 2층 3",
    "온누리약국": "누리빌딩 1층 1-1",
    "삼성약국": "에스에스빌딩 1층 3"
}
facilities_list = {
    "B2": ["주차장", "의료기기", "종교관"],
    "B1": ["편의점", "한정식", "카페"],
    "1": {"안경점"}
}

def escort():
    pass

def medical_department():
    print("선택 : 호흡기내과/신장내과/안과")
    md = input("방문할 진료과를 입력하십시오. : ")

    print(f"{md}위치 : {medical_location[md]}")

    ask = input("에스코드할까요(Y/N)? ")
    if ask == 'Y':
        escort(md)

def parking():
    member = input("고객번호를 입력하세요. : ")

    if member in member_list.keys():
        number = input("차량번호를 입력하세요. : ")
        member_list[member][0] = number

        print("등록되었습니다.")
        print(member_list)
    else:
        print("회원이 아닌 경우 등록할 수 없습니다.")

def payment():
    member = input("고객번호를 입력하세요. : ")
    
    if member in member_list.keys():
        expenses = member_list[member][1]

        print(f"{expenses}가 결제되었습니다.")
        member_list[member][1] = 0

        print(">>> 처리 결과 <<<")
        print(member_list)
    else:
        print("결제 금액을 조회할 수 없습니다.")

def drug_store():
    print("선택 : 연세약국/열린약국/온누리약국/삼성약국")
    ds = input("약국 이름을 입력하세요. : ")
    print(f"{ds}의 위치 : {drugstore_list[ds]}")

def facilities():
    for floor, shop in facilities_list.items():
        print(f"{floor}층 : ", end='')
        for s in shop:
            print(s, end='')
        print()

def menu():
    print("-"*30)
    print("1. 진료과 찾기")
    print("2. 주차 등록")
    print("3. 진료비 결제")
    print("4. 약국 찾기")
    print("5. 편의시설")
    print("-"*30)

while True:
    menu()
    select = input("메뉴에서 선택할 번호를 입력하세요. : ")

    if select == '1':
        medical_department()
    elif select == '2':
        parking()
    elif select == '3':
        payment()
    elif select == '4':
        drug_store()
    elif select == '5':
        facilities()
    else:
        print("잘못입력하셨습니다.")

    start = input("시작으로 가려면 enter키를 누르세요. : ")
    if start == 'q':
        break

print("시스템을 종료합니다..")