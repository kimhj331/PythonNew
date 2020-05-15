with open("./data/result.txt","r") as f:
    for line in f:
        (name, weight, height)=line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight)/(int(height) *int(height))*10000
        result=""
        if 25 <= bmi:
            result="과체중"
        elif 18.5 <= bmi:
            result="정상 체중"
        else:
            result="저체중"

        print('\n'.join([
            f"이름 : {name}",
            f"몸무게 : {weight}",
            f"키 : {height}",
            f"BMI : {bmi:,.2f}",
            f"결과 : {result}"

        ]))
        print()
    