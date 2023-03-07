from models import Product, User,Comment
import datetime


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_product(self, product, amount=1):
        self.products[product] = self.products.get(product, 0) + amount

    def remove_product(self, product, amount=1):
           if amount <= self.products[product]:
               self.products[product] -= amount
               if self.products[product] == 0 :
                  del self.products[product]
           else:
               raise Exception("Not Enough Products")


    def add_user(self, username):
        usernames = [user.username for user in self.users]
        if username in usernames:
           return None  
        else :
            self.users.append(User(username))
            return username

    def get_total_asset(self):
        total_asset = 0
        for k,v in self.products.items():
            total_asset += k.price * v
        return total_asset

    def get_total_profit(self):
        profit = 0
        for user in self.users:
           for product in user.bought_products:
               profit += product.price
        return profit


    def get_comments_by_user(self, user):
        comments = []
        for product in self.products:
            for comment in product.comments:
                if comment.user == user:
                    comments.append(comment.text)
        return comments

    def get_inflation_affected_product_names(self):
        inflation = {}
        for product in self.products.keys():
            if product.name in inflation.keys():
                inflation[product.name].append(product.price)
            else :
                inflation[product.name] = [product.price]
        return {k:v for k,v in inflation.items() if len(v) > 1}



    def clean_old_comments(self, date):
        #revised
        for product in self.products:
            copied = product.comments.copy()
            for comment in copied:
                    if comment.date_added < date:
                        product.comments.remove(comment)



    def get_comments_by_bought_users(self, product):
        comments = product.comments
        comments_verified = []
        for comment in comments:
            if product in comment.user.bought_products :
                comments_verified.append(comment.text)
        return comments_verified
                

#create a store
digikala = Store()

#create some products
dampaei_abri = Product("dampaei x4",12000,"shoe")
kafsh_melli = Product("Melli",12000,"shoe")
Hp_pavilion = Product("hp pavilion",30000,"tech")
mac = Product("mac",35000,"tech")

#add products to store
digikala.add_product(dampaei_abri,6)
digikala.add_product(kafsh_melli,3)
digikala.add_product(Hp_pavilion,4)
digikala.add_product(mac,1)
print("products = ",digikala.products)



#remove one mac
digikala.remove_product(mac)
print("products = ",digikala.products)


# #create users
# digikala.add_user("amin")
# digikala.add_user("mohsen")
# digikala.add_user("amin") #should not be added
# print("users = ",digikala.users)

# #calculate asset
# assets = digikala.get_total_asset()
# print("assests = " ,assets)

# #calculate profits
# digikala.users[0].bought_products.append(dampaei_abri) #first add some bought items
# digikala.users[0].bought_products.append(Hp_pavilion)  #first add some bought items
# profit = digikala.get_total_profit()
# print("profits = " ,profit)

# #create comments
# c1 = Comment("awli",digikala.users[0])
# c2 = Comment("Ashghal" , digikala.users[1])
# c3 = Comment("linux roosh nasb nemishe." ,digikala.users[0])
# c4 = Comment("man sefid sefaresh dadam na ghermez!!" ,digikala.users[1])

# #add comments to products
# Hp_pavilion.comments.append(c3)
# Hp_pavilion.comments.append(c2)
# kafsh_melli.comments.append(c1)
# kafsh_melli.comments.append(c4)


# #calculate inflation
# kafsh_melli_new = Product("Melli",18000,"shoe") #add already existing product with diffrent price
# digikala.add_product(kafsh_melli_new)
# inflation = digikala.get_inflation_affected_product_names()
# print("inflation = ",inflation)

# #print comments for HP_pavilion from bought users
# print("comments of the users that have bought the product = ",digikala.get_comments_by_bought_users(Hp_pavilion))