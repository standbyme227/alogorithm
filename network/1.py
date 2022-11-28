from collections import deque
from itertools import combinations


def solution():
    n = int(input())
    m = int(input())
    arr = []
    for _ in range(m):
        arr.append(list(map(int, input().split())))
    matrix = [[0] * n for i in range(n)]

    # n = 6
    # m = 9
    # i = "1 2 5,1 3 4,2 3 2,2 4 7,3 4 6,3 5 11,4 5 3,4 6 8,5 6 8"
    # arr = [list(map(int, i.split())) for i in i.split(',')]
    # print(arr)

    for a in arr:
        x = a[0]
        y = a[1]
        p = a[2]

        matrix[x - 1][y - 1] = p

    answer = 0
    for i in matrix:
        l = [j for j in i if j != 0]
        if l:
            answer += min(l)

    return answer


# 6 컴퓨터 수
# 9 줄의 수
# 1 2 5 앞에랑 뒤에 연결하는데 드는 비용
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8

if __name__ == "__main__":
    solution()
