import sys
import os
import datetime
from urllib import request

# print(sys.argv)
# print(sys.getwindowsversion())
# print(sys.copyright)
# print(sys.version)

# print("OS: ", os.name)
# print("폴더: ", os.getcwd())
# print("files: ", os.listdir())

# os.mkdir("hello")
# os.rmdir("hello")

# os.system("dir")

# cur=datetime.datetime.now()
# print(f"{cur.year}년/{cur.month}월/{cur.day}일")

target = request.urlopen("https://google.com")
output = target.read()

print(output)


