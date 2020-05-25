"""
<풀이>
1. 신청한 금액 배열 d를 오름차순 정리
2. budget에서 배열 d의 값을 하나씩 빼주고 answer에 1개씩 세어 줌
3. budget의 남은 금액이 배열 d값보다 작으면 멈추고 answer 출력
"""

def solution(d, budget):
    answer = 0
    d.sort()               #여기를 sorted(d) 로 하니까 실패 뜨던데...
    for i in d:            #왜 그런지 아시는 분?
        if i <= budget:
            budget -= i
            answer += 1
    return answer