def is_leap_year(year: int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# 사용자 입력
year = int(input("연도를 입력 ==> "))

# 결과 출력
print("윤년 입니다" if is_leap_year(year) else "평년 입니다")