# 실전문제1. 큰수의 법칙
# 풀이 1

'''
문제 : 입력으로 주어진 수들을 M번 더하여 가장 큰 수를 만들기

조건 : 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없음, 수가 같지만 인덱스가 다르면 다른 것으로 간주
입력 : 배열의 크기 N, 숫자가 더해지는 횟수 M, K, 숫자배열
출력 : 큰수
'''

import sys

N, M, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
num = sorted(num, reverse=True)

count = 0 # 제일 큰 수를 연속해서 몇번 더했는가
answer = 0
for i in range(M) :
    if(count == K) : # 연속해서 K번을 더했다면 두번째로 큰수를 더한다
        count = 0
        answer += num[1]
        continue
    answer += num[0]
    count += 1

print(answer)

