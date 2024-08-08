ans = 0
for i in range(8):
    li1 = list(input())
    for j in li1:
        if j == "K":
            ans+=0
        elif j == "P":
            ans+=1
        elif j == "N":
            ans+=3
        elif j == "B":
            ans+=3
        elif j == "R":
            ans+=5
        elif j == "Q":
            ans+=9
        elif j == "k":
            ans-=0
        elif j == "p":
            ans-=1
        elif j == "n":
            ans-=3
        elif j == "b":
            ans-=3
        elif j == "r":
            ans-=5
        elif j == "q":
            ans-=9
print(ans)