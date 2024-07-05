N = int(input())   # 체크포인트의 수 N
points = []

for _ in range(N):
    x, y = map(int, input().split())   # 체크포인트의 x좌표, y좌표
    points.append([x, y])

dist = []
for i in range(1, N):
    dist.append(abs(points[i][0] - points[i-1][0]) + abs(points[i][1] - points[i-1][1]))

total = sum(dist)
results = []

for i in range(1, N-1):
    r = total - (dist[i-1] + dist[i]) + (abs(points[i+1][0] - points[i-1][0]) + abs(points[i+1][1] - points[i-1][1]))
    results.append(r)

print(min(results))