A: float = 4.5
A0: float = 4.0
B: float = 3.5

python: int = 3
mobile: int = 2
excel: int = 1

avg: float = ((python * B) + (mobile * A0) + (excel * A)) / (python + mobile + excel)

print(f"퍙균 학점 : {round(avg, 1)}")