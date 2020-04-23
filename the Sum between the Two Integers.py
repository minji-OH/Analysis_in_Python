def solution(a, b):
# a와 b 중 a를 큰 수로 놓기 위한 방법
    if b > a:
        tmp = a
        a = b
        b = tmp

# 가우스의 덧셈법칙 활용
    answer = (a + b) * (a - b + 1) / 2
    return answer