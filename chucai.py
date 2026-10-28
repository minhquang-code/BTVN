c = input("Nhập vào một chữ cái in hoa: ")
if c == 'A':
    print('z')
else:
    c_thuong = c.lower()
    ket_qua = chr(ord(c_thuong) - 1)
    print(ket_qua)