
for a in range(1,10001):
    d = 0
    for b in range(1,a):
        c = a%b
        if c==0:
            d = b + d
    if d == a:
        print(a)
