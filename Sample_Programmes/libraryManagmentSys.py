# All books are stored here

books = [
    {"id": 1, "author": "J.K. Rowling", "title": "Harry Potter and the Sorcerer's Stone", "genre": "Fantasy", "status": "Available"},
    {"id": 2, "author": "George Orwell", "title": "1984", "genre": "Dystopian", "status": "Available"},
    {"id": 3, "author": "J.R.R. Tolkien", "title": "The Hobbit", "genre": "Fantasy", "status": "Available"},
    {"id": 4, "author": "F. Scott Fitzgerald", "title": "The Great Gatsby", "genre": "Classic", "status": "Available"},
    {"id": 5, "author": "Harper Lee", "title": "To Kill a Mockingbird", "genre": "Classic", "status": "Available"}
]

# All users are stored here

users = [
    {"id": 1, "name": "Alice Johnson", "borrowed_books": []},
    {"id": 2, "name": "Bob Smith", "borrowed_books": []},
    {"id": 3, "name": "Charlie Brown", "borrowed_books": []}
]

# Take input from user for choice in main menu
def user_choice():
    while True:    
        choice = input("\nEnter your choice (1-6): ")
        try:
            choice = int(choice.strip())
            if choice in range(7):
                choice = str(choice)
                return choice
            else:
                print("Please enter a Valid Input i.e from 1 to 6\n")
        except:
            print("Please enter a Valid Input i.e form 1 to 6\n")

# all functions are below
def view_books():
    print("All Books:")
    for book in books:
        print(f'{book["id"]}- "{book["title"]}" by {book["author"]} ( {book["status"]} )')
def search_books():
    print("Search Books:")
    search_by = input("Search by (title/author/genre): ").strip().lower()
    query = input(f"Enter {search_by}: ").strip().lower()
    
    found_books = [book for book in books if query in book[search_by].lower()]
    
    if found_books:
        for book in found_books:
            print(f"{book['id']}. \"{book['title']}\" by {book['author']} ({book['status']})")
    else:
        print("\nNo books found.")
def borrow_books():
    pass
def return_books():
    pass
def view_users():
    pass

            # main loop starts here
print("Welcome to the Community Library System!\n----------------------------------------\n")
while True:
    print("1. View all books\n2. Search for a book\n3. Borrow a book\n4. Return a book\n5. View all users\n6. Exit")
    choice = user_choice()
    print()
    if choice == "6":
        print("\nExiting the System --- GoodBye")
        break

    options = {
        "1" : view_books,
        "2" : search_books,
        "3" : borrow_books,
        "4" : return_books,
        "5" : view_users,
    }
    options[choice]()
    print("----------------------------\n")