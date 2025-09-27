from fastapi import FastAPI
from pydantic import BaseModel
from bcrypt import hashpw, gensalt, checkpw

app = FastAPI()
valid_users = dict()


@app.get("/index")
def index():
    return {"message": "Welcome Aspiring FastAPI!"}


@app.get("/login")
def login(username: str, password: str):
    if valid_users.get(username) == None:
        return {"message": "User Does Not Exist"}
    else:
        user = valid_users.get(username)
        if checkpw(password.encode(), user.passphrase.encode()):
            return user
        else:
            {"message": "Invalid User"}

class User(BaseModel):
    username: str
    password: str

pending_users = dict()

@app.post("/login/signup")
def signup(uname: str, passwd: str):
    if (uname == None and passwd == None):
        return {"message": "Invalid User"}
    elif not valid_users.get(uname) == None:
        return {"message": "User Already Exists"}
    else:
        user = User(username=uname, password=passwd)
        pending_users[uname] = user
        return user