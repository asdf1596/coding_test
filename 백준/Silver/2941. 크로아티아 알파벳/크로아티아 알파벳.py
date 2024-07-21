li1 = input()
ans = 0
i = 0
li2 = ["c=","c-","d-","lj","nj","s=","z="]
while i != len(li1):
    if(li1[i:i+3] == "dz="):
        ans+=1
        i+=3
    elif(li1[i:i+2] in li2):
        ans+=1
        i+=2
    else:
        ans+=1
        i+=1
print(ans)