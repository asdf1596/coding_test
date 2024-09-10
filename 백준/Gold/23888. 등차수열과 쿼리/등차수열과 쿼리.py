#0910 마지막 버전
import sys
def try1(a, b):
    while b:
        a, b = b, a%b
    return a
a,b = map(int, sys.stdin.readline().split())
cdg = try1(a,b)
z = int(sys.stdin.readline())
results = []
for _ in range(z):
    c,d,e = map(int, sys.stdin.readline().split())
    num1 = (a+(d-1)*b)
    num2 = (a+(e-1)*b)
    if c == 1:
        if d==e:
            results.append(str(num1) + '\n')
        elif (e-d)%2==1:
            ans = ((num1)+(num2))*((e-d+1)//2)
            results.append(str(ans) + '\n')
        else:
            ans = ((num1)+(num2))*((e-d)//2)+((num1)+(num2))//2
            results.append(str(ans) + '\n')
    else:
        if b !=0:
            if d==e:
                results.append(str(num1) + '\n')
            else:
                f = cdg
                results.append(str(f) + '\n')
        else:
            results.append(str(a) + '\n')
sys.stdout.write("".join(results))