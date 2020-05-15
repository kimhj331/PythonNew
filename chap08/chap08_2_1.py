class Student:
    def __init__(self, name, korean, math, eng, sci):
        self.name = name 
        self.korean = korean
        self.math = math
        self.eng = eng
        self.sci = sci
        pass
    def get_sum(self):
        return self.korean + self.math + self.eng + self.sci
    
    def get_average(self):
        return self.get_sum()/4
    

students = [
    Student("윤인성",87,98,88,95),
    Student("연하진",87,98,88,95),
    Student("구지연",87,98,88,95),
    Student("나선주",87,98,88,95),
    Student("윤아린",87,98,88,95),
    Student("윤명월",87,98,88,95)
] 

std=Student("윤인성",87,98,88,95)
print("std의 클래스:",isinstance(std,Student))