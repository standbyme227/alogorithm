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


# def get_gragh2(nodes, edge):
#     # dict가 아닌 이전 계층의 리스트만을 갖게 한다.


def get_gragh(nodes, edge):
    # 1부터 시작한다.
    # 방향은 내려가는 방향이 있다.
    # 그러니 같은 계층은 연결되지 못하게한다.

    d = dict()
    upper = [1]
    k = [0]
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
                        if j in e:
                            x = list(e)
                            # x.remove(j)
                            y = x[0] if x[0] != j else x[1]

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
    answer = len(d[max(k)])
    return answer


def solution(n, edge):
    # edge = list(map(lambda x:sorted(x), edge)).sorted(x[0])
    # print(edge)
    edge = sorted(list(map(lambda x: sorted(x), edge)), key=lambda x: x[0])
    start = [1]
    prev_list = []
    while True:
        temp = []

        for i in start:
            cnt = 0
            print("처음", edge)
            for j in edge:
                print("이전", prev_list)
                if i == j[0]:
                    if j[1] in prev_list:
                        continue
                    print("맞네", j)
                    cnt += 1
                    target = j[1]
                    temp.append(target)
                else:
                    break
            edge = edge[cnt:]
            print("변경", edge)
            print("")

        print("템프", temp)
        if not temp or not edge:
            break

        start = temp
        prev_list += temp

    if temp:
        print(temp)
        return len(set(temp))

    if edge:
        return len(edge)



if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
