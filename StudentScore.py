class Person():
    def __init__(self,name,role):
        self.name = name
        self.role = role

class Student(Person):
    def __init__(self,student_id,name,role):
        self.student_id = student_id
        super().__init__(name,role)
        self.grades={}
    def add_grade(self,grade,lesson):
        self.grades[lesson]=grade

class Teacher(Person):
    def __init__(self,teacher_id,name,role):
        super().__init__(name,role)

class Lesson():
    def __init__(self,lesson_id,lesson_title,credit):
        self.lesson_id = lesson_id
        self.lesson_title = lesson_title
        self.credit = credit


