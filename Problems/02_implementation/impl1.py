# 구현 예제1. 상하좌우

'''
조건 : 이동할 계획대로 이동, 만약 정사각형 공간을 벗어난다면 무시됨
입력 : 공간의 크기 N (전체 공간은 N x N), 이동할 계획 (R, U, D, L)
출력 : 이동 후 위치

시간 복잡도 : O(이동횟수)
'''

import sys

N = int(sys.stdin.readline())
go = sys.stdin.readline().split()

go_dict = {'R' : (0, 1), 'L' : (0, -1), 'U' : (-1, 0), 'D' : (1, 0)}
x, y = 1, 1
for g in go :
    go_x = go_dict[g][0]
    go_y = go_dict[g][1]
    if(x + go_x < 1 or x + go_x > N or y + go_y < 1 or go_y > N) :
        pass
    else :
        x += go_x
        y += go_y
print(f'{x} {y}')