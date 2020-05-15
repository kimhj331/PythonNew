#  딕셔너리 선언
dic_a={
    "name":"어밴저스 엔드게임",
    "type":"히어로 무비",
    "cast":["아이언맨","타노스","토르","닥터스트레인지","헐크"],
    "director":["안소니 루소","조 루소"],
    "release":2019
}


# print(dic_a)
print(dic_a["director"][0])
dic_a["cast"].append("블랙위도우")

#새로운 값 추가
dic_a["까메오"]="스텐리"
print(dic_a)

del dic_a["release"]
    print(dic_a)

key="cast"
if key in dic_a:
    print("cast",dic_a["cast"])
else:
    print("키없음")