li1 = []
for a in range(5):
    li1.append(int(input()))
try1 = 0
for i in li1:
    if(i < 40):
        try1+=40
    else:
        try1+=i
print(int(try1/5))