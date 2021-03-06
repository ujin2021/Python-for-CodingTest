# 구현 실전문제1. 왕실의 나이트

'''
조건 : 체스판은 8 x 8, 나이트 이동시 L자 형태로만 가능, 정원밖으로 나갈 수 없음
        이동 : 1. 수평으로 두칸 이동 후, 수직으로 한칸 2. 수직으로 두칸 이동 후 수평으로 한칸
입력 : 나이트의 위치 (행 : 1 ~ 8, 열 : a ~ h)
출력 : 나이트가 이동할 수 있는 경우의 수
'''

import sys

n = sys.stdin.readline()

col = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6, 'g' : 7, 'h' : 8}
# move = [(0, -1), (0, 1), (-1, 0), (1,0)] # 왼, 오, 위, 아래

# # 왼왼위, 왼왼아, 오오위, 오오아, 아아왼, 아아오, 위위오, 위위아
# rule = [(0, 0, 2), (0, 0, 3), (1, 1, 2), (1, 1, 3), (3, 3, 0), (3, 3, 1), (2, 2, 0), (2, 2, 1)]

# move + rule을 합쳐서 => 결국 최종 목적지에 도착할 수 있는지 없는지. 과정은 안중요함
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

now = (col[n[0]], int(n[1])) # 현재 위치 좌표
count = 0 # 가능한 경우의 수
for s in steps :
    x, y = now[0] + s[0], now[1] + s[1]
    possible = True
    if(x < 1 or x > 8 or y < 1 or y > 8) :
        continue
    count += 1
print(count)