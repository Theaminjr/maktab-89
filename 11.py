import re


class User:
    database = {}

    def __init__(self, first_name, last_name, phone, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.password = password
        self.email = email
        User.database[self.username] = self

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone_number):
        pattern = r'^\+98'
        if re.search(pattern, phone_number):
            self._phone = phone_number
        else:
            raise ValueError('phone number start with +98')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password):
        pattern = r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)[A-z\d]{8,}'
        if re.search(pattern, new_password):
            self._password = new_password
        else:
            raise ValueError('password must contains A-Z a-z 0-9 and minimum 8')

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        pattern = r'^[A-z]+\w+\@[a-z]{2,5}\.[a-z]{2,3}'
        if re.search(pattern, new_email):
            self._email = new_email
        else:
            raise ValueError('hint: myemail@abcd.com')

    @classmethod
    def register(cls, first_name, last_name, phone, email, username, password):
        return cls(first_name, last_name, phone, email, username, password)

    @staticmethod
    def login(username, password):
        if username in User.database:
            if User.database[username].password == password:
                print("you are login")
            else:
                print('username or password incorrect')

