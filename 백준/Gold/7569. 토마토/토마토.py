from collections import deque
a,b,c = map(int, input().split())
map1 = []
queue = deque()
def mapPrint(map1):
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            print(map1[i][j])
        print("-------------")
    print("=============")
li1 = [[0,-1,0],[0,0,-1],[0,1,0],[0,0,1],[1,0,0],[-1,0,0]]
for i in range(c):
    map1.append([])
    for j in range(b):
        map1[i].append(list(map(int, input().split())))
    for j in range(b):
        for k in range(a):
            if(map1[i][j][k] == 1):
                queue.append([i,j,k])
day = -1
while queue:
    for _ in range(len(queue)):
        z,y,x = queue.popleft()
        for nz,ny,nx in li1:
            if(0<= nz+z < c and 0<= ny+y < b and 0 <= nx+x < a):
                if(map1[nz+z][ny+y][nx+x] == 0):
                    map1[nz+z][ny+y][nx+x] = 1
                    queue.append([nz+z, ny+y, nx+x])
    day+=1
for i in range(c):
    for j in range(b):
        if 0 in map1[i][j]:
            day = -1
print(day)