def power_last_digit(base, exponent):
    result = 1
    base %= 10
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % 10
        base = (base * base) % 10
        exponent //= 2
    
    return result
num_cases = int(input())
results = []

for _ in range(num_cases):
    b, c = map(int, input().split())
    last_digit = power_last_digit(b, c)
    if last_digit == 0:
        last_digit = 10
    results.append(last_digit)
for result in results:
    print(result)
