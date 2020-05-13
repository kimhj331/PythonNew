number = input("수입력 :")

last_num = number[-1]


if last_num in "02468" :
    print("%s는(은) 짝수입니다"%(number))    
    
if last_num in "13579" :
    print("%s는(은) 홀수입니다"%(number))    


print("%d %d %.2f"%(1,2,3))
