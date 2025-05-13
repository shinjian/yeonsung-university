start: int = int(input("시작값: "))
end: int = int(input("끝값: "))

step: int = int(input("증가값: "))

total = 0

for i in range(start, end+1, step):
    total += i

print(total)