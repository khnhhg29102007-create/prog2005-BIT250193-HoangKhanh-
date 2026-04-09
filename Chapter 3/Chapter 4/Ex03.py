def kiem_tra_key(d, key):
    if key in d:
        print("Key tồn tại")
    else:
        print("Key không tồn tại")

d = {"a": 1, "b": 2, "c": 3}
kiem_tra_key(d, "b")
kiem_tra_key(d, "x")