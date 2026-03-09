n = int(input("Nhập n: "))
print("tam giác :")

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("tam giác 2 :")
for i in range(1, n+1):
    if i == 1:
        print(" "*(n-1) + "*")
    elif i == n:
        print("* "*n)
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*")