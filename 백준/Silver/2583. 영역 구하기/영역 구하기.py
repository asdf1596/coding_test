import sys
from collections import deque
queue = deque()
def mapPrint(map1):
    print("=================")
    for i in map1:
        print(i)
    print("===========")
a,b,c= map(int, sys.stdin.readline().split())
map1 = [[0 for _ in range(b)] for _ in range(a)]
for i in range(c):
    d,e,f,g = map(int, sys.stdin.readline().split())
    for j in range(d,f):
        for k in range(e,g):
            map1[k][j] = 1
            #print(k,j)
li2 = [[-1,0],[0,-1],[1,0],[0,1]]
ans = []
#mapPrint(map1)
for i in range(a):
    for j in range(b):
        if map1[i][j] == 0:
            queue.append([i,j])
            try1 = 1
            map1[i][j] = 1
            while queue:
                for _ in range(len(queue)):
                    y,x = queue.popleft()
                    for ny, nx in li2:
                        if(0<= ny+y <a and 0<= nx+x <b):
                            if(map1[ny+y][nx+x] == 0):
                                map1[ny+y][nx+x] = 1
                                queue.append([ny+y, nx+x])
                                try1+=1
                                #print(ny+y,nx+x)
            ans.append(try1)
#mapPrint(map1)
print(len(ans))
ans.sort()
for i in ans:
    print(i, end = " ")