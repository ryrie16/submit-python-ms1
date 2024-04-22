bookshelf = []

def add_book(title, read_status):
    global bookshelf
    book_id = len(bookshelf) + 1
    book = {'id': book_id, 'title': title, 'read_status': int(read_status)}
    bookshelf.append(book)
    print(f"You have added '{title}' to the bookshelf successfully")

def edit_book(book_id, new_title, new_read_status):
    global bookshelf
    for book in bookshelf:
        if book['id'] == book_id:
            book['title'] = new_title
            book['read_status'] = new_read_status
            print(f"The book '{new_title}' has been edited successfully")
            return
    print("The book has not been found")


def search_books(search_term):
    found_books = []
    for book in bookshelf:
        if search_term.lower() in book['title'].lower():
            found_books.append(book)
    if found_books:
        print("Books have been found:")
        for book in found_books:
            print(f"ID: {book['id']}, title: {book['title']}, read status: {book['read_status']}")
    else:
        print("No book has been found")

def delete_book(book_id_title):
    global bookshelf
    for i, book in enumerate(bookshelf):
        if book_id_title.isdight():
            if book['id'] == book_id_title:
                del bookshelf[i]
                print(f"The id {book_id_title} of book has been deleted successfully")
                return    
        else:  
            if book['title'] == book_id_title:
                del bookshelf[i]
                print(f"The book {book_id_title} has been deleted successfully")
                return
    print("No book has been found")

def display_statistics():
    total_books = len(bookshelf)
    read_books = sum(1 for book in bookshelf if book['read_status'])
    unread_books = total_books - read_books
    print(f"total books: {total_books}, read books: {read_books}, unread books: {unread_books}")

def main():
    print('==================================================\n')
    print('Welcome to your personal books digital library!\n')
    print('==================================================\n')
    print('1: Add a Book\n')
    print('2: Edit a Book\n')
    print('3: Search for Books\n')
    print('4: Delete a Book\n')
    print('5: View Library Stats\n')
    print('6: Exit app\n')
    while True:
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter the title of the book: ")
            read_status = input("Is the book read? (1 for read/ 0 for unread): ")
            if int(read_status) in (0, 1):
                add_book(title, read_status)
            else:
                print("Please enter the read status correctly")
            

        elif choice == '2':
            book_id = int(input("Enter the ID or the title of the book you want to edit: "))
            new_title = input("Enter the new title of the book: ")
            new_read_status = input("Is the book read? (1 for read/ 0 for unread): ")
            edit_book(book_id, new_title, new_read_status)
        elif choice == '3':
            search_term = input("Enter the search term: ")
            search_books(search_term)
        elif choice == '4':
            book_id_title = input("Enter the ID or the title of the book you want to delete: ")
            delete_book(book_id_title)
        elif choice == '5':
            display_statistics()
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == '__main__':
    main()

            