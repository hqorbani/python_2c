# inheritance 
from person import Person
class Student(Person):
    def __init__(self, age , name , family) -> None:
        self.age = age
        super().__init__(name , family)
    
    def say_your_age(self):
        return f"I have {self.age} years old"
        
    def __str__(self) -> str:
        # return "student class"
        return super().__str__()


ali = Student(13 , "Hamzeh" , "Qorbani")

# print(ali.say_your_age())
# print(ali.say_hello())
# print(ali.introduce_yourself())
print(ali)