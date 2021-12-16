try:
    t = int(input())
    while t > 0:
        first, second, third = [i for i in input().split()]
        x, y = [i for i in input().split()]
        if x == first:
            print(x)
        elif y == first:
            print(y)
        elif x == second:
            print(x)
        else:
            print(y)

except: pass