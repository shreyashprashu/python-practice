class Student:
    def __init__(self,name, age, sex, grade,is_promoted):
        self.name=name
        self.age=age
        self.sex=sex
        self.grade=grade
        self.is_promoted=is_promoted

    def on_scholarship(self):
        if self.grade >= 7:
            return True
        else:
            return False
