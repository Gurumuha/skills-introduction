class Booklist: #detailed breakdowns to come later
    def __init__(self, name ):
        self.name =name
        self.title = [] #entails appending and removing list items using functions/methods in a class
    def addBook(self, title):
        self.title.append(title)
        print(f"Added {title} to the list of {self.name}!")
    def removeBook(self, title):
        if title in self.title:
            self.title.remove(title)
            print(f"Removed {title} from the list of {self.name}!")
    def showBooks(self):
        print(f"Book List: {self.name.upper()}")
        for title in self.title:
            print(title)
my_genre=Booklist("Novels")
my_genre.addBook("A man of the People")
my_genre.addBook("The Old Man and the Sea")
my_genre.addBook("The Land Without Thunder and Other Stories")

my_genre.showBooks()
#more on oop
class Car:
    def drive (self, speed):
        self.speed =speed
        print(f"The car is moving at {self.speed} km/hr.")
        if self.speed <=50:
            print("You are cruising!")
        else:
            print("You should watch out for other road users.")
    def radio (self):
        print("The music is on!")
    def fuel (self):
        print("Check the fuel gauge to see if we should stopover for fuel.")
ford =Car()
ford.drive(60)
ford.radio()
ford.fuel()
