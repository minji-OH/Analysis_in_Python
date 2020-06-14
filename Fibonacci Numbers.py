#### 풀이 1. 알고리즘 책에서 배운 거 적용해서 예제는 통과했지만
####        채점 시 런타임 에러 뜸
def solution(n):
    def fib(n):
        if n==1 or n==2:
            return 1
        return fib(n-1) + fib(n-2)
    answer = fib(n) % 1234567
    return answer

#### 풀이 2.
def solution(n):
    a = 0
    b = 0
    c = 1
    for i in range(n):
        a = b
        b = c
        c = a+b
    return (b%1234567)