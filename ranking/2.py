# 확신할 수 있는 순위의 조건
# 그래프를 그렸을때
# 그 위치에 자기뿐이라면
# 그럼 확신할 수 있지않을까?
# 매트릭스를 구성하고
# results를 돌아가면서 넣어보자
# 그리고 하나 있는 곳이 확신의 구간
# results를 돌면서 내가 이긴애들만 저장한다.
from collections import deque


# 내가 이긴애들을 다 가지고 있어보자
def solution(n, results):
    matrix = [deque() for i in range(n)]
    for r in results:
        w = r[0]
        l = r[1]

        matrix[w - 1].append(l)
        for i in matrix:
            if w in i and l not in i:
                i.append(l)

    ranking = []
    num = 1
    for i in matrix:

        if not ranking:
            ranking.append(num)
            for j in i:
                ranking.append(j)
        else:
            for j in i:
                if j in ranking:
                    pass
                else:

        num += 1



# 5, [[1, 2], [4, 3], [4, 2], [3, 2], [2, 5]]

if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
