# 11
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]


# maps = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]

# maps = [
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#
# ]
maps = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
]
# maps = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1]]


# maps = [[1, 1, 1], [1, 1, 1]]

# (1,1) 부터 (사실은 0,0임)
# (n,m)까지 최단거리 처리
# 재귀로 처리?

# 리스트를 순환하면서
# 근접한 지점들을 확인?
# 갈 수 있는 방향을 가지고 있던가?
# 갈 수 있는 지점을 가지고 있던가? (이걸로 시작)
def check_blocks(maps, x, y, n, m):
    results = []
    if x < n - 1:
        a = x + 1
        if maps[y][a] == 1:
            results.append((a, y))

    if x > 0:
        a = x - 1
        if maps[y][a] == 1:
            results.append((a, y))

    if y < m - 1:
        b = y + 1
        if maps[b][x] == 1:
            results.append((x, b))

    if y > 0:
        b = y - 1
        if maps[b][x] == 1:
            results.append((x, b))

    return results


def solution(maps):
    n = len(maps[0])
    m = len(maps)
    shortcut = n + m - 1

    if n > 1 and m > 1:
        if 0 == maps[0][1] == maps[1][0] or 0 == maps[m - 1][n - 2] == maps[m - 2][n - 1]:
            return -1

    map_dict = dict()
    zero = 0
    other = 0

    for y, i in enumerate(maps):
        for x, j in enumerate(i):
            k = maps[y][x]
            if k == 1:
                other += 1
            else:
                zero += 1

            map_dict[(x, y)] = []
            results = check_blocks(maps, x, y, n, m)
            for result in results:
                if result != (x, y) and result not in map_dict[(x, y)]:
                    map_dict[(x, y)].append(result)

    if zero > (n * m) * (2 / 3):
        return -1

    elif zero == 0:
        return shortcut

    elif zero < n and zero < m:
        return shortcut

    starts = [
        [[], (n - 1, m - 1), 0]
    ]

    answer = 0

    while starts:
        temp = []
        for i in starts:
            # 시작 지점
            target = i[1]
            cnt = i[2]
            cnt += 1

            if target == (0, 0):
                if answer == 0 or answer > cnt:
                    answer = cnt

                if shortcut == answer:
                    return answer
                continue

            if answer != 0 and cnt >= answer:
                continue

            x = target[0]
            y = target[1]

            i[0].append(target)

            if maps[y][x] != 0:
                results = map_dict[(x, y)]
                for result in results:
                    if result not in i[0]:
                        temp.append([i[0], result, cnt])
        starts = temp
    # print(answer if answer else -1)
    return answer if answer else -1


solution(maps)
