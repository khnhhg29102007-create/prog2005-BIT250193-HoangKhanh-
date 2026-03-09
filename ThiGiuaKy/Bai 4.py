n = int(input("Nhập n: "))
a = []

for i in range(n):
    x = int(input("Nhập phần tử: "))
    a.append(x)

for i in range(n-1):
    for j in range(n-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print("Bước", i+1, ":", a)