# greedy 예제 1

'''
조건 : 500원, 100원, 50원, 10원 동전이 무한히 존재
입력 : 손님에게 거슬러 줘야 할 돈 N원 (N은 10의 배수)
출력 : 거슬러 줘야 할 동전의 최소 갯수
'''
def solution(n) :
    answer = 0
    coin = [500, 100, 50, 10]
    for i in coin :
        answer += n // i
        n %= i
        
    return answer

print(solution(1260) == 6)