# 마지막 테스트 파이썬
import json

# print(dic_mcu)
# with open("./data/mcu_movies.json", "w", encoding="UTF-8") as mcu_list:
#   json.dump(dic_mcu, mcu_list, ensure_ascii=False)

with open("./mcu_movies.json", "r", encoding="UTF-8") as mcu_list:
  dic_mcu = json.load(mcu_list)

# 문제 1번
# 페이즈가 2인 마블 시네마틱 유니버스 영화면 뽑기
def Phase(valuse):
    for movie in dic_mcu:
        if valuse == movie["시리즈"]:
            print("{} ( {} )".format(movie["영화명"],movie["개봉일"]))

Phase("페이즈2")

# 문제 2번
# 박스오피스가 450000000 이상인 영화들의 감독이름 리스트와 전체 합계금액, 평균 박스오피스 구하기



def pro_list():
    count=0
    a=[]
    dal=0
    for movie in dic_mcu:
        if movie["박스오피스"]>=450000000:
            a.append(movie["감독"])
            dal+=movie["박스오피스"]
            count+=1
    print("감독 리스트:\n",list(set(a)))
    print(f"총 박스오피스 합계 ${dal:,d}")
    print(f"평균 박스오피스 ${int(dal/count):,d}")

pro_list()