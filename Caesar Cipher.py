"""
1. 문자열 s 를 하나하나씩 쪼개서 리스트(answer)로 만들어줌 -> str에 list()를 씌우면 된다는군...!
2. 리스트(answer)에서 하나씩 차례대로 알파벳을 조건에 맞게 바꿔줌
   - 알파벳에 각각 숫자가 대응된다는 개념 사용(아스키코드)
   - 알파벳을 숫자로 바꿀 때는 ord('알파벳')
   - 숫자를 알파벳으로 바꿀 때는 chr('숫자')
   - 대문자, 소문자 구분해줄 필요 있음  -> str.isupper() 구문: 모든 문자의 문자열이 대문자인지 판단
                                      str.islower() 구문: 모든 문자의 문자열이 소문자인지 판단
   - 'Z'→'A'로 넘어가고, 'z'→'a'로 넘어가는 구간을 잘 계산해야 함
"""


def solution(s, n):
    answer = list(s)
    for i in range(len(answer)):
        if answer[i].isupper():
            answer[i] = chr((ord(answer[i]) + n - ord('A')) % 26 + ord('A'))
        elif answer[i].islower():
            answer[i] = chr((ord(answer[i]) + n - ord('a')) % 26 + ord('a'))

    return "".join(answer)