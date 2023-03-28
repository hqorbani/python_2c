from Person import Person
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
    
    def choose_class(self):
        pass