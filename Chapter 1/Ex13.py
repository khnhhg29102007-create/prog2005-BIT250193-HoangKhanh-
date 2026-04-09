try:
    a = int(input())
    b = int(input())
    print(a / b)
except ZeroDivisionError:
    print("Khong chia duoc cho 0")
except:
    print("Du lieu khong hop le")