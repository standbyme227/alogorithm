def get_gragh(nodes, edge):
    # 1부터 시작한다.
    # 방향은 내려가는 방향이 있다.
    # 그러니 같은 계층은 연결되지 못하게한다.

    d = dict()
    upper = [1]
    k = [0]
    edge_keys = edge.keys()
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
                    edge_list = edge[j] if j in edge_keys else []
                    for e in edge_list:
                        if e not in upper:

                            if i in k:
                                t = d[i]
                                if e not in t:
                                    t.append(e)
                                    d[i] = t
                            else:
                                d[i] = [e]
            else:
                # print(i-2)
                answer = len(d[i - 2])
                # print(answer)
                break
        if i in k:
            upper += d[i]
    # print(d)
    # answer = len(d[max(k)])
    return answer

# 이 부분이 속도를 망치는 부분인거 같다.
# 간선과 노드들을 파악하면서
# 한 번에 가장 먼 노드들을 가져올 수 있을까?
# 1부터 시작한다.
# [1, 2], [4, 3], [2, 3], [1,4]
#
def set_dict(key, value, d, keys=None):
    if not keys:
        keys = d.keys()

    if key in keys:
        if value not in d[key]:
            d[key].append(value)
    else:
        d[key] = [value]
    return d


def get_edge_dict(edge):
    d = dict()
    for i in edge:
        x = i[0]
        y = i[1]
        d = set_dict(x, y, d)
        d = set_dict(y, x, d)
    return d


def solution(n, edge):
    # edge = list(map(lambda x:sorted(x), edge))
    # print(edge)
    edge = get_edge_dict(edge)
    # print(edge)
    return get_gragh(n, edge)