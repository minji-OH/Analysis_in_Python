# 1. 실패작(실행은 되는데 시간오류(초과)로 틀림

def solution(array, commands):
    answer = []
    i1 = commands[0][0]
    j1 = commands[0][1]
    k1 = commands[0][2]

    i2 = commands[1][0]
    j2 = commands[1][1]
    k2 = commands[1][2]

    i3 = commands[2][0]
    j3 = commands[2][1]
    k3 = commands[2][2]

    list1 = array[i1-1:j1]
    list1.sort()
    answer.append(list1[k1-1])

    list2 = array[i2-1:j2]
    list2.sort()
    answer.append(list2[k2-1])

    list3 = array[i3-1:j3]
    list3.sort()
    answer.append(list3[k3-1])

    return answer


# 2. 위의 코드를 for문으로 재작성....했는데 ~sort~부분이 틀렸다고 나옴

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sort(array[i - 1:j])[k - 1])
    return answer

# 3. 두 번째 코드에서 sort를 sorted로 바꿔봄....정답

def solution(array, commands):
    answer = []
    for i, j, k in commands:
        answer.append(sorted(array[i - 1:j])[k - 1])
    return answer

"""
>>>sort 함수
ㅁ 형태: listname.sort()
ㅁ 구분: 리스트형의 메소드
ㅁ 기능:리스트 원본값을 직접 수정하고 반환 값은 none 임
ㅁ 원본 리스트 값이 정렬된 값으로 수정되어 원본이 변함

>>>sorted 함수
ㅁ 형태: sorted(listname)
ㅁ 구분: 내장함수
ㅁ 기능: 리스트 원본 값은 그대로이고 정렬 값을 반환함
          원본 리스트 값이 유지되고 정렬된 리스트는 새 리스트에 저장됨
          모든 iterable에 동작함 (list, tuple, dict, 문자열 등)

* listname.sort()는 새로운 복사본을 만들지 않기 때문에 sorted(listname)보다 처리속도가 빠르다 함
"""