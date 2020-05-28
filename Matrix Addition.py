"""
<풀이>
1. len(arr) = 행의 갯수
2. len(arr[0]) = 열의 갯수
3. arr[x][j] 를 먼저 계산하고 그걸 그대로 arr[i][x]로 묶어서 계산하면 행렬 완성
"""

def solution(arr1, arr2):
    answer[[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
    return answer


# 넘파이 이용하기
import numpy as np
def solution(arr1, arr2):
    answer = np.array(arr1) + np.array(arr2)
    return answer.tolist()