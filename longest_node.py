"""
구조
 - 그래프를 표현한다.
 - 딕트로 그래프들을 표현한다.
 - 각 노드는 key 그와 연결된 노드는 리스트에 넣는다.

로직
 - DFS를 우선적으로 해당 노드들을 돌아본다
 - 가장 깊은 단계를 변수로 저장하고
 - 그와 같은 깊이가 나오면 다른 변수에 갯수를 저장한다.
 - 깊이를 찾아가는 로직에서
 - 못가는 곳이 분명히 존재하는데 현재 표현할 방법을 모르겠다.
 - 계층을 저장한다.

 - 한 칸을 갈 수 있는 곳을 다 가본다.
 - 이전 단계에서 들린적이 있는 곳이면 해당 방법은 폐기한다.
"""


def get_gragh(nodes, edge):
    # 1부터 시작한다.
    # 방향은 내려가는 방향이 있다.
    # 그러니 같은 계층은 연결되지 못하게한다.

    d = dict()
    upper = [1]
    for i in range(nodes):
        k = d.keys()
        if i == 0:
            d[i] = [1]
        else:
            # 계층을 확인하는 로직
            u = i - 1
            if u in k:
                l = d[u]
                # 해당 계층에서 갈 수 있는 노드(j)를 모아놓은 리스트(l)
                for j in l:
                    deleting_list = []
                    for e in edge:
                        x = list(e)
                        if j in x:
                            x.remove(j)
                            y = x[0]

                            if y not in upper:
                                if i in k:
                                    t = d[i]
                                    if y not in t:
                                        t.append(y)
                                        d[i] = t
                                else:
                                    d[i] = [y]
                                deleting_list.append(e)
                    for r in deleting_list:
                        edge.remove(r)
        if i in k:
            upper += d[i]
    # print(d)
    answer = len(d[max(d.keys())])
    return answer


def solution(n, edge):
    edge = list(map(lambda x:sorted(x), edge))
    # print(edge)
    print(get_gragh(n, edge))


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
