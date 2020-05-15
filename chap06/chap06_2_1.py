lists = [52,273,32,72,100]

try:
    num=int(input("정수 입력>"))
    print(f"{num}번째 요소 :{lists[num]}")
    예외.발생()
except ValueError as ex:
    print("[ERROR]정수를 입력 해 주세요")
    print(ex)
except IndexError as ex:
    print("[ERROR]인덱스 에러 발생")
    print(ex)
# 부모 exception은 항상 마지막에 적어준다
except Exception as ex:
    print(ex)