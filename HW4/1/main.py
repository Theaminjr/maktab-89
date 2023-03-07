from logic import User

login = "not logged in"
while True:
    request = input("1-sign up 2-login ==> ")
    if request == "1":
        username,phone_number,password = input("username  phone_number  password ==>").split()
        try:
            User.register(username,phone_number,password)
        except Exception as error:
            print(error)
        print(User.users_list)
    elif request == "2":
        username,password = input("enter username and password with space ==> ").split()
        login = User.login(username,password)
        if login != "not logged in":
            while True:
                request = input("1-check profile 2-edit profile 3-change password 4-logout  ")
                if request == "4":
                    login = "not logged in"
                    break
                if request == "1":
                    User.showprofile(login)
                if request == "2":
                    User.editprofile(login)
                if request == "3":
                    User.editpass(login)
