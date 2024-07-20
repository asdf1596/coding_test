A = []
B = []
while(True):
    a,b = map(int, input().split())
    A.append(a)
    B.append(b)
    if(a==0 and b==0):
        break
for i in range(len(A)):
    if(A[i]==0 and B[i]==0):
        break
    print(A[i]+B[i])