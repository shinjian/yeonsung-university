# continue문은 반복문의 남은 부분은 건너뛰고 반목문의 처음 부분으로 돌아가는 문장

i, hap = 0, 0

for i in range(1, 101, 1):
    if i % 4 == 0:
        continue

    hap += i

print(f"1~100까지의 합 (4의 배수 제외): {hap}")