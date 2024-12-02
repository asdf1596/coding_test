for i in range(3):
    a,b,c,d,e,f = map(int, input().split())
    d = (d*3600+e*60+f)-(a*3600+b*60+c)
    print(d//3600, (d%3600)//60, d%60)