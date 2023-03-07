username = input("username: ")
password = input("password: ")
if username and password == "admin":
    print("welcome on admin")
elif username == "admin" and password != "admin":
    print("wrong")
else: print("welcome",username)