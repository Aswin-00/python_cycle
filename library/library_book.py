'''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Create a Python class called `Library` to manage a library's book collection with 
      the following attributes and methods:
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Attributes: `books` (a list of book titles).
- Methods:
  - `__init__(self)` - Initialize an empty list to store books.
  - `add_book(self, book_title)` - Use a list to add a book to the collection.
  - `remove_book(self, book_title)` - Use list methods to remove a book from the collection.
  - `list_books(self)` - Return the list of all books in the collection.

'''



class Library:

# intilize a empty list
    def __init__(self):        
        self.book_list=[]


#add book to list
    def add_book(self,book_title):
        if book_title in self.book_list:
            print("iteam already present in list")
        else:
            self.book_list.append(book_title)

#remove a list iteam
    def remove_book(self,book_title):
        if book_title not in self.book_list:
            print("iteam not in list")
        else:
            self.book_list.remove(book_title)
# list all the books
    def list_books(self):
        return(self.book_list)

# return a list 
    def __str__(self):
        return(f'{self.book_list}')



    
