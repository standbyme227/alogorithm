n = int(input())
m = int(input())
arr = []
for _ in range(m):
    arr.append(list(map(int, input().split())))

# 오름차순 정렬
arr.sort(key=lambda x: x[2])
matrix = [[] for i in range(n)]
current = arr[0][0]

results = 0
for a in arr:
    is_cycle = False

    x = a[0]
    y = a[1]

    current = x
    stack = [current]
    visited = []

    while stack:
        visited.append(current)

        if current == x:
            if y not in visited:
                stack.append(y)

        if current == y:
            if x not in visited:
                stack.append(x)

        neighbors = matrix[current - 1]
        for i in neighbors:
            if i not in visited:
                stack.append(i)
        current = stack.pop()

    if len(visited) != len(set(visited)):
        is_cycle = True

    if is_cycle is False:
        matrix[x - 1].append(y)
        matrix[y - 1].append(x)
        # new_arr.append(a)
        results += a[2]

print(results)
