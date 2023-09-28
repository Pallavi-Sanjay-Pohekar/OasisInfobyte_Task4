
user_credentials = {}

def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
    if username in user_credentials:
        print("Username already exists. Please choose a different one.")
    else:
        user_credentials[username] = password
        print("Registration successful. You can now log in.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
   
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful. Welcome, " + username + "!")
      
    else:
        print("Login failed. Please check your username and password.")

while True:
    print("\nMenu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
