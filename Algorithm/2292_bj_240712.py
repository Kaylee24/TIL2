N = int(input())

# 6, 12, 18, ...

i, result = 1, 1

while N > 1:
    N -= 6 * i
    i += 1
    result += 1

print(result)