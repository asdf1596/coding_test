from math import factorial
import sys
li1 = list(str(factorial(int(sys.stdin.readline()))))
#print(li1)
for i in range(len(li1)-1, -1, -1):
    #print(li1[i])
    if li1[i] != '0':
        print(li1[i])
        break