# 11
# maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
# maps = [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
# maps = [[1, 1, 1, 1, 1], [0, 0, 0, 0, 1], [1, 1, 1, 1, 1], [1, 0, 0, 0, 0], [1, 1, 1, 1, 1]]
maps = [[1, 1, 1, 0, 0], [0, 0, 1, 1, 1]]


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

    if n > 1 and m > 1:
        if 0 == maps[0][1] == maps[1][0] or 0 == maps[m - 1][n - 2] == maps[m - 2][n - 1]:
            return -1

    map_dict = dict()
    for y, i in enumerate(maps):
        for x, j in enumerate(i):
            map_dict[(x, y)] = []
            results = check_blocks(maps, x, y, n, m)
            for result in results:
                if result != (x, y) and result not in map_dict[(x, y)]:
                    map_dict[(x, y)].append(result)

    starts = [
        [[], (n - 1, m - 1), 0]
    ]

    answer = 0

    while starts:
        temp = []
        for i in starts:
            # 시작 지점
            start = i[1]
            prev_list = i[0]
            cnt = i[2]
            cnt += 1

            if start == (0, 0):
                if answer == 0:
                    answer = cnt
                else:
                    if answer > cnt:
                        answer = cnt
                continue

            if answer != 0 and cnt >= answer:
                continue

            x = start[0]
            y = start[1]

            next_list = []
            prev_list.append(start)

            if maps[y][x] != 0:
                results = map_dict[(x, y)]
                for result in results:
                    if result not in prev_list:
                        next_list.append(result)

            for nxt in next_list:
                temp.append([prev_list, nxt, cnt])
        starts = temp
    # print(answer if answer else -1)
    return answer if answer else -1


solution(maps)
