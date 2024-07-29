from collections import deque
import sys
queue = deque()
a = int(input())
for i in range(a):
    b = sys.stdin.readline().strip().split()
    if(len(b) != 1):
        b,c = b[0][0], b[1]
        queue.append(c)
    else:
        b = b[0]
        if b == "pop":
            if(len(queue) !=0):
                print(queue.pop())
            else:
                print(-1)
        elif b == "size":
            print(len(queue))
        elif b == "empty":
            print([1 if len(queue) == 0 else 0][0])
        else:
            if len(queue) == 0:
                print(-1)
            else:
                print(queue[len(queue)-1])