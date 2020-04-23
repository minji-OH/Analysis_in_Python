def solution(s):
    answer = ''
#대소문자 구분하기
    lower = []
    upper = []
    for i in range(len(s)):
        if s[i] >='a' and s[i] <='z':
            lower.append(s[i])
        else:
            upper.append(s[i])
#각각 정렬
    lower.sort(reverse=True)
    upper.sort(reverse=True)

#조인
    answer = ''.join(lower) + ''.join(upper)
    return answer