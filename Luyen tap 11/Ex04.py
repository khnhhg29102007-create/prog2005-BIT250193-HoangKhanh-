import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

arr = [1, 2, 3, 4, 5]

arr.append(int(input("Nhập số thêm: ")))

k = int(input("Nhập k: "))
print("Số lần xuất hiện:", arr.count(k))

print("Tổng số nguyên tố:", sum(x for x in arr if is_prime(x)))

arr.sort()
print("Danh sách sau sắp xếp:", arr)

arr.clear()
print("Danh sách sau khi xóa:", arr)