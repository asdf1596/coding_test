def solution(nums):
    ans = 0
    a = len(nums)//2
    li1 = list(set(nums))
    if len(li1)>a:
        return(a)
    else:
        return(len(li1))