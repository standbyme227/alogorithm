# 매트릭
# for 문을 돈다.


from collections import deque

n = 3


# [[1, 3], [4, 3], [3, 2], [1, 2], [5, 3]]
#
# [[4, 1, 5], 3, 2]


# 내가 이긴애들을 다 가지고 있어보자
def solution():
    n = 5
    results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

    win = [deque() for i in range(n)]
    lose = [deque() for i in range(n)]
    for r in results:
        w = r[0]
        l = r[1]

        # lose[l - 1].append(w)
        win[w - 1].append(l)
        # for i in matrix:
        #     if w in i and l not in i:
        #         i.append(l)
    # results = [[i for i in range(1, n + 1)]]
    print(win)
    results = []
    for idx in range(n):
        v = idx + 1

        # 내가 이긴애들
        win_list = win[idx]

        # if set(win_list) - results
        pass








# 5, [[1, 2], [4, 3], [4, 2], [3, 2], [2, 5]]

if __name__ == "__main__":
    # node_count = int(input("노드의 수를 넣어주세요"))
    # l = input("리스트를 넣어주세요")
    # if node_count and l:
    #     import ast
    #
    #     l = ast.literal_eval(l)
    solution()
