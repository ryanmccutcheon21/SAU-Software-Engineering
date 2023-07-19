class UserAuthentication:
    def __init__(self):
        self.users = {
            "admin": "password123",
            "john": "secret",
            "jane": "pass123"
        }

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            return True
        else:
            return False

# Sample usage of the UserAuthentication class
auth = UserAuthentication()
username = input("Enter your username: ")
password = input("Enter your password: ")

if auth.login(username, password):
    print("Login successful.")
else:
    print("Invalid username or password.")
