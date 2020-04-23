def solution(strings, n):
    answer = []

# 인덱스 n번째 문자를 문자열 맨 앞에 붙여줌
	for i in range(len(strings)):
		strings[i] = strings[i][n]+strings[i]

# 리스트 안의 문자열을 오름차순으로 정렬함
	strings.sort()

# 인덱스 0번째 문자를 빼고 나머지를 가져옴
	for j in range(len(strings)):
		answer.append(strings[j][1:])

	return answer
