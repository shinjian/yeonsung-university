# 6장 반복문

for i in range(3):
    print(f"i = {i}")

# range(0, 3, 1)에서 첫 인수가 0이고 세 번째 인수가 1이면 range(3)으로 줄여 쓸 수 있다.
# 0부터 3 이전 숫자인 2까지 1씩 증가
for i in range(0, 3, 1):
    print(f"i = {i}")

# for 루프 변수 in range(start, end, step): end-1까지
for i in range(1, 10, 2):
    print(f"i = {i}")

# 리스트를 이용한 반복문 => 리스트 : 대괄호 사용
for i in [0, 1, 2]:
    print(f"i = {i}")