def solution(a, b):
    answer = 0
    for A in range(len(a)):
        for B in range(len(b)):
            if a[A] == b[B]:
                answer+=1
    return answer