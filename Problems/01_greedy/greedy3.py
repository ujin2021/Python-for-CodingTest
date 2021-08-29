# 실전문제 2. 숫자 카드 게임

'''
조건 : 각 행에서 가장 낮은 숫자를 뽑음 => 그것들 중 가장 큰 수를 찾기
입력 : 카드들이 놓인 행의 갯수 N x M (행 x 열), 카드에 적힌 숫자
출력 : 게임의 룰에 맞게 선택한 카드에 적힌 숫자 출력
'''

import sys

N, M = map(int, sys.stdin.readline().split())
minimum = []
for i in range(N) :
    minimum.append(min(list(map(int, sys.stdin.readline().split()))))
print(max(minimum))
    
