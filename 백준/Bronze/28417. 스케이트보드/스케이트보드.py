import sys
z = int(sys.stdin.readline())
li2 = []	
for i in range(z):
	a,b,c,d,e,f,g= map(int, sys.stdin.readline().split())
	try1 = max([a,b])
	li1 = sorted([c,d,e,f,g], reverse = True)
	try1+=sum(li1[0:2])
	li2.append(try1)
print(max(li2))
