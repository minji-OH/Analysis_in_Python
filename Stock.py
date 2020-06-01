#[정답]
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)-1):
        for j in range(i, len(prices)-1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    return answer

#[오답]
#결과값 [4, 3, 2, 1, 0] 나옴... 기대값은 [4, 3, 1, 1, 0]인데
def solution2(prices):
    answer = []
    for i in range(len(prices)-1):
        for j in range(i, (len(prices)-1)):
            if prices[i] > prices[j]:
                answer.append(len(prices)-1-j)
            else:
                answer.append(len(prices)-1-i)
            break
    answer.append(0)
    return answer



#[시간초과]
def solution3(prices):
    answer = []
    while len(prices)>0:
        if prices[0] == min(prices):
            answer.append(len(prices)-1)
            prices.pop(0)
        else:
            for i in range(len(prices)):
                if prices[0] > prices[i]:
                    answer.append(i)
                    break
    return answer