usersdata = {
    "1": {
        "username": "Joseph",
        "password": "12345aj"
    },
    "2": {
        "username": "Saleem",
        "password": "23523si"
    },
    "3": {
        "username": "Adanna",
        "password": "90523si"
    },
    "4": {
        "username": "Ajibuah",
        "password": "15678ok"
    }
}
username = input("Enter your username: ")
password = input("Enter your password: ")
if username in [userdata['username'] for userdata in usersdata.values()]:
    for user_id, user_data in usersdata.items():
        if user_data["username"] == username and user_data["password"] == password:
            print("Login successful!! Welcome back, " + user_data["username"])
            break
    else:
        print("Incorrect password. Please try again.")
else:
    print("Username not found. Please check your username.")



