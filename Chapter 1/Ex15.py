for i in range(3):
    name = input("Nhap ten: ")
    toan = float(input("Toan: "))
    ly = float(input("Ly: "))
    hoa = float(input("Hoa: "))

    dtb = (toan + ly + hoa) / 3
    print(name, "- DTB:", round(dtb, 2))