##### 1번째 시도 --> 예제에서 3의 배수에서 오류

def solution(n):
    answer = ''
    while n > 0:
        answer = '412'[n%3] + answer
        n //= 3
    return answer


##### 2번째 제출 --> 예제에서 어떤 3의 배수는 통과하고
#####              어떤 3의 배수는 통과 못함
def solution(n):
    answer = ''
    if n%3 !=0:
        while n > 0:
            answer = '412'[n%3] + answer
            n //= 3
    else:
        n -= 1
        while n > 0:
            answer = '214'[n%3] + answer
            n //= 3
    return answer


##### 3번째 제출 --> 예제는 통과하는데 채점은 실패 뜸
def solution(n):
    answer = ''
    if n%3 !=0:
        while n > 0:
            answer = '412'[n%3] + answer
            n //= 3
    else:
        while n > 0:
            n -=1
            answer = '124'[n%3] + answer
            n //= 3
    return answer


##### 4번째 제출 --> 완성 !!!!
def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer