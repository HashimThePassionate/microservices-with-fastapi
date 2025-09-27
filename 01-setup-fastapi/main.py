from fastapi import FastAPI
from pydantic import BaseModel
from bcrypt import hashpw, gensalt, checkpw
from uuid import UUID, uuid1
from typing import Optional, List, Dict
from datetime import date, datetime
from enum import Enum

app = FastAPI()
valid_users = dict()
valid_profiles = dict()

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


class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"

class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType


@app.put("/account/profile/update/{username}")
def update_profile(username: str, id: UUID, new_profile: UserProfile):
    if valid_users.get(username) == None:
        return {"message": "User Does Not Exist"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            valid_profiles[username] = new_profile
            return {"message": "Profile Successfully Updated", "profile": new_profile}
        else:
            {"message": "User Does Not Exist"}