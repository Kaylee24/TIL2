for _ in range(int(input())):
    R, S = input().split()
    R = int(R)
    S = list(S)

    result = ''
    for char in S:
        result += char * R

    print(result)