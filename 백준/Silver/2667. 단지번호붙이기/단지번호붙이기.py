import sys
from collections import deque
queue = deque()
def mapPrint(map1):
    for i in map1:
        print(i)
a= int(sys.stdin.readline())
map1 = []
for i in range(a):
    map1.append(list(map(int, list(sys.stdin.readline().strip()))))
li2 = [[-1,0],[0,-1],[1,0],[0,1]]
ans = []
for i in range(a):
    for j in range(a):
        if map1[i][j] == 1:
            queue.append([i,j])
            try1 = 1
            map1[i][j] = 0
            while queue:
                for _ in range(len(queue)):
                    y,x = queue.popleft()
                    for ny, nx in li2:
                        if(0<= ny+y <a and 0<= nx+x <a):
                            if(map1[ny+y][nx+x] == 1):
                                map1[ny+y][nx+x] = 0
                                queue.append([ny+y, nx+x])
                                try1+=1
                                #print(ny+y,nx+x)
            ans.append(try1)
#mapPrint(map1)
print(len(ans))
ans.sort()
for i in ans:
    print(i)