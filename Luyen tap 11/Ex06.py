n = int(input("Nhập số người: "))
d = {}

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    d[name] = age

avg = sum(d.values()) / n
print("Tuổi trung bình:", avg)

items = list(d.items())

for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j
    items[i], items[max_idx] = items[max_idx], items[i]

print("Sau sắp xếp:", items)