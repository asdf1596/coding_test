import sys
from collections import deque
a,b  = map(int, sys.stdin.readline().split())
map1 = []
def bfs(a,b):
    queue = deque()
    queue.append(a)
    #mapPrint(map1)
    if a==b:
        return 0
    else:
        day = 0
        li3 = set([a])
        while queue:
            day+=1
            for _ in range(len(queue)):
                x = queue.popleft()
                if x==b:
                    return day
                for n in [x+1, x-1, x*2]:
                    if b==n:
                        return day
                    if(0<= n <100001 and n not in li3):
                        queue.append(n)
                        li3.add(n)
            #print(queue)
        return day
print(bfs(a,b))