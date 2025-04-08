# 자동으로 줄바꿈
print("Hello")
print("Python")

# 형식 지정자를 사용하여 출력
# %d : 정수, %s : 문자열, %f : 실수, %c : 문자
print("100")
print("%d" % 100)

print("100 + 100")
print("%d" % (100 + 100))

# 정수 형식 지정자 %d => int
print("%d %d %d" % (100, 200, 300))
print("%5d %5d %5d" % (100, 200, 300))
print("%05d %05d %05d" % (100, 200, 300))
print("%-5d %-5d %-5d" % (100, 200, 300))

# 실수 형식 지정자 %f => float
print("%f" % 123.45)
print("%7.1f" % 123.45)
print("%7.3f" % 123.45)

# 문자열 형식 지정자 %s => str
print("%s" % "Python")
print("%10s" % "Python")
print("%-10s" % "Python")