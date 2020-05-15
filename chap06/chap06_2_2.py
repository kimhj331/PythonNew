
# try:
#     num = int(input("정수 입력 > "))
#     if num > 0:
#         raise NotImplementedError("0보다 큼 : 구현안됨")
#     else:
#         raise NotImplementedError("0보다 작음")
#     pass
# except NotImplementedError as ex:
#     print(ex)
#     pass
# except Exception as ex:
#     print(type(ex))
#     print(ex)
# finally:
#     print("무조건 실행")
#     pass

a,b = map(int,input().split())
