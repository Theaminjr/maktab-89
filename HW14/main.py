from fastapi import FastAPI,HTTPException
from starlette.requests import Request
from starlette.responses import Response
from pydantic import BaseModel,Field,validator,ValidationError
from typing import Dict,List
from datetime import datetime


app = FastAPI()

fake_database = {"fundementals of electronics" : "an electronic book written by behzan razavi",
                  "grokking algorithms":"an algorithm book written by jush",
                  "clean code":"this book will teach you how to write better code",
                  "django fundementals":"learn to code in django framework and build web apps"}
usernames = ["amin","ramin"]
emails = ["amin@gmail.com","ramin@gmail.com"]
fake_database2 = {"book1":"3000","book2":"6500"}

class User(BaseModel):
    username:str 
    email:str 
    password:str = Field(regex="^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    date_joined = datetime.now()
   
    @validator('username')
    def username_must_be_unique(cls,name):
        if name in usernames:
            raise ValueError("username is already chosen")
        return name

    @validator('email')
    def email_must_be_unique(cls,e):
        if e in emails:
            raise ValueError("email is already registered")
        return e


class Cart(BaseModel):
    items : dict = {"book1":"3000","book2":"6500"} #item as key and price as value

class IntList(BaseModel):
    nums : List[int]


#Question 1
@app.get("/searh")
def search(query:str):
    found= []
    for k,v in fake_database.items():
        if query in k or query in v:
            found.append(f"item:{k} desc:{v}")
    return found


#Question 3
@app.post("/register")
def register(user:User):

    usernames.append(user.username)
    emails.append(user.email)
    return "success"

#Question 7
@app.post("/sum")
def sum(intlist:IntList):
    print("hi")
    total = 0
    print(intlist)
    
    for i in intlist.nums:
        total += i
    return total

#Question 6
@app.post("/cart")
def get_total_value(cart:Cart):
    total = 0
    for item,price in cart.items.items():
        total += int(price)
    return f"total price ={total}"

#Question 2
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception:
        return Response("Internal server error", status_code=500)

app.middleware('http')(catch_exceptions_middleware)