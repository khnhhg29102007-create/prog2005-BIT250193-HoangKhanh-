for i in range(111, 16 ,-1):
    if i % 2 != 0:
        print(i)
        break
for n in range(17, 112):
    snt = True
    for i in range(2, n):
        if n % i == 0:
            snt = False
            break
    if snt:
        print(n)
