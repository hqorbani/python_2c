class Person:
    def __init__(self,age,name,family):
        self.age = age
        self.name = name
        self.family = family

    def introduce_yourself(self):
        return "hello, I'm "+ self.name
    
    
    def __str__(self):
        return f"{self.name}_{self.family}_{self.age}"

first_person = Person(12,"Hamid" , "Borhani")
second_person = Person(31,"Hamideh" , "Borhaninia")

# print(first_person.age)
# print(first_person.name)
# print(first_person.introduce_yourself())
# hello_msg = second_person.introduce_yourself()
# print(hello_msg + " How are you? ")

print(first_person.introduce_yourself())