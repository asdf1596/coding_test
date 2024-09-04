import sys
from collections import deque
queue = deque()
def mapPrint(map1):
    for i in map1:
        print(i)
    print("==============================")
li2 = [[-1,0],[0,-1],[1,0],[0,1]]
a,b  = map(int, sys.stdin.readline().split())
map1 = []
for i in range(a):
    map1.append(list(map(int, map(int, list(sys.stdin.readline().strip())))))
queue.append([a-1,b-1])
#mapPrint(map1)
day = 0
while queue:
    for _ in range(len(queue)):
        y,x = queue.popleft()
        if x==0 and y==0:
            queue = []
            break
        for ny, nx in li2:
            if(0<= ny+y <a and 0<= nx+x <b):
                if(map1[ny+y][nx+x] == 1):
                    map1[ny+y][nx+x] = 0
                    queue.append([ny+y, nx+x])
                map1[y][x] = -1
    #print(queue)
    day+=1
print(day)