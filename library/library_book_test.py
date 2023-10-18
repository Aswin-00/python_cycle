'''

Create a Python program that does the following:


1. Import the `Library` class from a separate module.
2. Create an instance of the `Library` class.
3. Add several books to the library's collection using the `add_book` method.
4. Remove a book from the collection using the `remove_book` method.
5. List all the books in the library's collection using the `list_books` method.
6. Display the results.

Hint : Use  a list to store the book titles

Sample Output

Books in the Library:
['The Great Gatsby', 'To Kill a Mockingbird', '1984']

Books after removal:
['The Great Gatsby', '1984']

'''

# importing the class Livrary from library_book 

from library_book import Library as Lib

def main():
# create a intance
    sample=Lib()
    sample.add_book('The Great Gatsby')
    sample.add_book('To Kill a Mockingbird')
    sample.add_book('1984')
    
    print('Books in the Library:')
    print(sample.list_books(),'\n')
    sample.remove_book('To Kill a Mockingbird')
    print('Books after removal:')
    print(sample.list_books())

if __name__=="__main__":
    main()
