class Bird:
    def intro(self):
        print("There are many types of birds.")
    def flight(self):
        print("Most of the birds can fly but some cannot.")
class Kaftar(Bird):
    def intro(self):
        print("kaftar is a type of birds.")

    def flight(self):
        print("kaftar can fly")

class Chicken(Bird):
    def flight(self):
        print("chicken cannot fly.")

obj_bird = Bird()
obj_kaftar = Kaftar()
obj_chicken = Chicken()

# obj_bird.flight()
# obj_chicken.flight()
obj_kaftar.flight()