"""
<문제 첫 줄이 이해가 안 가더라 이말입니다>
1. input()은 표준 입력을 받음
  ㅇ=> a, b = map(int, "5 3".strip().split(' '))

2. strip()은 처음과 끝에 있는 공백문자를 제거함. input()에서 받은 값에 공백이 있을 경우를 위해 전처리를 해주는 것.
  ㅇ=> a, b = map(int, "5 3".split(' '))

3. split(' ')은 문자열을 공백을 기준으로 잘라줌. "5 3"을 공백기준으로 잘랐으니 ["5", "3"]을 리턴함
  ㅇ=> a, b = map(int, ["5", "3"])

4. map(int, ["5", "3"]) 은 리스트의 원소에 int를 취해, 문자열을 정수로 변환해줌.
  ㅇ=> a, b = [5, 3]

5. 마지막으로 남은 구문에서 unpacking을 적용해, a에는 5가 b에는 3이 할당됨.
"""

a, b = map(int, input().strip().split(' '))
for i in range (0, b):
    print("*"*a)



"""
<알게 된 것>
1. .strip()
    문자열의 맨 앞과 맨 뒤의 whitespace가 제거됨

2. .split()
    문자를 괄호 기반으로 잘라줌
    
3. map(함수, <iterable object>)
    입력받은 iterable object의 각 요솔르 함수로 수행된 결과로 묶어서 반환한다
"""