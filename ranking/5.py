# 확정적인 순위를 알 수 있는 방법?
# 내가 얘를 이기면


# 내가 이긴애들을 다 가지고 있어보자
def solution():
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

    matrix = [[] for i in range(n)]
    for r in results:
        w = r[0]
        l = [r[1]]
        target = matrix[w - 1]
        for i in l:
            if i not in target:
                target.append(i)

        while l:
            temp = []
            for j in l:
                for i in results:
                    if i[0] == j and i[1] not in target:
                        target.append(i[1])
                        temp.append(i[1])
            l = temp

    answer = 0
    for idx, i in enumerate(matrix):
        v = idx + 1
        i.append(v)

        for idx2, j in enumerate(matrix):
            v2 = idx2 + 1
            if v in j and v2 not in i:
                i.append(v2)

        if len(i) == n:
            answer += 1

    return answer


if __name__ == "__main__":
    # node_count = int(input("노드의 수를 넣어주세요"))
    # l = input("리스트를 넣어주세요")
    # if node_count and l:
    #     import ast
    #
    #     l = ast.literal_eval(l)
    solution()
