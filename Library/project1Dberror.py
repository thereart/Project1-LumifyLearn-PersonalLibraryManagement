import json
import os

DB_FILE = "library_db.json"

class LibraryDatabase:
    def __init__(self):
        if not os.path.exists(DB_FILE):
            self._initialize_database()
        else:
            self._load_database()

    def _initialize_database(self):
        self.data = {
            "books": [],
            "users": [],
            "borrowed_books": []
        }
        self._save_database()

    def _load_database(self):
        with open(DB_FILE, "r") as file:
            self.data = json.load(file)

    def _save_database(self):
        with open(DB_FILE, "w") as file:
            json.dump(self.data, file, indent=4)

    def add_book(self, book_id, title, author, year):
        new_book = {
            "book_id": book_id,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        }
        self.data["books"].append(new_book)
        self._save_database()

    def add_user(self, user_id, name):
        new_user = {
            "user_id": user_id,
            "name": name
        }
        self.data["users"].append(new_user)
        self._save_database()

    def borrow_book(self, book_id, user_id):
        for book in self.data["books"]:
            if book["book_id"] == book_id and book["available"]:
                book["available"] = False
                self.data["borrowed_books"].append({
                    "book_id": book_id,
                    "user_id": user_id
                })
                self._save_database()
                return True
        return False

    def return_book(self, book_id, user_id):
        for book in self.data["books"]:
            if book["book_id"] == book_id:
                book["available"] = True

        self.data["borrowed_books"] = [
            record for record in self.data["borrowed_books"]
            if not (record["book_id"] == book_id and record["user_id"] == user_id)
        ]
        self._save_database()

    def list_books(self):
        return self.data["books"]

    def list_users(self):
        return self.data["users"]

    def list_borrowed_books(self):
        return self.data["borrowed_books"]

    def find_book_by_title(self, title):
        return [book for book in self.data["books"] if title.lower() in book["title"].lower()]

    def delete_book(self, book_id):
        self.data["books"] = [book for book in self.data["books"] if book["book_id"] != book_id]
        self._save_database()

    def delete_user(self, user_id):
        self.data["users"] = [user for user in self.data["users"] if user["user_id"] != user_id]
        self._save_database()

    def update_book_title(self, book_id, new_title):
        for book in self.data["books"]:
            if book["book_id"] == book_id:
                book["title"] = new_title
                break
        self._save_database()

    def update_user_name(self, user_id, new_name):
        for user in self.data["users"]:
            if user["user_id"] == user_id:
                user["name"] = new_name
                break
        self._save_database()

    def book_exists(self, book_id):
        return any(book["book_id"] == book_id for book in self.data["books"])

    def user_exists(self, user_id):
        return any(user["user_id"] == user_id for user in self.data["users"])

    def generate_summary(self):
        total_books = len(self.data["books"])
        total_users = len(self.data["users"])
        borrowed_books = len(self.data["borrowed_books"])

        print("Library Summary:")
        print(f"Total Books: {total_books}")
        print(f"Total Users: {total_users}")
        print(f"Books Currently Borrowed: {borrowed_books}")

# ---------------- ERROR HERE ON LINE 125  and how to fix ----------------
def buggy_function():
    a = 6
    b = 1
    result = a / b  # ERROR: Division by zero -- Fix it by changing value of b
    print(result)
# -------------------------------------------------------

if __name__ == "__main__":
    db = LibraryDatabase()
    db.add_user("U001", "Alice")
    db.add_book("B001", "Python Basics", "John Smith", 2022)
    db.borrow_book("B001", "U001")
    db.generate_summary()
    buggy_function()
