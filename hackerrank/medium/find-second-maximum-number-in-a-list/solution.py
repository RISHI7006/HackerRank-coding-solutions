if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    a = max(arr)
    b = []

    for i in arr:
        if i < a:
            b.append(i)

    print(max(b))
