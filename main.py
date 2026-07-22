
import json
import os
books = []

def add_book():
    title = input("Enter book title: ")
    author = input("Enter the name of the author: ")
    book = {"title": title, "author": author, "read": False}
    books.append(book)
    print("Book added successfully!")
    save_books()

def view_books():
    for book in books:
        print("Title:", book["title"])
        print("Author:", book["author"])
        print("Read:", book["read"])

def mark_as_read():
    title_to_mark = input("Enter the title of the book you finished: ")
    for book in books:
        if book["title"] == title_to_mark:
            book["read"] = True
            print("Marked as read!")
            save_books()

def save_books():
    with open("books.json", "w") as file:
        json.dump(books,file)

def load_books():
    if os.path.exists("books.json"):
        with open("books.json", "r") as file:
            global books
            books = json.load(file)

load_books()

while True:
    print("\nWhat would you like to do?")
    print("1. Add a book")
    print("2. View all books")
    print("3. Mark a book as read")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        mark_as_read()
    elif choice == "4":
        print("Goodbye!")
        break
