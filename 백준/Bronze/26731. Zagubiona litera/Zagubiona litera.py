import string
t = input()
for a in string.ascii_uppercase :
    if a not in t :
        print(a)
        break