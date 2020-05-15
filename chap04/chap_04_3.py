# for i in range(5,10):
#     print(i," = 반복변수")

# arr=[11,22,33,44,55,66]

# for i in range(len(arr)):
#     print(i+1,"번째 arry값", arr[i])


# 역반복문

# for i in range(10, 0,-1,-1):
#     print(i)

# while True:
#     print(".",end="")

# i=0
# while i<10:
#     print("%d번째 반복입니다"%(i+1))
#     i+=1
#     #반복종료
#     input_text = input("> 종료합니까?(y)")
#     if input_text in ["y","Y"]:
#         print("반복 종료")
#         break

number = [5,15,6,60,7,25]
for num in number:
    if num<10:
        continue

    print(num)