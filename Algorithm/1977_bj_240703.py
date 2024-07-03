from math import sqrt, ceil, floor

M = int(input())
N = int(input())

m = ceil(sqrt(M))
n = floor(sqrt(N))

if m > n:
    exit(print(-1))

total = 0
for i in range(m, n+1):
    total += i**2

print(total)
print(m**2)