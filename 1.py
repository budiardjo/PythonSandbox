for i in range(int(input())):
      a,b,c = map(str,input().split())
      x,y = map(str,input().split())
      if a == x:
           print(x)
      elif a == y:
           print(y)
      elif b==x:
           print(x)
      else:
           print(y)