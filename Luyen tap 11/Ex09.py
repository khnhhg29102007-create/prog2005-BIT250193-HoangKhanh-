def nhap_ma_tran(hang, cot, ten):
    print(f"\nNhập ma trận {ten}:")
    matrix = []

    for i in range(hang):
        row = []
        for j in range(cot):
            while True:
                value = input(f"Phần tử [{i}][{j}]: ")

                if value.strip() == "":
                    print("Lỗi: Không được nhập giá trị trống!")
                else:
                    try:
                        row.append(float(value))
                        break
                    except:
                        print("Lỗi: Phải nhập số!")

        matrix.append(row)

    return matrix


def cong_ma_tran(A, B):
    hang = len(A)
    cot = len(A[0])

    C = []
    for i in range(hang):
        row = []
        for j in range(cot):
            row.append(A[i][j] + B[i][j])
        C.append(row)

    return C


def in_ma_tran(matrix, ten):
    print(f"\nMa trận {ten}:")
    for row in matrix:
        print(row)

try:
    hang = int(input("Nhập số hàng: "))
    cot = int(input("Nhập số cột: "))

    if hang <= 0 or cot <= 0:
        print("Lỗi: Kích thước phải > 0")
    else:
        A = nhap_ma_tran(hang, cot, "A")
        B = nhap_ma_tran(hang, cot, "B")

        C = cong_ma_tran(A, B)

        in_ma_tran(A, "A")
        in_ma_tran(B, "B")
        in_ma_tran(C, "C = A + B")

except:
    print("Lỗi: Nhập sai định dạng!")