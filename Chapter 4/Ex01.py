def xu_ly_tuple(t):
    tong = sum(t)
    lon_nhat = max(t)
    nho_nhat = min(t)
    return tong, lon_nhat, nho_nhat

t = (1, 5, 3, 9, 2)
print(xu_ly_tuple(t))