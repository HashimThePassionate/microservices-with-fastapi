from bcrypt import hashpw, gensalt, checkpw
from fastapi import FastAPI
from uuid import UUID, uuid1
from typing import Optional, List, Dict
from datetime import date, datetime
from enum import Enum
from pydantic import BaseModel


app = FastAPI()
pending_users = dict()
valid_profiles = dict()
valid_users = dict()
discussion_posts = dict()

class User(BaseModel):
    username: str
    password: str


class User(BaseModel):
    username: str
    password: str


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
            return {"message": "Invalid User"}

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
            return {"message": "User Does Not Exist"}
        
@app.patch("/account/profile/update/names/{username}")
def update_profile_names(username: str, id: UUID, new_names: Dict[str, str]):
    if valid_users.get(username) == None:
        return {"message": "User Does Not Exist"}
    elif new_names == None:
        return {"message": "new names are required"}
    else:
        user = valid_users.get(username)
        if user.id == id:
            profile = valid_profiles[username]
            profile.firstname = new_names['fname']
            profile.lastname = new_names['lname']
            profile.middle_initial = new_names['mi']
            valid_profiles[username] = profile
            return {"message": "Profile Names Successfully Updated", "profile": profile}
        else:
            return {"message": "User Does Not Exist"}
        


@app.delete("/discussion/posts/remove/{username}")
def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "User Does Not Exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "Post Does Not Exist"}
    else:
        del discussion_posts[id]
        return {"message": "Post Successfully Deleted"}