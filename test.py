#arr = input("Nhập chuỗi: ").split(" ")
arr = ("     ahihi   thelove     dtnm   deptrai    ").split(" ")

print(len(arr))

while True:
    if(arr[0] == ""):
        del arr[0]
    else:
        break

while True:
    tmp = len(arr) - 1
    if(arr[tmp] == ""):
        del arr[tmp]
    else:
        break

while True:
    if(arr[0] == " "):
        del arr[0]
    else:
        break

for i in range(2, (len(arr)-1)):
    if(arr[i] == "" and arr[i-1] == ""):
        del arr[i]

print(len(arr))
print(arr)

print(type(arr))