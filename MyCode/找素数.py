
sushu = list(range(2,101))

for a in range(2,101):
    b = range(2,a)
    for c in b[:]:
        if a%c ==0:
            sushu.remove(a)
            break
print(sushu)