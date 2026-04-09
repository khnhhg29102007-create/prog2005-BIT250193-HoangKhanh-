def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
            count += 1
    return count

s = input("Nhập chuỗi: ")
print("Số nguyên âm:", count_vowels(s))