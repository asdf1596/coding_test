from collections import deque
while True:
    Big = 0
    Small = 0
    last = deque([])
    li1 = list(input())
    check = True
    if li1 == ["."]:
        break
    for i in li1:
        if i == "(":
            Big+=1
            last.append(")")
        elif i == ")":
            if Big < 1 or last.pop()!=i:
                check = False
                break
            else:
                Big-=1
        elif i == "[":
            Small+=1
            last.append("]")
        elif i == "]":
            if Small < 1 or last.pop() != i:
                check = False
                break
            else:
                Small-=1
    #print(check, Small, Big)
    if not check or Small !=0 or Big !=0:
        print("no")
    else:
        print("yes")