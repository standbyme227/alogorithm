from collections import deque


def solution(n, edge):
    matrix = [deque() for i in range(n)]
    for e in edge:
        x = e[0]
        y = e[1]

        matrix[x - 1].append(y)
        matrix[y - 1].append(x)

    prev = [1]
    cnt = 0
    while True:
        n = len(prev)
        for i in prev[cnt:]:
            for j in matrix[i - 1]:
                if j not in prev:
                    prev.append(j)

        if len(prev) == n:
            return n - cnt
        cnt = n


