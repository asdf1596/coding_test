from sys import stdin
input = stdin.readline
SIZE = 1.86 * int(1e6)
no = 1
while True:
    S = int(input())
    if S == 0: break
    S = (S + 1) // 2
    S += S // 2
    print(f'File #{no}\nJohn needs {int((S + SIZE - 1) // SIZE)} floppies.\n')
    no += 1