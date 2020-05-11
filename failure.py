"""
< 문제 조건 >
1. 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
2. stages에는 1~N+1 이하의 자연수 담김
   (즉, 201이 담겨있으면 200까지 깼고, 201에 도달해서 201을 도전 중라는 것)
3. 스테이지에 도달한 유저가 없으면 해당 스테이지의 실패율은 0
4. 실패율이 높은 스테이지부터 정렬 but 실패율이 같은 스테이지라면 작은 번호의 스테이지가 먼저 옴
   (즉, 실패율 내림차순 정렬 → 스테이지 오름차순 정렬)

< 풀이 접근 >
1. n단계 실패율 = n단계 스테이지에 도달한 사용자 수 / n단계 이상 스테이지에 도달한 플레이어 수
   (분자) => len(stages)
   (분모) => 전체 - 앞단계 도달한 이용자 수
2. collections.counter 를 쓸지 or dictionary 를 쓸지..?

"""

# collections 모듈 사용하고 정렬 잘 해주면 될 것 같은데..모르겠다ㅠ___ㅠ
# 그냥 dictionary만 쓰고, collections는 다음에 사용해보기ㅠㅠ
def solution(N, stages)
    answer = {}
    totalNum = len(stages)


    for i in range(1, N+1):
        if totalNum !=0:
            k = stages.count(i)        # i단계 스테이지 도전 중인 사용자 수 k
            answer[i] = k / totalNum   # 정의된 실패율 계산
            totalNum -= k              # [전체 이용자수]에서 [앞단계 도달한 이용자 수] 제거
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: answer[x], reverse = 1)


"""
< reflection >
collections 를 사용한 모범답안 없는지 찾아보고 코딩 분석해보기
"""