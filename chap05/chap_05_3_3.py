from random import *

hanguls=list("민경수진욱상은채섭철건예")

with open("./data/result.txt","w") as f:
    f.write("이름, 몸무게, 키\n")

    for i in range(1000):
        name = choice(hanguls)+choice(hanguls)
        weight = randrange(40,100)
        height = randrange(150,200)

        f.write(f"{name}, {weight}, {height}\n")

print("파일생성이 완료되었습니다")