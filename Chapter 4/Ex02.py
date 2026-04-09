def tinh_diem_trung_binh(danh_sach_sv):
    tong = sum(danh_sach_sv.values())
    so_luong = len(danh_sach_sv)
    return tong / so_luong

sinh_vien = {
    "An": 8,
    "Binh": 7,
    "Chi": 9
}

print("Điểm trung bình:", tinh_diem_trung_binh(sinh_vien))