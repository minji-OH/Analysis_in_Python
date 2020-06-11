
#### 답안 1 __ 이런 코드 짜는 것도 대단해보임. 근데 이거 시간초과 (test 5 실패)
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec


#### 답안 2 __ deque 사용
from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 1
    dq = deque()  # [트럭무게, 다리를 지난 시간]
    dq.append([truck_weights[0], bridge_length])
    truck_weights.pop(0)

    while len(dq) != 0 and dq[0][1] != 0:
        temp = 0  # 다리를 다 건넌 트럭
        total_weight = 0  # 현재 다리에 있는 트럭들의 총 무게

        # dq에 있는 트럭들의 시간 -1
        for i in range(len(dq)):
            total_weight += dq[i][0]
            dq[i][1] -= 1
            if dq[i][1] == 0:
                temp += 1

        # 다리를 다 건넌 트럭만큼 지우기
        for i in range(temp):
            total_weight -= dq[i][0]
            dq.popleft()

        # (현재 다리에 있는 트럭들 무게 + 대기트럭)이 다리 무게보다 작으면 다리에 추가!
        if len(truck_weights) != 0 and total_weight + truck_weights[0] <= weight:
            dq.append([truck_weights[0], bridge_length])
            truck_weights.pop(0)

        answer += 1

        # print(answer, dq, truck_weights)

    return answer


#### 답안 3
def solution(bridge_length, weight, truck_weights):
    answer = 0
    curr_weight = 0
    st = truck_weights[::-1]   # 스택 생성
    q = []                     # 큐 생성
    dist = [0] * len(truck_weights) # 진행 거리 배열 생성

    # 마지막 트럭이 다리를 지날때까지 다음을 반복합니다.
    while st:
        # 1. 출발해야 할 트럭 top을 구합니다. 즉, st에서 데이터를 빼옵니다.
        top = st.pop()

        # 2. 현재 다리를 지나는 트럭들의 무게와, top의 무게를 더한 값이 weight보다 큰지 확인 합니다.
        # 2-1. 크다면, 현재 트럭은 다리를 지나지 않습니다. 다시 스택으로 되돌립니다.
        # 2-2. 그렇지 않다면, 트럭은 다리를 지납니다. 즉 큐에 데이터를 넣고 다리를 지나는 트럭의 무게를 더합니다.
        if curr_weight + top > weight:
            st.append(top)
        else:
            curr_weight += top
            q.append(top)

        # 3. 현재 다리에 들어선 트럭들을 움직입니다. 즉, 각 진행 거리를 나타내는 dist를 q의 길이만큼 순회하여 1씩 더해줍니다.
        for i in range(len(q)):
            dist[i] += 1

        # 4. 다리를 지난 트럭을 제거합니다. 진행 거리가, 입력 bridge_length보다 큰지 확인합니다.
        # 4-1. curr_weight에서 q의 첫 원소만큼 빼주고, q에서 그 데이터를 제거합니다.
        # 4-2. dist 역시 첫 원소를 제거해주어야 합니다.
        if dist[0] >= bridge_length:
            curr_weight -= q.pop(0)
            dist.pop(0)

        answer += 1

    # 5. 마지막 트럭의 진행한 거리를 구합니다.
    length = dist.pop()
    # 6. answer 에 마지막 트럭이 다리를 지나는 시간 (다리 길이 - 현재 진행한 길이 + 1)을 더합니다.
    answer += (bridge_length - length + 1)
    return answer