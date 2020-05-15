# yield 는 출력하고 다음단계로 넘어감

def test():
    print("A 지점 통과")
    yield 1
    print("B 지점 통과")
    yield 2
    print("C 지점 통과")
    yield 3
# print(list(test()))

output= test()


print("D 지점 통과")
a = next(output)
print(a)


print("E 지점 통과")
b = next(output)
print(b)

#에러발생 next를 호출할 때 마다 yield값을 할당. 더이상 할당 할 값이 없음
print("f 지점 통과")
c = next(output)
print(c)

num=[1,2,3,4,5]
for i in num:
    print("::".join([num[i])])