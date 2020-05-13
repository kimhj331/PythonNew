#반복문
# for i in range(5):
#     print("출력")

arr=[273,32,103,57,52]

for item in arr:
    print(item)


arr2=[1,2,1,3,4,1,5,6,7,8,9]

for item in arr2:
    if(item == 1):
        arr2.remove(1)


print(arr2)