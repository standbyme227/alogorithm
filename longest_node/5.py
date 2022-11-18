from collections import deque


# 노드를 돌고
# 이어진 선을 찾아간다.
# 갈곳이 없다면 멈춘다.
# 첫 스타트 를 돌면서
# 다음 노드를 찾는다.
# 다음 노드 리스트를 다시 스타트로 정한다.
# 이미 지나간 계층은 접근하지 못한다.
from collections import deque
def solution(n, edge):
    start = [1]
    prev_list = []
    while start:
        temp = []
        for i in start:
            cnt = 0

            remove = list()
            for j in edge:
                t = list(j)
                if i in t:
                    cnt += 1
                    target = t[1] if i == t[0] else t[0]
                    if target not in start and target not in prev_list and target not in temp:
                        temp.append(target)
                        remove.append(t)
                else:
                    pass
            prev_list.append(i)
            for r in remove:
                edge.remove(r)


        if temp:
            start = sorted(temp)
        else:
            print(start)
            if start == [1]:
                return 0
            return len(start)


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
