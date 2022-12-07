import time


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
    matrix = [[] for i in range(n)]
    current = arr[0][0]

    results = 0
    for a in arr:
        is_cycle = False

        x = a[0]
        y = a[1]

        matrix[x - 1].append(y)
        matrix[y - 1].append(x)

        stack = [current]
        visited = []

        while stack:
            visited.append(current)

            neighbors = matrix[current - 1]
            for i in neighbors:
                if i not in visited:
                    stack.append(i)
            current = stack.pop()

        if len(visited) != len(set(visited)):
            is_cycle = True

        # 스택은 어떻게 쌓이는가?
        # DFS를 진행한다.
        # 가장 밑에까지가고 다른 형재로 간다.
        # DFS를 위한 방법이 stack으로 보여진다.

        if is_cycle is True:
            matrix[x - 1].pop()
            matrix[y - 1].pop()
        else:
            # new_arr.append(a)
            results += a[2]

    print(results)


if __name__ == "__main__":
    prev = time.time()
    solution()
    print(time.time() - prev)
