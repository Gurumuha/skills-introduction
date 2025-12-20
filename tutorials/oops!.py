class House:
    sofa ="red"
    bed ="white"
    kitchen ="cream"
obj1 =House()
obj2 =House()
print(f"You  have a {obj1.sofa} sofa, a {obj1.bed} bed, and a {obj1.kitchen} kitchen.")


print(obj2.sofa)

class Children:
    def __init__(self, name, age, grade):
        self.name =name
        self.age =age
        self.grade =grade
fBorn =Children("Kelly K", 8, "Grade 3")
sBorn =Children("Rocky S. Laston", 4, "PP2")
sBorn2 =Children("Amie J.", 4, "PP2")
print(f"You first child is {fBorn.name}, age: {fBorn.age}, who is in {fBorn.grade}.")
print(f"You second child is {sBorn.name}, age: {sBorn.age}, who is in {sBorn.grade}.")
print(f"You second child is {sBorn2.name}, age: {sBorn2.age}, who is in {sBorn2.grade}. She's a twin sister to Richard.")

class Flock:
    def __init__(me, name, breed, origin):
        me.name =name
        me.breed =breed
        me.origin =origin
sheep1 =Flock("Nyamita", "Dorper", "Laikipia")
print(f"You have a pedigree {sheep1.breed} from {sheep1.origin} called {sheep1.name}.")

class Cars:
    def __init__(self, brand, color, yom):
        self.brand =brand
        self.color =color
        self.yom =yom
    def display_info(self):
        print(f"This is a {self.color} {self.brand} made in {self.yom}.")
car1=Cars("Mercedes Benz AMG", "white", 2024)
car1.display_info()
class Visitors:
    def __init__(self, name):
        self.name =name
    def greet(self):
        return f"Hello, {self.name}!"
    def introduce(self):
        message =self.greet()
        print(message + " Feel most welcome to this conference.")
visit1 =Visitors("Amiru")
visit1.introduce()
class Seminar:
    def __init__(self, visitor_name):
        self.visitor_name =visitor_name
    def greet(self):
        return f"Hello {self.visitor_name}!"
    def introduce(self):
        intro = self.greet()
        print(f"{intro} How are you feeling today?")
visitor1= Seminar("Amolo")

visitor1.introduce()

#class instance v. property
class Phones:
    model ="Nokia" #property-directly declared in the class
    def __init__(self, type, cost):
        self.type =type
        self.cost =cost #these are instances-declared as parameters of 'self'
phone1 =Phones("XP", 2500)
phone2 =Phones("Windows", 1000)
print(f"This is a {phone1.model}-{phone1.type} which costs KES. {phone1.cost}")
print(f"This is a {phone2.model}-{phone2.type} which costs KES. {phone2.cost}")

