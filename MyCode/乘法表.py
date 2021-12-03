
for a in range(1,10):
    for b in range(1,a+1):
        c = a*b
        if len(str(c))==1:
            print(str(a) + '*' + str(b) + '=' + str(c) + '   ',end = '')
        else:
            print(str(a) + '*' + str(b) + '=' + str(c) + '  ',end = '')
    print()
