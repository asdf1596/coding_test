a = int(input())
print("abcdefgh"[(a-1) % 8] + str((a+7) // 8))