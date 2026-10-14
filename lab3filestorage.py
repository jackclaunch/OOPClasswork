import pickle

def addtoFile(filename, newContent):
    addFile = open(filename, "ab")
    pickle.dump(newContent, addFile)
    addFile.close()

def loadtoList(filename, listname):
    f = open(filename, "rb")
    while True:
        try:
            newLoad = pickle.load(f)
            listname.append(newLoad)
        except EOFError:
            f.close()
            break

class Book:
    def __init__(self):
        self.id = ""
        self.title = ""
        self.publisher = ""
        self.year_published = ""
        self.authorid = ""
        self.isborrowed = False
        self.user_borrowing = ""

    def create_new_book(self):
        self.id = int(input("Enter book ID: "))
        self.title = input("Enter book title: ")
        self.publisher = input("Enter book publisher: ")
        self.year_published = input("Enter year published: ")

    def display_book(self):
        print("ID:", self.id)
        print("Title:", self.title)
        print("Publisher:", self.publisher)
        print("Year Published:", self.year_published)
        print("Author ID:", self.authorid)
        print("Is Borrowed:", self.isborrowed)
        print("User Borrowed:", self.user_borrowing)

    def assign_author(self, author_id):
        self.authorid = author_id

    def add_user_borrowing(self, user_id):
        self.user_borrowing = user_id
        self.isborrowed = True
    def book_return(self):
        self.isborrowed = False
        self.user_borrowing = ""

class Author:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.affiliation = ""
        self.country = ""
        self.phone = ""
        self.email = ""
        self.books_written = []
    def create_new_author(self):
        self.id = int(input("Enter author ID: "))
        self.name = input("Enter name: ")
        self.affiliation = input("Enter affiliation: ")
        self.country = input("Enter country: ")
        self.phone = input("Enter phone: ")
        self.email = input("Enter email: ")
    def display_author(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Affiliation:", self.affiliation)
        print("Country:", self.country)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Books written:", self.books_written)
    def add_book(self, book_id):
        self.books_written.append(book_id)

class User:
    def __init__(self):
        self.id = ""
        self.name = ""
        self.password = ""
        self.address = ""
        self.email = ""
        self.books_borrowed = []
    def create_new_user(self):
        self.id = int(input("Enter user ID: "))
        self.name = input("Enter name: ")
        self.password = input("Enter password: ")
        self.address = input("Enter address: ")
        self.email = input("Enter email: ")
    def display_user(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Address:", self.address)
        print("Email:", self.email)
        print("Books borrowed:", self.books_borrowed)

    def add_books_borrowed(self, book_id):
        self.books_borrowed.append(book_id)
    def remove_books_borrowed(self, book_id):
        self.books_borrowed.remove(book_id)


booksList = []
authorsList = []
userList = []


loadtoList("books.dat", booksList)
loadtoList("authors.dat", authorsList)
loadtoList("users.dat", userList)


while True:
    userInput = input("1. Add content\n2. Assign author\n3. Borrow a book\n"
                      "4. Return a book\n5. Print content\n")
    if userInput == "1":
        userAddInput = input("1. New book\n2. New author\n3. New user\n")
        if userAddInput == "1":
            newBook = Book()
            newBook.create_new_book()
            booksList.append(newBook)
            addtoFile("books.dat", newBook)
        elif userAddInput == "2":
            newAuthor = Author()
            newAuthor.create_new_author()
            authorsList.append(newAuthor)
            addtoFile("authors.dat", newAuthor)
        elif userAddInput == "3":
            newUser = User()
            newUser.create_new_user()
            userList.append(newUser)
            addtoFile("users.dat", newUser)


    if userInput == "2":
        bookID = int(input("Enter book ID: "))
        authorID = int(input("Enter author ID: "))
        for i in range(len(booksList)):
            try:
                book = booksList[i]
                if book.id == bookID:
                    for j in range(len(authorsList)):
                        try:
                            author = authorsList[j]
                            if author.id == authorID:
                                book.assign_author(authorID)
                                author.add_book(bookID)
                        except IndexError:
                            print("Invalid author ID")
            except IndexError:
                print("Invalid book ID")

    elif userInput == "3":
        bookID = int(input("Enter book ID: "))
        userID = int(input("Enter user ID: "))
        for i in range(len(booksList)):
            try:
                book = booksList[i]
                if book.id == bookID:
                    for j in range(len(userList)):
                        try:
                            user = userList[j]
                            if user.id == userID:
                                user.add_books_borrowed(bookID)
                                book.add_user_borrowing(userID)
                        except IndexError:
                            print("Invalid user ID")
            except IndexError:
                print("Invalid book ID")
    elif userInput == "4":
        bookID = int(input("Enter returning book ID: "))
        userID = int(input("Enter user ID: "))
        for i in range(len(booksList)):
            try:
                book = booksList[i]
                if book.id == bookID:
                    for j in range(len(userList)):
                        try:
                            user = userList[j]
                            if user.id == userID:
                                book.book_return()
                                user.remove_books_borrowed(bookID)
                        except IndexError:
                            print("Invalid user ID")
            except IndexError:
                print("Invalid book ID")

    elif userInput == "5":
        userPrintInput = input("1. Print books\n2. Print authors\n3. Print users\n")
        if userPrintInput == "1":
            for i in range(len(booksList)):
                book = booksList[i]
                book.display_book()
        elif userPrintInput == "2":
            for i in range(len(authorsList)):
                author = authorsList[i]
                author.display_author()
        elif userPrintInput == "3":
            for i in range(len(userList)):
                user = userList[i]
                user.display_user()

    file1 = open("books.dat", "wb")
    for i in booksList:
        pickle.dump(i, file1)
    file1.close()
    file2 = open("authors.dat", "wb")
    for i in authorsList:
        pickle.dump(i, file2)
    file2.close()
    file3 = open("users.dat", "wb")
    for i in userList:
        pickle.dump(i, file3)
    file3.close()
