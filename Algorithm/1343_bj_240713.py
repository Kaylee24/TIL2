'원숭이 코드'

board = input()
L = len(board)

# 보드판 순회
    # X 나오면 . 나올때까지 X 몇갠지 확인
        # X 개수 홀수면 exit(print(-1))
        # X 개수 짝수면 4로 나눠서 몫, 나머지 확인하고 결과 출력
    # . 나오면 그대로 출력

result = ''
count_X = 0
for i in range(L):
    if board[i] == '.':
        if count_X > 0:
            if count_X % 2:
                exit(print(-1))
            else:
                count_A = count_X // 4
                count_B = count_X % 4 // 2
                result += 'AAAA' * count_A + 'BB' * count_B
        result += '.'
        count_X = 0
    else:
        count_X += 1
if count_X > 0:
    if count_X % 2:
        exit(print(-1))
    else:
        count_A = count_X // 4
        count_B = count_X % 4 // 2
        result += 'AAAA' * count_A + 'BB' * count_B

print(result)
