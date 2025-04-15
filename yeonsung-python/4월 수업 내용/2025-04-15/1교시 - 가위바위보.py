import random as ran

rules = {
    "가위": "보",
    "바위": "가위",
    "보": "바위"
}

def get_result(player: str, computer: str) -> str:
    if player == computer:
        return "무승부"
    elif rules[player] == computer:
        return "승리"
    else:
        return "패배"
    
player = input("가위바위보 입력: ")
computer = ran.choice(["가위", "바위", "보"])

print(f"컴퓨터 : {computer}")

print(f"결과 : {get_result(player=player, computer=computer)}")