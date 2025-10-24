nums = [0] * 49
flag = True

while True:
    n = int(input())
    # 탈출 조건
    if n == 0:
        break
    # 초기화
    flag = True
    nums = [0] * 49
    # 티켓 입력 및 값 저장
    for _ in range(n):
        tickets = list(map(int, input().split()))
        for ticket in tickets:
            nums[ticket - 1] += 1
    # 없는 숫자 있으면 flag 반전
    if 0 in nums:
        flag = False
    print("Yes" if flag else "No")