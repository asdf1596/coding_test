import sys
li1 = list(sys.stdin.readline().strip())
try1 = 0
for i in li1:
	if i == "@":
		try1+=1
	elif i == "(":
		print(try1, end=" ")
		try1 = 0
print(try1)
