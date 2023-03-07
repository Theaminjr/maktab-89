import random
class User():
    users_list = {}
    @classmethod
    def register(self,username,phone_number,password):
         user = {}
         user["username"] =self.checkusername(username)
         user["phone_number"] =phone_number
         user["password"] = self.checkpass(password)
         user["user_id"] = self.checkid()
         self.users_list[username] = user
   
    @classmethod
    def checkid(self):
        _id = random.randint(10000000,99999999)
        for user in self.users_list:
              details = self.users_list[user]
              if details["user_id"] == _id:
                self.checkid()
        return _id

         
    @classmethod
    def checkpass(self,password):
        if len(password)>= 4:
            return password
        else: 
            raise Exception("passweord length should be more than 3")

    @classmethod
    def checkusername(self,username):
        if  username in self.users_list:
                raise Exception("username is already taken")
        return username
    
    @classmethod
    def login(self,username,password):
        
            if  username in self.users_list.keys():
                if self.users_list[username]["password"] == password:
                    print("you are logged in as",username)
                    return username
                else:
                    print("wrong password")
                    return False
            else:
                print("username could not be found")
                return False
    @classmethod
    def editprofile(self,login):
        username,phonenumber = input("username - phonenumber   ").split()
        self.users_list[login]["username"] = username
        self.users_list[login]["phone_number"] = phonenumber
    @classmethod
    def editpass(self,login):
        oldpass , newpass ,rnewpass = input("oldpass - newpass - repeat newpass  ").split()
        if (newpass == rnewpass) and self.login(login,oldpass):
           self.users_list[login]["password"] = self.checkpass(newpass)
           print("pass changed")
       
    @classmethod
    def showprofile(self,login):
        print(f'{self.users_list[login]["username"] } and {self.users_list[login]["phone_number"] }')
