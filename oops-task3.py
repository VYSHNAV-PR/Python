class Book:
    def __init__(self,title,author,copies):
        self.title=title
        self.author=author
        self.copies=copies
    def display_info(self):
        print(f"Title:{self.title} | Author:{self.author} | Copies:{self.copies}")
library=[]
for i in range(3):
    print(f"Enter details of Book {i+1}:")
    title=input(f"Enter the Book title:")
    author=input(f"Enter Author:")
    copies=int(input("Enter Copies:"))

    book=Book(title,author,copies)
    library.append(book)
search_book=input("Enter the Book title to search:")
found=False
for book in library:
    if book.title.lower()==search_book.lower():
        book.display_info()
        found=True
        break
else:
 print("Book not available")

        