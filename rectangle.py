W, H, x, y, r = map(int, input().split())
if W > x + r and H > y + r and x - r > 0 and y - r > 0:
    print("Yes")
elif W < x + r:  
    print("NO")
elif H < y + r:
    print("NO")
elif x  < r:
    print("NO")
elif y -  r:
    print("NO")