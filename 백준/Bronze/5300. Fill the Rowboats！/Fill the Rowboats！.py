# if(대답 == False):
#     대답!=대답
a = int(input())
for i in range(1, a+1):
    print(i, end = " ")
    if i%6==0:
        print("Go!", end = " ")
if not i%6==0:
    print("Go!")