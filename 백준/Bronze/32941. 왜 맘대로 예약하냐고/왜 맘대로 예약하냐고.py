t, x = map(int, input().split())
n = int(input())
cnt = 0
for _ in range(n):
    k = int(input())
    a_list = list(map(int, input().split()))
    if x in a_list:
        cnt += 1
print("YES" if cnt == n else "NO")