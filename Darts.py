"""
1. dartResult 로 들어오는 문자열을 "점수|보너스|[옵션]"으로 잘 나눠야함.
2. (점수^보너스) * (옵션) 의 구조로 수식을 만들면 될 것 같음
3. 있을 수도 있고 없을 수도 있는 [옵션]을 어떻게 처리한담....

하나도 모르겠어서 구글링한 것 중 제일 좋아보이는 모범답안을 공부하기로 결정
"""
####### 모범답안 1

#파이썬 내장 Module인 re (=정규표현식, Regural Expression)
import re

def solution(dartResult):
# (\d+)         1개 이상의 숫자에 대응 (+, 한 개 이상의 임의 문자)
# ([a-zA-Z])    알파벳 하나에 대응
# (\*|#)?       * 혹은 # 라는 뜻 (|, or) (?, 0개 또는 1개의 임의문자)
# re.compile()  정규식 패턴을 입력으로 받아들여 정규식 객체를 리턴함
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
# .findall()  정규식과 매치되는 모든 문자열(substring)을 리스트로 돌려줌
# 그래서 score는 [('1', 'S', ''), ('2', 'D', '*'), ('3', 'T', '')]가 됨
    scores = p.findall(dartResult)
# 각각의 기회에서 얻은 점수를 리스트(result)로 반영함
    result = []
# enumerate 함수는 순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려줌
# for문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려 주는 인덱스 값이 필요할 때 enumerate 함수가 유용하게 쓰임
    for i, score in enumerate(scores):
        point = score[0]
        bonus = score[1]
        option = score[2]
# 영역의 제곱수를 매칭함
        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3
# 옵션'*'의 역할을 지정함
        if option == '*':
# 첫 번째 기회에서 스타상이 나올 경우
            if i == 0:
                result.append(int(point)**bonus*2)
# 2번째, 3번째 기회에서 스타상이 나올 경우
            else:
                result[-1] *= 2
                result.append(int(point)**bonus*2)
# 옵션'#'의 역할을 지정함
        elif option == '#':
            result.append(int(point)**bonus*-1)
# 옵션이 없을 경우
        else:
            result.append(int(point)**bonus)
# 각각의 기회에서 얻은 점수를 합함
    return sum(result)



####### 더 깔끔한 모범답안 2

import re

def solution(dartResult):
#보너스와 옵션을 딕셔너리로 만들어줌
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
# (\d+)       1개 이상의 숫자에 대응
# ([SDT])     SDT 중 하나에 대응
# ([*#])?     *, # 중에 하나에 대응 (?, 0개 또는 1개의 임의 문자)
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
# 2번째, 3번째 기회에서 스타상이 나올 경우
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
# 각각의 기회에서의 점수를 보너스제곱 하고 옵션을 곱해줘서 리스트(dart)값을 바꿔줌
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]
# 각각의 기회에서 얻은 점수를 합함
    answer = sum(dart)
    return answer


"""
>>>느낀점
1. 정규표현식
  : 예전에 김박사님이 마크베이스에서 센서데이터 가져오는 거 설명해주실 때 정규표현식 공부하라고 하셨는데ㅋㅋ
  
2. enumarate
  : 세 번째로 뵙는 분인데ㅎㅎ 이제는 반가운 분이네.. 나도 활용하고싶다
  
3. compile(souce, filename, mode, flags=0, dont_inherit=False, optimize=-1)
  : 누구냐 넌..(한글 뜻: 엮다)
  ㅁ source를 코드 또는 AST 객체로 컴파일한다
  ㅁ filename은 코드를 읽은 카일을 넣는다
  ㅁ mode는 컴파일하는 코드의 종류를 지정한다
  ㅁ flags나 dont_ingerit 으로 컴파일을 제어할 수 있다
  ㅁ optimize로 컴파일러의 최적화 수준을 지정할 수 있다
  
4. 인간의 사고과정을 어떻게 컴퓨터프로그래밍 언어로 다들 잘 바꿀까? 부럽다
"""