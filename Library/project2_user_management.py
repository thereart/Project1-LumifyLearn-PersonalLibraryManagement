# user_management.py

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user_id, name, email):
        user = {
            "user_id": user_id,
            "name": name,
            "email": email
        }
        self.users.append(user)

    def get_user(self, user_id):
        for user in self.users:
            if user["user_id"] == user_id:
                return user
        return None

    def delete_user(self, user_id):
        self.users = [u for u in self.users if u["user_id"] != user_id]

    def list_users(self):
        for user in self.users:
            print(f"ID: {user['user_id']}, Name: {user['name']}, Email: {user['email']}")

    def update_user_email(self, user_id, new_email):
        for user in self.users:
            if user["user_id"] == user_id:
                user["email"] = new_email
                break

# -------------- ERROR ON LINE 37 --------------
if __name__ == "__main__":
    um = UserManager()
    um.users = []  # ❌ ERROR: users is redefined as dict (should be a list)
    um.add_user("U002", "Bob", "bob@example.com")  # This will raise an error
    um.list_users()



#------- HOw to Fix the Error-------

# Change um.users = {} to um.users = []
# Reason: A dictionary has no .append() method, which is used in add_user.
#
#
