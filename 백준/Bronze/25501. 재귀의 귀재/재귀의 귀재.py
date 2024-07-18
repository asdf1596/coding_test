count = 0
def recursion(s, l, r):
    global count
    count+=1
    if l >= r: return 1
    elif s[l] != s[r]: return 0
    else: return recursion(s, l+1, r-1)

def isPalindrome(s):
    global count
    count = 0
    return recursion(s, 0, len(s)-1)
a = int(input())
li1 = []
for i in range(a):
    li1.append(list(input()))
for i in li1:
    print(isPalindrome(i), count)