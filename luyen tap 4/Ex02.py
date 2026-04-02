#hinh 1
n = int(input("Nhập n: "))

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
# hinh 2
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
#hinh 3
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
#hinh v4
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
#hinh 5
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(i):
        print("*", end=" ")
    print()
#hinh 6
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
#hinh 7
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
#hinh 8
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
#hinh 9
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end=" ")
    print()
#hinh 10
for i in range(n):
    for j in range(n):
        if j == i or j == n - i - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()