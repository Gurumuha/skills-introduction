class Booklist:
    def __init__(self, name ):
        self.name =name
        self.title = []
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