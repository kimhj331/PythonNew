def creat_student(name, korean, math, eng, sci):
    return{
        "name" : name,
        "korean" : korean,
        "math" : math,
        "eng" : eng,
        "sci" : sci
    }

def student_get_sum(student):
    return student["korean"]+student["math"]+student["eng"]+student["eng"]

def student_get_avg(student):
    return student_get_sum(student)/4

def student_to_string(student):
    return "{}\t{}\t{}\t".format(
        student["name"],
        student_get_sum(student),
        student_get_avg(student)
        )

students = [
   creat_student("윤인성",87,98,88,95),
   creat_student("연하진",87,98,88,95),
   creat_student("구지연",87,98,88,95),
   creat_student("나선주",87,98,88,95),
   creat_student("윤아린",87,98,88,95),
   creat_student("윤명월",87,98,88,95),
]

print("이름","총점","평균",sep="\t")


for student in students:
    print(student_to_string(student))