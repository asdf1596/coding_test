import sys
from collections import deque
queue = deque()
def mapPrint(map1):
    for i in map1:
        for j in i:
            print(j, end = " ")
        print("")
a,b = map(int, sys.stdin.readline().split())
map1 = []
for i in range(a):
    map1.append(list(map(int, sys.stdin.readline().split())))
    if 2 in map1[i]:
        for j in range(len(map1[i])):
            if map1[i][j] == 2:
                queue.append([i,j])
                map1[i][j] = 0
li2 = [[-1,0],[0,-1],[1,0],[0,1]]
li3 = deque()
day = 1
while queue:
    for _ in range(len(queue)):
        y,x = queue.popleft()
        for ny, nx in li2:
            if(0<= ny+y <a and 0<= nx+x <b):
                if(map1[ny+y][nx+x] == 1):
                    if day == 1:
                        map1[ny+y][nx+x] = -2
                        li3.append([ny+y, nx+x])
                    else:
                        map1[ny+y][nx+x] = day
                    queue.append([ny+y, nx+x])
    day+=1
for i in range(len(map1)):
    for j in range(len(map1[0])):
        if map1[i][j] == 1:
            map1[i][j] = -1
for _ in range(len(li3)):
    y,x = li3.popleft()
    map1[y][x] = 1
mapPrint(map1)
#print(li3)