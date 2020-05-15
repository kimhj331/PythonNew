PI=3.14159265

# print("모듈")
# print(__name__)

def number_input():
    try:
        output=float(input("숫자입력>"))
        return output
    except ValueError as ex:
        print(ex)
        pass
    except Exception as ex:
        print(ex)
   
def get_circumference(radius):
    return 2*PI*radius

def get_circle_area(radius):
    return PI*radius*radius

if __name__=="__main__":
    print(get_circumference(10))
    print(get_circle_area(10))