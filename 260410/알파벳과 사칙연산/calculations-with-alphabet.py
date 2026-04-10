import sys

expression = input().strip()

# 1. 식에 등장하는 고유한 알파벳만 추출하여 리스트로 저장
unique_alphas = list(set(char for char in expression if char.isalpha()))
num_alphas = len(unique_alphas)

max_num = -float('inf')

# 알파벳에 할당된 숫자를 기록할 딕셔너리
alpha_to_num = {}

# 식 계산 함수 (왼쪽에서 오른쪽으로 순차적 계산)
def cal_nums():
    # 현재 alpha_to_num에 할당된 숫자를 바탕으로 수식 구성
    num_expr = []
    for char in expression:
        if char.isalpha():
            num_expr.append(alpha_to_num[char])
        else:
            num_expr.append(char)
            
    # 앞에서부터 순서대로 연산 수행
    res = num_expr[0]
    for i in range(1, len(num_expr), 2):
        op = num_expr[i]
        nxt = num_expr[i+1]
        
        if op == '+':
            res += nxt
        elif op == '-':  # 기존 '0'으로 되어 있던 오류 수정
            res -= nxt
        elif op == '*':
            res *= nxt
            
    return res

# 고유 알파벳 단위로 숫자를 부여하는 백트래킹
def assign_nums(idx):
    global max_num
    
    # 모든 고유 알파벳에 숫자를 다 할당했다면 수식 계산
    if idx == num_alphas:
        max_num = max(max_num, cal_nums())
        return

    # 현재 순서의 고유 알파벳
    current_alpha = unique_alphas[idx]
    
    # 1부터 4까지의 숫자를 동일한 알파벳에 일괄 할당
    for i in range(1, 5):
        alpha_to_num[current_alpha] = i
        assign_nums(idx + 1)

# 0번째 고유 알파벳부터 할당 시작
assign_nums(0)

# 최댓값 출력
print(max_num)