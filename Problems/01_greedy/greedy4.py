# 실전문제 3. 1이 될 때 까지

'''
조건 : N이 1이 될 때 까지 1. N에서 1빼기 2. N을 K로 나누기(나눌 수 있을때만)
입력 : N, K (N은 항상 K보다 크거나 같다)
출력 : 조건에서 1, 2 를 수행할 때, 수행횟수의 최소값

=> '최대한 많이 나누기'
'''

import sys, math

N, K = map(int, sys.stdin.readline().split())

# 빼거나 K로 나눈 수가 K의 n승이 되어야 함
# print(int(math.log(N, K)) + N - K ** (int(math.log(N, K)))) => 25, 3일때 답: 6 / print : 18

count = 0

while N > 1 :
    if(N % K == 0) :
        N //= K
    else :
        N -= 1
    count += 1
print(count)

