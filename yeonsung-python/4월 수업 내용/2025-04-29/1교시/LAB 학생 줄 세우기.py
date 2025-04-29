fact = 1
fnum = int(input("학생 수 입력 : "))

print(fnum)

for i in range(fnum):
    fact *= i + 1

print(f"A, B, C, D, E 학생들을 순서대로 세우는 경우의 수 : {fact}")