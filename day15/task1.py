class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    def summary(self):
        print("Book Summary:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Published: {self.year}")
b1 = Book("Atomic Habits", "James Clear", 2018)
b1.summary()
