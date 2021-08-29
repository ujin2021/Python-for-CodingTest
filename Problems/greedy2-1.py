# 실전문제1. 큰수의 법칙
# 풀이 2

import sys

N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num = sorted(num, reverse=True)
max_num, max_num2 = num[0], num[1]


print(M // (K + 1) * max_num * K + M % (K + 1) * max_num2 + M // (K + 1) * max_num2)

# ( (큰수) * K + 작은수 ) 한세트
# M // (K + 1) 

'''
만약에 M = 8, K = 3
M // (K + 1) 번 (큰 + 큰 + 큰 + 작) 이 반복
따라서 M // (K + 1) * K 번 큰 이 더해진다

M // (K + 1) 번 (큰 + 큰 + 큰 + 작)이 반복
따라서 M // (K + 1) 번 작 이 더해진다

만약에 나눈 후 나머지는 작 의 몫
따라서 M % (K + 1) 만큼 작 이 더해진다

따라서 
큰 : M // (K + 1) * K
작 : M % (K + 1) + M // (K + 1)

'''