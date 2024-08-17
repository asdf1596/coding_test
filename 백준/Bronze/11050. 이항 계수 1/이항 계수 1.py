import math
a,b = map(int, input().split())
c = math.factorial(a)/(math.factorial(b)*math.factorial(a-b))
print(int(c))