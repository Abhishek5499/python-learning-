
# B2. Create a Book class with title and author. Instantiate 3 books and print all their titles using a loop.

class Book :
      def __init__(self,title,author):

            self.title = title
            self.author = author



book1 = Book("Harry Potter", "J.K. Rowling")
book2 = Book("The Alchemist", "Paulo Coelho")
book3 = Book("Wings of Fire", "A.P.J. Abdul Kalam")


books = [book1,book2,book3]

for book in books:

      print(book.title)

# or

print(book1.title)
print(book2.title)
print(book3.title)
