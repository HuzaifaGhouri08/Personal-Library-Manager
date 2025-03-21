import json  # To work with JSON data
import os  # To handle files

data_file = 'library.txt'  # Where we keep the book info

def load_library():
    """Get the book list from the file, or make a new one."""
    if os.path.exists(data_file):
        try:
            with open(data_file, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error: Library file is corrupted or empty. Creating a new library.")
            return []
    return []

def save_library(library):
    """Put the book list back into the file."""
    with open(data_file, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library):
    """Ask for book details, then add it."""
    title = input('Enter the title of the book: ')
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book? (yes/no): ').lower() == 'yes'

    new_book = {'title': title, 'author': author, 'year': year, 'genre': genre, 'read': read}
    library.append(new_book)
    save_library(library)
    print(f'Book "{title}" added successfully.')

def remove_book(library):
    """Find a book by title and remove it."""
    title = input("Enter the title of the book to remove from the library: ")
    initial_length = len(library)
    library[:] = [book for book in library if book['title'].lower() != title.lower()]
    if len(library) < initial_length:
        save_library(library)
        print(f'Book "{title}" removed successfully.')
    else:
        print(f'Book "{title}" not found in the library.')

def search_library(library):
    """Find books by title or author."""
    search_by = input("Search by title or author: ").lower()
    search_term = input(f"Enter the {search_by}: ").lower()

    results = []
    for book in library:
        if search_by in book and search_term in str(book[search_by]).lower():
            results.append(book)

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No books found matching '{search_term}' in the {search_by} field.")

def display_all_books(library):
    """Show all the books in the list."""
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

def display_statistics(library):
    """Give some stats about the books."""
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_read = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total books: {total_books}")
    print(f"Books read: {read_books}")
    print(f"Percentage read: {percentage_read:.2f}%")

def main():
    """Main part of the program."""
    library = load_library()
    while True:
        print("\nWelcome to Your Personal Library Manager!\n\nMenu:")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Find a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_library(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
