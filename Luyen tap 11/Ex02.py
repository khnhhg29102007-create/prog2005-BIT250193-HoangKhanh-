def binary_search(arr, x):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

arr = []
for i in range(5):
    arr.append(input(f"Nhập chuỗi {i + 1}: "))

arr.sort()
print("Mảng sau sắp xếp:", arr)

x = input("Nhập chuỗi cần tìm: ")

result = binary_search(arr, x)

if result != -1:
    print("Tìm thấy tại vị trí:", result)
else:
    print("Không tìm thấy")