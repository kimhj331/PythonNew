def factorial(n):
    output=1

    if n==0:
         return 1
    else:
        return n *factorial(n-1)
    # for i in range(1,n+1):
    #     output *=i
    # return output

counter = 0

def fibo(n):
    global counter
    counter += 1

    if(n==1):
        return 1
    if(n==2):
        return 2
    else:
        return fibo(n-1) + fibo(n-2)


# print(f"{factorial(10)}")
print(f"fibo={fibo(35)},{counter}번")

