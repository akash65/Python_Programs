class Student:
    def __init__(self,name, roll_no, age, degree, gpa):
        self.name = name
        self.roll_no = roll_no
        self.age = age
        self.degree = degree
        self.gpa = gpa


    #fucntions for student attendence
    def attendence(self):
        if self.gpa >= 6.5 :
            return True