"""
<접근>
1. ( 는 막대 또는 레이저의 시작
2. ) 는 막대 또는 레이저의 끝
3. ()는 레이저
4. 막대가 레이저를 만나면 [잘리는 막대의 수] = [이전에 잘린 막대 수] + [현재 막대 수]
5. 레이저를 만났을 때 [이전에 잘린 막대가 몇개]고
                   [현재 막대가 몇개]인지 알 수 있느냐가 중요!

<풀이>
1. ( 와 )가 막대인지 레이저인지 구분하는 코드를 짜는건 어떻게 해야할지 몰라... ()를 레이저로 바꿔줌
2. 레이저를 만나면 --> [잘리는 막대의 수] = [이전에 잘린 막대 수] + [현재 막대 수]
3. ( 를 만나면 -----> 현재 막대 1개 증가, 잘리는 막대의 수 1개 증가
3. ) 를 만나면 -----> 현재 막대 1개 감소, 작업 종료되는 막대 1개 증가
"""

# 처음 낸거
def solution(arrangement):
    answer = 0
    now = 0
    done = 0
    arr = arrangement.replace('()' ,'a')
    for i in range (len(arr)):
        if arr[i] == 'a':
            answer = answer + now
        elif arr[i] = ='(':
            now += 1
            answer += 1
        else:
            now -= 1
            done += 1
    return answer

# 최종 (생각해보니, done은 세 줄 필요가 없었음)
def solution(arrangement):
    answer = 0
    now = 0
    arr = arrangement.replace('()' ,'a')
    for i in range (len(arr)):
        if arr[i] == 'a':
            answer = answer + now
        elif arr[i] = ='(':
            now += 1
            answer += 1
        else:
            now -= 1
    return answer