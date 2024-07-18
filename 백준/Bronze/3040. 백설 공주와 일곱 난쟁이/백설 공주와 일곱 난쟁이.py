# 입력받기
li1 = [int(input()) for _ in range(9)]

# 전체 합 계산
total_sum = sum(li1)

# 필요한 두 숫자의 합 계산
target_sum = total_sum - 100

# 두 난쟁이 찾기
found = False
for i in range(9):
    for j in range(i + 1, 9):
        if li1[i] + li1[j] == target_sum:
            # 두 숫자를 제거
            num1, num2 = li1[i], li1[j]
            li1.remove(num1)
            li1.remove(num2)
            found = True
            break
    if found:
        break

# 결과 출력
for num in li1:
    print(num)
