#딕셔너리 선언
dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임",
    "ingredient":["망고","설탕","페타주아황산나트륨","치자황색소"],
    "origin" : "Philipine"
}

vlaue = dictionary.get("price")
#값이 없으면 non으로 나옴
print("값:",vlaue)

if vlaue == None:
    print("error")
    
for key in dictionary:
    print("값:",dictionary.get(key))
