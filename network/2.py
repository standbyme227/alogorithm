from collections import deque
from itertools import combinations


def solution():
    # n = int(input())
    # m = int(input())
    # arr = []
    # for _ in range(m):
    #     arr.append(list(map(int, input().split())))

    n = 6
    m = 9
    i = "1 2 5,1 3 4,2 3 2,2 4 7,3 4 6,3 5 11,4 5 3,4 6 8,5 6 8"
    arr = [list(map(int, i.split())) for i in i.split(',')]

    # 오름차순 정렬
    arr.sort(key=lambda x: x[2])


    new_arr = []
    result = 0
    results = []

    for i in arr:
        new_arr.append(i)

        matrix = [deque() for i in range(n)]
        for a in new_arr:
            x = a[0]
            y = a[1]

            matrix[x - 1].append(y)
            matrix[y - 1].append(x)

        print(matrix)

        stack = [1]
        visited = []

        is_cycle = False

        while stack:
            current = stack.pop()
            for neighbor in matrix[current-1]:
                if neighbor > 0:
                    if neighbor not in visited:
                        stack.append(neighbor)
                    visited.append(current)

            if current in visited:
                is_cycle = True
                break
        if is_cycle is True:
            pass
        else:
            results.append(i)
    print(results)

if __name__ == "__main__":
    solution()
