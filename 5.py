num = []
arr = []

#main
while True:
    n = input('Dữ liệu cần nhập cho mảng: ')
    if (n.isdigit() == True):
        num.append(int(n))
    else:
        print('Dữ liệu đã nhập thành công')
        break
print(num)

x = int(input("Nhập số cần tìm: "))

count = 0
flag = 0
while(count < len(num)):
        if(x == num[count]):
            arr.append(count)
            flag = 1
        count += 1

if(flag == 1):
    print("Giá trị", x, "xuất hiện đầu tiên trong danh sách tại vị trí:",arr[0])
    print("Giá trị", x, "xuất hiện trong danh sách tại các vị trí:",arr)
else:
    print("Không có giá trị", x, "xuất hiện trong danh sách")