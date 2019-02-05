class User(object):
    def __init__(self, name, email):
        
        self.name = name
        self.email = email
        self.books = {}

   
    def get_email(self):
        return self.email

    
    def change_email(self, address):
        self.new_email = address
        print("Changed user email address to {new_email_placeholder}.".format(new_email_placeholder=self.new_email))

    
    def __repr__(self):
        user_books_total_read = len(self.books)
        meaningful = "\nUser: {name}\nEmail: {email}\nBooks read: {books}\n".format(name=self.name, email=self.email, books=user_books_total_read)
        return meaningful

    
    def __eq__(self, other_user):
        return self.email == other_user.get_email() and self.name == other_user.get_name()

  
    def read_book(self, book, rating=None):
        if rating is not None:
            book.add_rating(rating)
        self.books[book] = rating

   
    def get_average_rating(self):
        ratings = [val for val in self.books.values() if not val is None]
        total_ratings = 0
        for value in ratings:
            total_ratings += value
        if total_ratings == 0:
            return 0
        return total_ratings / len(ratings)




class Book(object):
    def __init__(self, title, isbn):
        # Set instance variables, ratings is an empty dictionary
        self.title = title
        self.isbn = isbn
        self.ratings = []

  
    def get_title(self):
        return self.title

   
    def get_isbn(self):
        return self.isbn

   
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN has been updated to {isbn_placeholder}.".format(isbn_placeholder=self.isbn))

    def add_rating(self, rating):
        # only add rat ff least 0 and  most 4. Otherwise print 'Invalid Rating'
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
    
    def __eq__(self, other_book):
        return self.title == other_book.get_title() and self.isbn == other_book.get_isbn()

    def get_average_rating(self):
        average_book_rating = 0
        for rating in self.ratings:
            average_book_rating += rating
        if average_book_rating > 0:
            return average_book_rating / len(self.ratings)
        return 0
    
    
    def __hash__(self):
        return hash((self.title, self.isbn))




class Fiction(Book):
    def __init__(self, title, author, isbn):
        super(Fiction, self).__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return_string = "{title} by {author}".format(title=self.title, author=self.author)
        return return_string




class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super(Non_Fiction, self).__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return_string = "{title}, a {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
        return return_string




class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    # Method to create a novel
    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if not rating is None:
                book.add_rating(rating)
            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            print("No user with {email}!".format(email=email))

    def add_user(self, name, email, books=None):
        new_user = User(name, email)
        self.users[email] = new_user
        if books is not None:
            for book in books:
                self.add_book_to_user(book, email)


    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        most_read_title = None
        max_value = 0
        for key, value in self.books.items():
            if value > max_value:
                max_value = value
                most_read_title = key
        return most_read_title.get_title()


    def highest_rated_book(self):
        max_key = 0
        highest_rated_book = None
        for key, value in self.books.items():
            if key.get_average_rating() > max_key:
                max_key = key.get_average_rating()
                highest_rated_book = key
        return highest_rated_book.get_title()

    def most_positive_user(self):
        max_rating = 0
        highest_rating_user = None
        for value in self.users.values():
            if value.get_average_rating() > max_rating:
                max_rating = value.get_average_rating()
                highest_rating_user = value
        return highest_rating_user.name
