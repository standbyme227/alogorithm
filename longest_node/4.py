def solution(n, edge):
    edge = list(map(lambda x: sorted(x), edge))
    # for i in range(1, n + 1):
    l = [1]
    while True:
        temp = []
        remove = []
        remove_append = remove.append

        for j in edge:
            if i in j:
                temp.append(j[1])
                remove_append[j]

