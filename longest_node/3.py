# [[0, 1, 1, 0, 0, 0],
#  [0, 0, 0, 1, 0, 0],
#  [0, 1, 0, 0, 0, 1],
#  [0, 0, 1, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0]]

# idx리스트를 받아서
# 갈 수 있는 idx를 얻는다.
# 해당 값들을 계속 추가하며
# prev idx도 추가한다.
# while로 돌린다.


def get_bfs(matrix, idx_list):
    prev_list = [0]
    while True:
        temp = []
        temp_append = temp.append
        for i in idx_list:
            for idx, j in enumerate(matrix[i]):
                if j == 1 and idx not in prev_list:
                    temp_append(idx)
                    prev_list.append(idx)
        if temp:
            idx_list = temp
        else:
            break
    return idx_list


def get_adjecency_matrix(n, edge):
    m = [([0] * n) for i in range(n)]
    for i in edge:
        x = i[0] - 1
        y = i[1] - 1
        m[x][y] = 1
        m[y][x] = 1
    return m


def solution(n, edge):
    m = get_adjecency_matrix(n, edge)
    d = get_bfs(m, idx_list=[0])
    return d


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
