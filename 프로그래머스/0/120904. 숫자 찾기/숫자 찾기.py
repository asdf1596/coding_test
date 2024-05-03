def solution(num, k):
    k = str(k)
    a = str(num).find(k)
    if a!=-1:
        a+=1
    return a