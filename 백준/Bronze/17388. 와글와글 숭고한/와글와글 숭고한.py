a,b,c = map(int, input().split())
if sum([a,b,c]) <100:
  if min(a,b,c) == a:
    print("Soongsil")
  elif min(a,b,c) == b:
    print("Korea")
  elif min(a,b,c) == c:
    print("Hanyang")
else:
  print("OK")