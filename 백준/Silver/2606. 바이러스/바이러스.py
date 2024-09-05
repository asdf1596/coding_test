import sys
a  = int(sys.stdin.readline())
b  = int(sys.stdin.readline())
try1 = True
try2 = 0
li1 = []
for i in range(b):
    c,d = map(int, sys.stdin.readline().split())
    if c==1 or d==1:
        if try1:
            try1 = False
            try2 = i
            li1.append(set([c,d]))
        else:
            li1.append([c,d])
    else:
        li1.append([c,d])
if try1:
    print(0)
else:
    for i in range(len(li1)):
        for j in range(len(li1)):
            if li1[j] !=[] and j != try2 and (li1[j][0] in li1[try2] or li1[j][1] in li1[try2]):
                li1[try2].add(li1[j][0])
                li1[try2].add(li1[j][1])
                li1[j] = []
        #print(li1)
    print(len(li1[try2])-1)