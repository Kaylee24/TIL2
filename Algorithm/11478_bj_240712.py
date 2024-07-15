word = input()
L = len(word)

parts = []
for i in range(1, L):
    s = 0
    while s + i <= L:
        parts.append(word[s:s+i])
        s += 1

parts = set(parts)

print(len(parts) + 1)