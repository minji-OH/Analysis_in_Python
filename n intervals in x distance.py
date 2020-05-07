"""
< 문제 분석 >
1. 정수 x, 자연수 n을 입력받음
2. x부터 시작해서 x씩 증가하는 숫자를 n개 지니는 리스트 리턴
3. x의 범위는 (-천만 ~ 천만), n은 천 이하의 자연수
"""
# 직관적으로 우다다다 풀음
def solution(x, n):
    answer = []

    for i in range(1, n+1):
        a = x*(i)
        answer.append(a)

    return answer