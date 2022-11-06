# 정수 리스트를 받는다.
# 정렬을 해서 가장 큰수를 만들어낸다.

# 어떤 수가 더 큰지 가려내는 로직이 중요하다.
# 숫자 문자열을 비교해서 가장 긴 수를 인지한다.
# 그리고 자리수를 맨 앞부터 비교해서 가장 큰 수를 얻는다.
# 다중 배열로 얻어낸다.

def get_bigger(x, y):
    n = 0
    print(x, y)
    while True:
        target1 = x[n] if len(x) - 1 >= n else x[-1]
        target2 = y[n] if len(y) - 1 >= n else y[-1]

        if target1 > target2:
            pass
            break
        elif target1 < target2:
            x, y = y, x
            break
        else:
            n += 1
            if max(len(x), len(y)) <= n:
                x, y = (x, y) if len(x) <= len(y) else (y, x)
                break
    print(x, y)
    print("")
    return x, y


def solution(numbers):
    # 바뀐게 있으면 계속 돌아가고 없으면 멈춘다.
    numbers = list(map(str, numbers))
    while True:
        prev = 0
        is_changed = False
        temp = []
        for n in numbers:
            if prev == 0:
                prev = n
            else:
                if prev != n:
                    x, y = get_bigger(prev, n)
                    if x != prev:
                        is_changed = True
                        prev, n = x, y

                    temp.append(prev)
                    prev = n

                else:
                    pass
        if numbers:
            temp.append(n)

        if is_changed is False:
            break

        numbers = temp
    print("".join(numbers))
    return "".join(numbers)


if __name__ == "__main__":
    import ast

    l = input("리스트를 입력해주세요")
    if l:
        l = ast.literal_eval(l)
        solution(l)
