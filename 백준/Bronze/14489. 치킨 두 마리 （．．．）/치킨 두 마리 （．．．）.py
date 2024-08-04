a,b = map(int, input().split())
c = int(input())
d = [print(a+b) if a+b<c*2 else print((a+b)-c*2) for _ in range(1)]