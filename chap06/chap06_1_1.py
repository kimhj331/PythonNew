# # try except 연습

try:
    radius = int(input("정수입력 >"))
    print(f"원의 반지름 : {radius}")
    print(f"원의 둘레 : {2*3.14159265* radius:.2f}")
    print(f"원의 넓이 : {3.14159265 *radius *radius :.2f}")
    pass
except Exception as e:
    print("뭔가 잘못되었습니다")
    print(f"type(e):{type(e)}")
    print(f"exception:{e}")
    pass
else:
    print("에러가 발생하지 않았습니다")
finally:
    print("프로그램 종료")
   


# lists = ['11','22','33','44','하이','55']
# outputs = []

# for item in lists:
#     try:
#         float(item)
#         outputs.append(item)
#         pass
#     except:
#         pass
   

# print(outputs)


# try:
#     f=open("./data/basic.txt","w")
#     f.write("TEST!!")
# except Exception as e:
#     print(e)
# finally:
#     f.close()

# print("파일 클로즈?", f.closed)

# def test():
#     print("test() start")
#     try:
#         print("test() try")
#         return
#         print("test() after return")
#         pass
#     except :
#         print("test() except")
#         pass
#     else : 
#         print("test() else")
#     finally:
#         print("test() finally")
    
#     print("test() end")

# test()