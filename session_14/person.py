class Person:
    # constructor
    def __init__(self, name, family):
        self.name = name
        self.family = family
    def say_hello(self):
        return "Hello everyone"
    
    def introduce_yourself(self):
        return f"my name is {self.name} {self.family}"

    def __str__(self) -> str:
        return "I'm a person"


