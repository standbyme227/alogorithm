from collections import deque


# 내 위에 있는 놈들을 따져보자

def solution(n, results):
    matrix = [deque() for i in range(n)]
    for r in results:
        w = r[0]
        l = r[1]

        matrix[l - 1].append(w)
        # for i in matrix:
        # if w in i and l not in i:
        # i.append(l)

    print(matrix)
    answer = 0
    return answer


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
