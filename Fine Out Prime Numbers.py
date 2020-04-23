def solution(n):
    answer = 0
    numbers = []

# 인덱스 번호와 자연수 맞추기
    for i in range(n+1):
        numbers.append(i)

# 차례대로 배수를 '-1'로 바꾸기 (소수가 아닌 것은 '-1'로 바꿈)
    for i in range(2, n+1, 1):
        if i == -1:
            continue
        j = 0
        for j in range(i+i, n+1, i):
            numbers[j] = -1

# 리스트'numbers'에서 소수만 찾아 'answer'에 더하기
    for i in range(2, n+1):
        if numbers[i] != -1:
            answer += 1

    return answer

"""
>> 더 알아봐야 하는 것
1. 차집합을 사용할 수도 있다.
2. 제곱근을 사용하면 처리속도가 더 빨라진다."""