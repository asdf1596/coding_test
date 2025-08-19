def XOR (a, b): 
    if a != b: 
        return True
    else: 
        return False
for i in range(int(input())):
    a = input()
    b = input()
    ans = 0
    for i in range(len(a)):
        if(XOR(a[i], b[i])):
            ans+=1
    print("Hamming distance is", str(ans)+".")
        