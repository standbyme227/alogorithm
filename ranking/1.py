def solution(n, results):
    ranking = []
    for r in results:
        w = r[0]
        l = r[1]

        if w in ranking:
            if l in ranking:
                w_idx = ranking.index(w)
                l_idx = ranking.index(l)

                if w_idx < l_idx:
                    pass
                else:
                    t = ranking[:l_idx]
                    t.append(w)
                    t2 = ranking[l_idx:]
                    t2.remove(w)

                    ranking = t + t2
            else:
                ranking.append(l)
        else:
            if l in ranking:
                l_idx = ranking.index(l)
                t = ranking[:l_idx]
                t.append(w)
                t2 = ranking[l_idx:]

                ranking = t + t2
            else:
                ranking.append(w)
                ranking.append(l)

    print(ranking)




# 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]

if __name__ == "__main__":
    node_count = int(input("노드의 수를 넣어주세요"))
    l = input("리스트를 넣어주세요")
    if node_count and l:
        import ast

        l = ast.literal_eval(l)
        solution(node_count, l)
