"""
<접근>
1. arr1, arr2의 숫자를 2진수로 나타내기
2. arr1, arr2의 항목을 각각 비교하기
   1 + 1 -> 1
   1 + 0 -> 1
   0 + 1 -> 1
   0 + 0 -> 0
3. 문자열에서 1은 #로 바꾸고, 0은 공백으로 바꿔주기

<적용 방안>
1. bin() *문자열로 출력해줌 **0b로 시작하기 때문에 슬라이싱 해줘야 함
2. 비트연산자 활용
3. listname.replace()
"""

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip (arr1, arr2):                           #리스트에서 각각 항목 가져옴
        binary = bin(i|j)[2:]                               #2진수로 변환 + 비트연산자 사용 + 슬라이싱
        binary = '0'*(n-len(binary)) + binary               #사각형 변의 길이 n에 맞게 2진수의 자리수 맞춰줌
        binary = binary.replace('0', ' ').replace('1', '#') #0을 공백으로, 1을 #로 변환
        answer.append(binary)
    return answer


"""
<배운 것>
1. for 문에도 zip이 되는구나
2. 2진수로 바꾸는 방법
    >> 2진수로 바꾸면 '문자열'로 반환하는구나
3. 비트연산자
4. replace로 문자열 바꿀 수 있구나
    >> 근데 str.maketrans 랑은 무슨 차이인거지?
"""