li1 = [380,425,450,495,570,590,620,781]
li2 = ["Violet","Indigo","Blue","Green","Yellow","Orange","Red"]
a = int(input())
for i in range(len(li1)-1):
    x,y = li1[i],li1[i+1]
    if x<=a<y:
        print(li2[i])