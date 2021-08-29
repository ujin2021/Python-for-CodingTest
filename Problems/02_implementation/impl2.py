# 구현 예제2. 시각

'''
조건 : 00시 00분 00초 부터 N시 59분 59초까지 모든 시각 중 3이 하나라도 포함되어야 함
입력 : 정수 N (0 <= N <= 23)
출력 : 3이 포함되는 경우의 수
'''

import sys

N = int(sys.stdin.readline())
count = 0
for h in range(N + 1) :
    for m in range(60) :
        for s in range(60) :
            t = str(h) + str(m) + str(s)
            if('3' in t) :
                count += 1
print(count)

# 내가 풀고싶은 방법
# hh mm ss -> 경우의 수로