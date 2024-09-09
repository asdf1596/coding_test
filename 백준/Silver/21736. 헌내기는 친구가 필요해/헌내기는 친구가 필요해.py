import sys
from collections import deque
queue = deque()
def mapPrint(map1):
    for i in map1:
        print(i)
a,b = map(int, sys.stdin.readline().split())
map1 = []
for i in range(a):
    map1.append(list(sys.stdin.readline().strip()))
    if "I" in map1[i]:
        for j in range(len(map1[i])):
            if map1[i][j] == "I":
                queue.append([i,j])
                map1[i][j] = "X"
li2 = [[-1,0],[0,-1],[1,0],[0,1]]
li3 = deque()
ans = 0
while queue:
    for _ in range(len(queue)):
        y,x = queue.popleft()
        for ny, nx in li2:
            if(0<= ny+y <a and 0<= nx+x <b):
                if(map1[ny+y][nx+x] == "O"):
                    map1[ny+y][nx+x] = "X"
                    queue.append([ny+y, nx+x])
                elif(map1[ny+y][nx+x] == "P"):
                    map1[ny+y][nx+x] = "X"
                    queue.append([ny+y, nx+x])
                    ans+=1
#mapPrint(map1)
if ans == 0:
    print("TT")
else:
    print(ans)