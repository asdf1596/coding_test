a = input()
a = int(a)
if(100<=a or a>=90):
    b = "A"
elif(89<=a or a>=80):
    b = "B"
elif(79<=a or a>=70):
    b = "C"
elif(69<=a or a>=60):
    b = "D"
else:
    b = "F"
print(b)