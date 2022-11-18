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
        temp = deque()
        for i in starts:
            l = d[i]

            for v in l:
                if v not in prev_list:
                    temp.append(v)
                    prev_list.append(v)

        if not temp:
            return len(starts)
        starts = temp


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
