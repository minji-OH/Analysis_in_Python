N = [2,5,7,2,6,8,9,2,3,4,1,7,6]
m = 8

answer = []
for head in range(len(N)):
    partial = N[head]
    for i in range(head+1, len(N)):
        partial = partial + N[i]
        answer.append(partial)

print(answer.count(m) + N.count(m))

#예제의 기대값 4, 결과값 4. 정답!? ~_~??