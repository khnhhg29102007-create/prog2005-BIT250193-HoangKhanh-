#cach 1
s = input("Nhập chuỗi: ")
print("Đảo ngược:", s[::-1])

#cach 2
s = input("Nhập chuỗi: ")
rev = ""

for char in s:
    rev = char + rev

print("Đảo ngược:", rev)