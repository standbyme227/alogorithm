from collections import deque


def solution():
    # n = int(input())
    # m = int(input())
    n = 6
    m = 9

    i = "1 2 5,1 3 4,2 3 2,2 4 7,3 4 6,3 5 11,4 5 3,4 6 8,5 6 8"
    arr = [list(map(int, i.split())) for i in i.split(',')]
    # print(arr)
    # arr = []
    # for _ in range(m):
    #     arr.append(list(map(int, input().split())))
    # DFS?

    matrix = [deque() for i in range(n)]
    for a in arr:
        x = a[0]
        y = a[1]
        p = a[2]

        # matrix[x - 1].append(y)
        # matrix[y - 1].append(x)

        matrix[x - 1].append((y, p))
        matrix[y - 1].append((x, p))

    # print(matrix)

    # 어떻게 연결되는 모든 경우의 수를 알 수 있을까?
    price = 0
    next = [(1,0)]
    prev = []

    while True:
        temp = []
        for i in next:
            route = []
            prev.append(i[0])
            for j in matrix[i[0] - 1]:
                if j[0] not in prev:
                    temp.append([j[0], i[1]+j[1]])
        if not temp:
            break
        next = temp
    print(min(next, key=lambda x: x[1]))



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
