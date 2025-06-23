li = [input() for _ in range(9)]

tiger = li.count('Tiger')
lion = li.count('Lion')

if lion < tiger:
    print('Tiger')
else:
    print('Lion')