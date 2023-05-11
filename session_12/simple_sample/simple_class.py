class simple_class():
    def __init__(self,name ,family,  age) -> None:
        self.name = name
        self.family = family
        self.age = age
    
    def say_hi(self):
        print("hi" , self.name , self.family)

    def report_age(self):
        print(self.family,"you have",self.age ,"years old.")