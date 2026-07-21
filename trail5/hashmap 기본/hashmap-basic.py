import sys

def solve():
    input = sys.stdin.readline

    # n: 명령어의 개수
    n = int(input())

    # 해시맵으로 사용할 딕셔너리 생성
    hashmap = {}

    for _ in range(n):
        command = input().split()
        op = command[0]

        if op == "add":
            k, v = int(command[1]), int(command[2])
            hashmap[k] = v

        elif op == "remove":
            k = int(command[1])
            # key가 존재할 때만 삭제 (KeyError 방지)
            if k in hashmap:
                del hashmap[k]

        elif op == "find":
            k = int(command[1])
            # key가 존재하면 해당 value 출력, 없으면 None 출력
            if k in hashmap:
                print(hashmap[k])
            else:
                print("None")

if __name__ == '__main__':
    solve()