from collections import deque


# 내가 갈 수 있는 곳들을 넣어둔다.
# def solution(n, edge):
#     edge = list(map(lambda x: sorted(x), edge))
#     result = deque()
#     for i in range(1, n + 1):
#         d = deque()
#         for e in edge:
#             if i in e:
#                 if e[0] != i:
#                     d.append(e[0])
#         result.append(d)
#     print(result)

from collections import deque


def solution(n, edge):
    matrix = [deque() for i in range(n)]
    for e in edge:
        x = e[0]
        y = e[1]

        matrix[x - 1].append(y)
        matrix[y - 1].append(x)

    prev = deque([1])
    for i in matrix:
        pass

if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
