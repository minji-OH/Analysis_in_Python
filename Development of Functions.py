"""
<접근 방법>
1. 각 기능의 진도가 100%를 처음으로 넘는 날(day)을 구한다.
2. 각각의 day를 비교해서 앞쪽의 비교 기준(head)이 배포될 때 뒤이어 몇 개까지 배포가 가능한지 생각한다
3. 그걸 코드로 짠다

<풀이>
1. 각 기능의 진도가 100%를 처음으로 넘는 날(day)은
   "(100-진도(progresses)) ÷ 개발속도(speeds)" 의 값을 "소수점 올림"해서 구함
   ==> 소수점 올림해주는 math 클래스의 ceil 함수 사용

2. 인덱스 [0]번부터 head(비교기준)로 설정
   (1) head가 바뀌는 시점은, head가 비교대상보다 작을 때 head를 비교대상으로 교체해야함
   (2) head가 교체될 때, 교체되는 head 앞에 있는 항목들은 같이 배포되는 애들들임
   (3) 그 애들의 개수를 세주기
   (4) 2-(3)를 answer 리스트에 추가

3. 마지막 head만 남았을 때, 마지막에 같이 배포되는 애들을 어떻게 세줄까?
   (1) 마지막 head가 남으면, 뒤에는 더이상 head보다 큰 값이 없음
   (2) 그러면 비교는 더이상 무의미
   (3) day의 배열길이에서 head의 인덱스 번호를 빼면 마지막 head가 배포될 때 같이 배포되는 애들의 개수가 나옴
   (4) 그 개수를 세주기
   (5) 3-(4)를 answer 리스트에 추가
"""

import math

def solution(progresses, speeds):
    answer = []
    day = [math.ceil((100-i)/j for i, j in zip(progresses, speeds)]
    head = 0
    for a in range (len(day)):
        if day[head]<day[a]:
            answer.append(a-head)
            head = a
    answer.append(len(day)-head)

    return answer



"""
<느낀점>
math 클래스.. 배우고 갑니다
"""