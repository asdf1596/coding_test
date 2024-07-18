a = int(input())
string = list(input())
#-96
li1 = []
count = 0
for i in range(len(string)):
    li1.append((ord(string[i])-96)*(31**count))
    count+=1
print(sum(li1))