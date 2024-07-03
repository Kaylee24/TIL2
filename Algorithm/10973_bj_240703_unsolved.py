N = int(input())
arr = list(map(int, input().split()))

arr_sorted = sorted(arr)

print(arr)
print(arr_sorted)

if arr == arr_sorted:
    print(-1)
else:
    