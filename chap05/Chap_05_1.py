#함수의 기본

def print_3_times():
    print("안녕하세요")
    print("hello")
    print("봉주르")

# def print_n_times(value, n=2):
#     for i in range(n):
#         print(value,end="")

# def print_n_times(value):
#     for i in range(10):
#         print(value,end="")        

def print_n_times(*values,n=1):
    for i in range(n):
        for value in values:
            print(value)
        print()

def multi_all(start,end):
    output = 1
    for i in range(1,end+1):
        output *=i
    return output

print(f"0 to 100 ={multi_all(0,100):,d}")
