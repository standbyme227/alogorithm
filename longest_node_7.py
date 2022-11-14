# 노드의 정보를 가지고 있는 리스트를 돈다.
# 돌면서 다음 시작점을 가져온다.
# 남은 리스트를 (이미 돌았던 리스트를 삭제)

from collections import deque


from collections import deque
def solution(n, edge):
    starts = [1]
    prev_list = deque()
    while True:
        temp = deque()
        prev_list += starts
        for i in edge:
            for s in starts:
                if s in i:
                    target = i[1] if i[0] == s else i[0]
                    if target not in prev_list:
                        temp.append(target)

        if not temp:
            return len(set(starts))
        starts = temp


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
