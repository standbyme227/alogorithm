from collections import deque


# 확실한 순위라는 건 어떤 상황일까?
# -> 그래프로 구현했을때 갈 수 있는 곳이 거기밖에 없다.
# 그래프를 구성하면 어떻게 될까?
# 그래프는 어떻게 구성할 수 있을까?
# class로 구성해보자

class Node:
    # 단방향으로 구성
    def __init__(self, value):
        self.value = value
        self.next = []
        self.index = None

    def add_next(self, next):
        self.next.append(next)

    def set_index(self, index):
        self.index = index


class Graph:
    # 그래프는 어떤 구성을 하면 좋을까?
    # 일단 노드끼리 연결되어있는건 그 안에서 구성이 되니
    # 그 노드를 리스트로 저장해서 계층을 나눠볼까?
    # 그리고 value와 node로 dict를 구현한다.
    def __init__(self):
        self.map = []
        self.dict = {}

    def get_node(self, value):
        return self.dict[value]

    def get_group(self, index):
        return self.map[index]

    def add_group(self, index, value):
        g = self.get_group(index)
        if isinstance(g, list):
            g.append(value)
        else:
            g = [g, value]

        self.map[index] = g
        return index

    def add_node(self):

    def pop_node(self, from_index, to_index, value):
        g =


def solution(n, results):
    matrix = [deque() for i in range(n)]
    for r in results:
        w = r[0]
        l = r[1]

        matrix[w - 1].append(l)

    ranking = []
    while True:


# 5, [[1, 2], [4, 3], [4, 2], [3, 2], [2, 5]]

if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
