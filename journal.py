users = []

def add_user():
    user = {}
    user ['Name'] = input("Enter name:")
    user['Surname'] = input("Enter Surname:")
    user['Age'] = input("Enter age:")
    user['Adress'] = input("Enter Adress:")
    user['Username'] = input("Enter Username:")
    user['Password'] = input("Enter Password:")


    while len(user['Password']) < 8:
        print("Password should contain at leas 8 symbols")
        user['Password'] = input("Enter PAssword:")

    emails = [existing_user ['Username'] for existing_user in users]
    while user['Username'] in emails:
        print("Email already exists. Enter a unique email.")
        user['Username'] = input("Enter username: ")


    def delete_user():
        username = input("Enter username to delete:")
        for user in users:
            if user['Username'] == username:
                users.remove(user)
                print(f"User'{username}' removed sucesfully")
                break
            else:
                print(f"User '{username}' not found.")

    def view_users():
        print("\n list of users:")
        for user in users:
            print (user)
        print()

        while True:
            print("1. Add User")
            print("2. Remove User")
            print("3. View Users")
            print("4. Exit")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_user()
            elif choice == 2:
                delete_user()
            elif choice == 3:
                view_users()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please enter a valid option.")