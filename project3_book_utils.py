# book_utils.py

def calculate_total_pages(books):
    total = 0
    for book in books:
        total += book["pages"]
    return total

def print_books(books):
    for book in books:
        print(f"{book['title']} by {book['author']} - {book['pages']} pages")

def search_books(books, keyword):
    return [b for b in books if keyword.lower() in b["title"].lower()]

# -------- ERROR ON LINE 19 ----------
if __name__ == "__main__":
    books = [
        {"title": "Python 101", "author": "John Smith", "pages": "300"},  # ❌ pages as str
        {"title": "Flask in Action", "author": "Jane Doe", "pages": 250}
    ]
    print_books(books)
    total_pages = calculate_total_pages(books)  # This will cause an error
    print(f"Total Pages: {total_pages}")

#----- How to fix it ------
# 
# In the first book dictionary, "pages": "300" should be an integer: "pages": 300
#  
# Reason: Adding string + integer causes a TypeError.
#
#