from urllib import request
from bs4 import BeautifulSoup
from flask import Flask

#name=system변수/ main이 실행됨 
app=Flask(__name__)

@app.route("/")

def hello():
    target = request.urlopen("https://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")
    soup = BeautifulSoup(target,"html.parser")
    output=""
    for location in soup.select("location"):
       output += "<h3>{}</h3>".format(location.select_one("city").string)
       output +="날씨: {}<br/>".format(location.select_one("wf").string)
       output +="최저/최고 기온: {}℃/{}℃"\
           .format(\
                location.select_one("tmn").string,\
                location.select_one("tmx").string\
            )

       output += "<hr/>"
    return output
    
app.run(host='192.168.0.12',debug=False)
    