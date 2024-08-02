a,b = map(int, input().split())
li1 = [0,31,28,31,30,31,30,31,31,30,31,30]
ans = sum(li1[0:b])+a+2
li2 = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(li2[ans%7])