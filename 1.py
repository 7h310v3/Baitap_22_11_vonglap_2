import math

mydict = {}

n = int(input("Nhập số nguyên dương N: "))

while(n < 1):
    print("Nhập sai, xin nhập lại!")
    n = int(input("Nhập số nguyên dương N: "))

count = 1

while(count <= n):
    mydict[count] = math.log(count)
    count += 1

print(mydict)