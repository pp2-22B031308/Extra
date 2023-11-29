users = []


def add_user():
    user = {}
    user['Name'] = input("Enter name: ")
    user['Surname'] = input("Enter Surname: ")

    while True:
        try:
            user['Age'] = int(input("Enter age: "))
            break
        except ValueError:
            print("Please enter a valid integer for age.")

    user['Address'] = input("Enter Address: ")
    user['Username'] = input("Enter Username: ")

    while len(user['Password']) < 8:
        user['Password'] = input("Enter Password (minimum 8 characters): ")
        if len(user['Password']) < 8:
            print("Password should contain at least 8 characters.")

    while user['Username'] in [existing_user['Username'] for existing_user in users]:
        print("Username already exists. Enter a unique username.")
        user['Username'] = input("Enter username: ")

    users.append(user)
    print("User added successfully.")


def delete_user():
    username = input("Enter username to delete: ")
    for user in users:
        if user['Username'] == username:
            users.remove(user)
            print(f"User '{username}' removed successfully.")
            return
    print(f"User '{username}' not found.")


def view_users():
    print("\nList of users:")
    for user in users:
        print(user)
    print()


def authenticate_user():
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user['Username'] == username and user['Password'] == password:
            print("Authentication successful!")
            return
    print("Authentication failed.")


while True:
    print("1. Add User")
    print("2. Remove User")
    print("3. View Users")
    print("4. Authenticate User")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_user()
    elif choice == '2':
        delete_user()
    elif choice == '3':
        view_users()
    elif choice == '4':
        authenticate_user()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please enter a valid option.")
