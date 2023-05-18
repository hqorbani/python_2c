# inheritance 
from person import Person

class Personel(Person):
    def __init__(self, name, family  , code):
        super().__init__(name, family)
        self.code = code
    def tell_me_code(self):
        return f"my code is {self.code}"
    
    def __str__(self) -> str:
        # return "student class"
        return super().__str__()

personel_1 = Personel("Mina", "Minaee", "123654")
print(personel_1.introduce_yourself())
print(personel_1.tell_me_code())