arr = list(map(int, input("Nhập danh sách: ").split()))
x = int(input("Nhập số cần tìm: "))

found = False
for i in range(len(arr)):
    if arr[i] == x:
        print("Tìm thấy tại vị trí:", i)
        found = True
        break

if not found:
    print("Không tìm thấy")