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
    print("Borrow Books:")
    
    # Get user ID
    userid = input("Please Enter Your User ID: ")
    try:
        userid = int(userid)
    except ValueError:
        print("Invalid User ID")
        return
    
    # Find the user
    user_found = None
    for user in users:
        if user["id"] == userid:
            user_found = user
            break

    if not user_found:
        print("User Not Found")
        return
    
    print(f"User Found with name: {user_found['name']}")
    
    # Get book ID
    bookid = input("Please enter the ID of the book you want to borrow: ")
    try:
        bookid = int(bookid)
    except ValueError:
        print("Invalid Book ID")
        return
    
    # Find the book
    book_found = None
    for book in books:
        if book["id"] == bookid:
            book_found = book
            break

    if not book_found:
        print("Book Not Found")
        return

    # Check if the book is available
    if book_found["status"] == "Available":
        book_found["status"] = "Borrowed"  # Change the book status to "Borrowed"
        user_found["borrowed_books"].append(book_found)  # Add book to user's borrowed_books list
        print(f"Book '{book_found['title']}' borrowed successfully by {user_found['name']}.")
    else:
        print(f"Sorry, '{book_found['title']}' is already borrowed by someone else.")

def return_books():
    print("Return Books:")
    
    # Get user ID
    userid = input("Please Enter Your User ID: ")
    try:
        userid = int(userid)
    except ValueError:
        print("Invalid User ID")
        return
    
    # Find the user
    user_found = None
    for user in users:
        if user["id"] == userid:
            user_found = user
            break

    if not user_found:
        print("User Not Found")
        return
    
    # Check if the user has any borrowed books
    if not user_found["borrowed_books"]:
        print(f"{user_found['name']} has not borrowed any books.")
        return
    
    # Display borrowed books
    print(f"\n{user_found['name']}'s Borrowed Books:")
    for idx, book in enumerate(user_found["borrowed_books"], start=1):
        print(f"{idx}. {book['title']} by {book['author']}")
    
    # Select book to return
    book_to_return_idx = input("Enter the number of the book you want to return: ")
    try:
        book_to_return_idx = int(book_to_return_idx) - 1  # Convert to 0-based index
        if book_to_return_idx < 0 or book_to_return_idx >= len(user_found["borrowed_books"]):
            print("Invalid selection.")
            return
    except ValueError:
        print("Invalid selection.")
        return
    
    # Get the book from the borrowed_books list
    book_to_return = user_found["borrowed_books"][book_to_return_idx]
    
    # Update the book's status to "Available"
    for book in books:
        if book["id"] == book_to_return["id"]:
            book["status"] = "Available"
            break
    
    # Remove the book from user's borrowed_books list
    user_found["borrowed_books"].pop(book_to_return_idx)
    
    print(f"Book '{book_to_return['title']}' returned successfully by {user_found['name']}.")


def view_users():
    print("All Users:")
    for book in users:
        print(f'{book["id"]}- "{book["name"]}"')

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