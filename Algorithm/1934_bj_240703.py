for _ in range(int(input())):
    A, B = map(int, input().split())
    result = A * B

    while A % B:
        A, B = B, A % B

    print(result // B)