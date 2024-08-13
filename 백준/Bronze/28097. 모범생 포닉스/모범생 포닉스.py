a = int(input())
li1 = list(map(int, input().split()))
print((sum(li1)+8*(a-1))//24, (sum(li1)+8*(a-1))%24)