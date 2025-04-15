n = int(input("숫자 입력: "))

if (n > 100):
    if (n < 1000):
        print(f"{n}은 100보다 크고 1000보다 작다.")
    else:
        print(f"{n}은 1000보다 크거나 같다.")

else:
    print(f"{n}은 100보다 작거나 같다.")