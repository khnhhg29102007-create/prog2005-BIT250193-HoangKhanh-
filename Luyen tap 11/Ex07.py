import csv

name = input("Tên: ")
age = input("Tuổi: ")
id_nv = input("ID: ")

with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(f"{name}, {age}, {id_nv}")

with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, id_nv])

print("Đã lưu file")