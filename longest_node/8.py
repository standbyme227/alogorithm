from collections import deque

# 돌면서
# 현재 노드 추가
# 이전에 갔던 노드면 제외
# 전체 노드를 추가하는게 있고
# 각 칸마다 추가하는게 있다고 가정

from collections import deque


def insert_value(d, k, v):
    if k in d:
        d[k].append(v)
    else:
        d[k] = deque([v])
    return d


def solution(n, edge):
    # 돌면서 위치를 저장한다.
    d = dict()
    for e in edge:
        x, y = e[0], e[1]
        d = insert_value(d, x, y)
        d = insert_value(d, y, x)

    starts = deque([1])
    prev_list = deque([1])
    while True:
        for i in starts:
            l = d[i]
            if not l:
                return len(starts)

            for v in l:
                if v not in prev_list:
                    starts.append(v)
                    prev_list.append(v)
            starts.popleft()

def solution(n, edge):
    # s = deque()
    # s.append(1)
    starts = deque([1])
    prev_list = deque([1])

    while True:
        temp = deque()
        for i in edge:
            for s in starts:
                if s in i:
                    target = i[1] if i[0] == s else i[0]
                    if target not in prev_list:
                        temp.append(target)
                        prev_list.append(target)

        if not temp:
            # print(len(set(starts)))
            return len(set(starts))
        starts = temp


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
