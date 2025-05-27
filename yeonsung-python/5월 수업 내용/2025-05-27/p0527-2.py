# a = 10
# b = 20
# sum = a + b
# print(sum)

def sum_func(num1: int, num2: int) -> int:
    return num1 + num2

def sub_func(num1: int, num2: int) -> int:
    return num1 - num2

def div_func(num1: int, num2: int) -> int:
    return num1 / num2

def mul_func(num1: int, num2: int) -> int:
    return num1 * num2

print(sum_func(10, 20))
print(sub_func(10, 20))
print(div_func(10, 20))
print(mul_func(10, 20))