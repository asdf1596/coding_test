a = int(input())
big = 2**a-1
if(big%2==0):
    ans = (big+1)*(big//2)
else:
    ans = (big+1)*(big//2)+big//2+1
print(bin(ans)[2:])