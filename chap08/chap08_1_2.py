class Student:
    count = 0

    def __init__(self, radius, name, korean, math, eng, sci):
        self.__radius = radius
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng
        self.sci = sci
        Student.count += 1
        print(f"{Student.count}번째 학생이 생성되었습니다.")
        pass

    def get_sum(self):
        return self.korean + self.math + self.eng + self.sci
    
    def get_average(self):
        return self.get_sum()/4
    
    def get_radius(self):
        return self.__radius

    def set_radius(self,value):
        return self.__radius=value
    
    #함수 재정의
    def __str__(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_average())
    

    


std_a=Student(5,"윤인성",87,98,88,95)



print(std_a)
print("생성한 학생 수 :",Student.count)
print("실행완료")