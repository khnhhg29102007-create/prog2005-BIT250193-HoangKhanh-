n = int(input("Nhập n: "))
#hinh 1
for i in range(n):
    for j in range(n):
        print(1, end=" ")
    print()
#hinh 2
for i in range(n):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()
#hinh 3
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#hinh 4
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#hinh 5
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
#hinh 6
for i in range(n):
    for j in range(n):
        if i == j:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()
#hinh 7
for i in range(n):
    for j in range(n):
        if i == j or i + j == n - 1:
            print(j + 1, end=" ")
        else:
            print(" ", end=" ")
    print()
#hinh 8
for i in range(1, n + 1):
    print(" " * (n - i), end="")

# hinh tăng
    for j in range(1, i + 1):
        print(j, end=" ")

#hinh giam
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()
#hinh 9
for i in range(n, 0, -1):
    print(" " * (n - i), end="")

# tăng
    for j in range(1, i + 1):
        print(j, end=" ")

# giảm
    for j in range(i - 1, 0, -1):
        print(j, end=" ")

    print()