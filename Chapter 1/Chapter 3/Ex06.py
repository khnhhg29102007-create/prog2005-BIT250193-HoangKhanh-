arr = list(map(int, input("Nhập danh sách số: ").split()))
n = len(arr)
swap_count = 0

for i in range(n):
    for j in range(0, n - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swap_count += 1

print("Danh sách tăng dần:", arr)
print("Số lần hoán đổi:", swap_count)