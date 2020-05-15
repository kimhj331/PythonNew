# def power(item):
#     return item*item

# def under_3(item):
#     return item < 3
power = lambda item: item*item
under_3 = lambda x: x<3


lists=[1,2,3,4,5]

output = map(power,lists)
print(output)
print(list(output))

output_b = filter(under_3,lists)
print(output_b)
print(list(output_b))