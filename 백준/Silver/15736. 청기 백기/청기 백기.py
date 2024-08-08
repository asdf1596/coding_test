import math
def countOddDivisors(a):
    count = 0
    for i in range(1, int(math.sqrt(a)) + 1):
        count +=1
    return count
a = int(input())
ans = countOddDivisors(a)
print(ans)
