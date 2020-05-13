# list_a=[1,2,3]
# list_b=[4,5,6]
# list_c=list_a+list_b

# print("# 리스트")
# print("list_a=",list_a)

# print("# 리스트 기본 연산자")
# print("list_a + list_B =",list_c)
# print("list_B *4",list_b*4)


# print("# 길이 구하기")
# print("len(list_a)=",len(list_c*3))

# print("# 마지막 요소 출력")
# print(list_c[len(list_c)-1])

# print("# 첫번째 요소 출력")
# print(list_c[-len(list_c)])


list_a=[1,2,3]
list_c=[4,5,6]

list_a.append(4)
list_a.append(5)

list_a.extend(list_c)
print(list_a)

list_a.append("마지막")
print(list_a)

list_a.insert(len(list_a),"진짜 마지막")
print(list_a)

# print("# del 요소 삭제1")
# del list_a[1]
# print("del list_a[1]:",list_a)

# print("# pop 요소 삭제2")
# list_a.pop(0)
# print("pop(0):",list_a)

# print("# pop 요소 삭제2")
# del list_a[:3]
# print(list_a)
print(2 in list_a)
list_a.remove(2)
print(list_a)

print(2 not in list_a)

list_a.clear()
print(list_a)