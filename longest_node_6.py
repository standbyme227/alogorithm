def get_gragh(nodes, edge):
    d = dict()
    upper = [1]
    k = [0]
    edge_keys = edge.keys()
    for i in range(nodes):
        k = d.keys()
        if i == 0:
            d[i] = [1]
        else:
            u = i - 1
            if u in k:
                l = d[u]
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
                answer = len(d[i - 2])
                break
        if i in k:
            upper += d[i]
    return answer


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
    edge = get_edge_dict(edge)
    return get(edge)
    # return get_gragh(n, edge)


def get(edge):
    start = [1]
    prev_list = []
    # cnt = 0

    while True:
        temp = []
        temp_append = temp.append
        prev_list += start
        for i in start:
            v = edge[i]
            for j in v:
                if j not in prev_list:
                    temp_append(j)

        if not temp:
            return len(set(start))
        start = temp


if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
