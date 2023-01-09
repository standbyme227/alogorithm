# 사방이 막혀있다
# 모든
# 각 점들을 저장한다.
# 각 꼭지점을 저장한다.
# - 방향이 바뀌면 꼭지점이다.
# - 이미 지나간 지점을 만나면 꼭지점이다.
# 이미 지나간 지점을 또 지나가면 하나의 방이 완성된다.
# 이동 arrow가 4차이가 나면 무시한다 (왔다갔다)

arrows = [6, 6, 4, 4, 2, 2, 0, 0]

def solution(arrows):
    move_dict = {
        0: (0, 1),
        1: (1, 1),
        2: (1, 0),
        3: (1, -1),
        4: (0, -1),
        5: (-1, -1),
        6: (-1, 0),
        7: (-1, 1),
    }

    point = (0, 0)
    point_list = [point]
    stack = []
    # corner_list
    prev = None
    room = 0

    for i in arrows:
        if not prev:
            pass
        else:
            if stack:
                exception = abs(stack[-1] - i)

                if exception == 4:
                    stack.pop()
                    continue

            # if 4 == abs(prev - i):
            #     continue

        stack.append(i)
        move = move_dict[i]
        point = (point[0] + move[0], point[1] + move[1])

        if point in point_list:
            room += 1
        else:
            point_list.append(point)

        prev = i

    # answer = len(point_list) - len(set(point_list))
    # print(room)
    return room
