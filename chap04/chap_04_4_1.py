# temp=reversed([1,2,3,4,5,6])

# for i in temp:
#     print("첫번째 반복문{}".format(i))

# for i in temp:
#     print("두번째 반복문{}".format(i))

# 필요한 시점에 reversed를 사용해야함

# numbers=[1,2,3,4,5,6]

# for i in reversed(numbers):
#     print("첫번째 반복문{}".format(i))
# for i in reversed(numbers):
#     print("두번째 반복문{}".format(i))

# enumerate의 사용

example_list = ["itemA","itemB","itemC","itemD"]
#단순출력
print(example_list)
print()
#enumerate()출력
print(enumerate(example_list))
print()
#enumerate() list 출력
print(list(enumerate(example_list)))

#반복문 조합
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}".format(i,value))

