from collections import deque
from copy import deepcopy
queue = deque()
a,b = map(int, input().split())
def mapPrint(map1):
    for i in map1:
        print(i)
    print("==============================")
def check(queue, map1, a, b):
    li2 = [[-1,0],[0,-1],[1,0],[0,1]]
    while queue:
        for _ in range(len(queue)):
            y,x = queue.popleft()
            for ny, nx in li2:
                if(0<= ny+y <a and 0<= nx+x <b):
                    if(map1[ny+y][nx+x] == 0):
                        map1[ny+y][nx+x] = 2
                        queue.append([ny+y, nx+x])
    ans = 0
    #mapPrint(map1)
    for i in range(len(map1)):
        for j in range(len(map1[0])):
            if(map1[i][j] == 0):
                ans+=1
    return ans

map1 = []
for i in range(a):
    map1.append(list(map(int, input().split())))
li1 = []
ansli = []
for i in range(a):
    for j in range(b):
        if(map1[i][j] == 2):
            queue.append([i,j])
        elif(map1[i][j] == 0):
            li1.append([i,j])
for i in range(len(li1)-2):
    for j in range(i+1, len(li1)-1):
        for k in range(j+1, len(li1)):
            map2 = deepcopy(map1)
            map2[li1[i][0]][li1[i][1]] = 1
            map2[li1[j][0]][li1[j][1]] = 1
            map2[li1[k][0]][li1[k][1]] = 1
            #mapPrint(map2)
            ansli.append(check(deepcopy(queue), map2, a, b))
print(max(ansli))
