a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))
max_num = max(a, b, c)
min_num = min(a, b, c)
print("Số lớn nhất:", max_num)
print("Số nhỏ nhất:", min_num)
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình có nghiệm x =", x)
else:
    delta = b**2 - 4*a*c

    if delta > 0:
        x1 = (-b + delta**0.5) / (2*a)
        x2 = (-b - delta**0.5) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Nghiệm kép x =", x)
    else:
        print("Phương trình vô nghiệm")