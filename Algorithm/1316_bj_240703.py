result = 0

for _ in range(int(input())):
    word = list(input())
    checked = [word[0]]

    # 단어의 철자를 순회하며
    a = word[0]
    count = 1
    for char in word:
        # 앞의 철자와 연속되지 않는 철자라면
            # 이전에 나왔던 철자라면 count 하지 말고 for문 종료 및 do not count
            # 이전에 없던 철자라면 pass
        if char != a:
            a = char
            if char in checked:
                count = 0
                break
            checked.append(a)
    
    # for문이 정상적으로 끝났다면 count
    if count:
        result += 1

print(result)