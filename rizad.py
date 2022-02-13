# pylogin | @riz4d
# github : https://github.com/riz4d/pylogin
# -------------------------------------------------
import time
users = {
    "root@rizad": {
        "password": "#admin",
        "group": "admin",
        "mail": []
    }
}
def validate(form):
    if len(form) > 0:
        return False
    return True

def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Enter your Username")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Enter your Password")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Enter a Username")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Enter a Password")
            continue
        else:
            break
    print("Creating  your account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

# session interface
def session(username):
    print("Welcome to your account " + username)


# Home Page
print("Welcome to the Network(@riz4d). Please register or login.")
print("Options:\n 1 : register\n 2 : login\n 3 : exit")
while True:
    option = input("> ")
    if option == "2":
        login()
    elif option == "1":
        register()
    elif option == "3":
        break
    else:
        print(option + " is not an option")

print("Shutting down...")
time.sleep(1)
