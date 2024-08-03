a = list(map(int, list(input())))
a.sort(reverse=True)
b = [print(i, end = "") for i in a]