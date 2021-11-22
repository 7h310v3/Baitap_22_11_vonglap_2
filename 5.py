num = []

#nhập dữ liệu cho mảng
def enter_num():
    global num
    print('Nhập dữ liệu xong thì nhập (Done) hoặc (done)')
    while True:
        x = input('Dữ liệu cần nhập cho mảng: ').upper()
        if x == 'STOP':
            print('Dữ liệu đã nhập thành công')
            break
        num.append(float(x))





#chạy chương trình
enter_num()

print("Mảng trước khi sắp xếp")
print(num)
