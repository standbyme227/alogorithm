from collections import deque


def solution(n, edge):
    matrix = [deque() for i in range(n)]
    for e in edge:
        x = e[0]
        y = e[1]

        matrix[x - 1].append(y)
        matrix[y - 1].append(x)

    prev = [1]
    cnt = 0
    while True:
        l = []
        n = len(prev)

        for i in prev[cnt:]:
            l += matrix[i - 1]

        prev += set(l) - set(prev)

        if len(prev) == n:
            return n - cnt
        cnt = n

# [deque([2, 3]), deque([1, 4, 5]), deque([1, 5, 6]), deque([2, 8, 9]), deque([2, 3, 9, 10]), deque([3, 10, 11]), deque([]), deque([4]), deque([4, 5]), deque([5, 6]), deque([6])]
if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
