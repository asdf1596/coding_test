from math import factorial
a = int(input())
for i in range(a):
    b,c = map(int, input().split())
    print(factorial(c)//(factorial(b)*factorial(c-b)))