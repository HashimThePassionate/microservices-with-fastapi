# 🚀 **FastAPI – Building Blocks for Microservices**

## 📌 Importance of Business Requirements

In any **software development** work, it is always important to first know the **business requirement** of the project.
Equally crucial is identifying the **appropriate framework, tools, and deployment platform** to use before pursuing the task.

* ⚡ Frameworks that are:

  * Easy to **understand** and **use**
  * Seamless during **coding**
  * Within **standards**

...are always picked because of the **integrity** they provide to solve problems without risking too much development time.

---

## 🐍 FastAPI – A Promising Python Framework

One such framework is **FastAPI**, created by **Sebastian Ramirez**.
It provides experienced developers, experts, and enthusiasts with the **best option** for building:

* 🌐 REST APIs
* 🧩 Microservices

FastAPI has gained popularity due to its **speed**, **ease of use**, and **modern design principles**.

---

## 🏗️ Before Diving Into Microservices

Before proceeding to the **core details** of building microservices using FastAPI, it is best to first learn the **building blocks** of this framework:

### 🔹 Client Requests

* How FastAPI **captures clients’ requests**
* The mechanism it uses to handle incoming data

### 🔹 HTTP Methods

* How FastAPI **builds the rules** for each HTTP method (`GET`, `POST`, `PUT`, `DELETE`, etc.)
* Ensuring requests are routed to the correct function logic

### 🔹 HTTP Responses

* How FastAPI **manages HTTP responses**
* Ensuring correct **status codes**, **content**, and **error handling** are applied

---

## 📖 Why Learn the Basics?

Learning the **basic components** is always essential because:

* 🛠️ It helps identify the **strengths** and **weaknesses** of the framework
* 🎯 It shows **to what extent** we can apply FastAPI to solve different **enterprise-grade** and **microservices-related problems**

---

# ⚙️ **Setting up the Development Environment for FastAPI**

## 🐍 Python Requirement

The **FastAPI framework** is a fast, seamless, and robust Python framework but can only work on **Python versions 3.6 and above**.
So make sure you have the correct version installed on your system.

---

## 💻 IDE Setup (Visual Studio Code)

The **Integrated Development Environment (IDE)** used here is **Visual Studio Code (VS Code)**, an **open-source tool**.

🔗 You can download it from: [https://code.visualstudio.com/](https://code.visualstudio.com/)

### ✅ Recommended VS Code Extensions

After installation, install these important extensions to enhance your coding experience:

* 🐍 **Python**
* 🐍 **Python for VS Code**
* 📦 **Python Extension Pack**
* 📏 **Python Indent**
* 🎨 **Material Icon Theme**

These provide:

* Syntax checking
* Syntax highlighting
* Editor support & auto-formatting

---

## 📦 Installing FastAPI and Dependencies

After successfully installing **Python** and **VS Code**, you can install **FastAPI** using a terminal/command prompt.

### 🔹 Step 1: Upgrade pip

Always make sure your `pip` (Python package manager) is up to date:

```bash
python -m pip install --upgrade pip
```

📌 **Explanation**:

* `python -m pip` → runs pip as a module of Python.
* `install --upgrade pip` → upgrades pip to the latest version.
* This prevents errors when installing new packages.

---

### 🔹 Step 2: Install FastAPI

Now install the FastAPI framework:

```bash
pip install fastapi
```

📌 **Explanation**:

* Installs the **core FastAPI framework**.
* Includes base modules but not optional extras.

---

### 🔹 Step 3: Install Uvicorn (ASGI Server)

FastAPI apps run on an **ASGI-based server** (Asynchronous Server Gateway Interface).
The most common is **Uvicorn**:

```bash
pip install uvicorn[standard]
```

📌 **Explanation**:

* `uvicorn` → the ASGI server used to run FastAPI.
* `[standard]` → installs standard optional dependencies (e.g., `uvloop`, `httptools`) for better performance.

---

### 🔹 Step 4: Install Multipart Support

For handling form data (like file uploads, form parameters):

```bash
pip install python-multipart
```

📌 **Explanation**:

* Required for **form handling** in FastAPI.
* Enables API endpoints to accept multipart/form-data requests.

---

## ⚡ Important Notes

* If you need to install the **complete FastAPI platform (with all optional dependencies):**

```bash
pip install fastapi[all]
```

* To install and utilize the **full-blown uvicorn server**:

```bash
pip install uvicorn
```

* For **encryption-related tasks** (like password hashing), install:

```bash
pip install bcrypt
```

---

## 🧩 Installed Modules Overview

By now, you should have installed these essential modules:

* **FastAPI** → main framework
* **pydantic** → for data validation
* **starlette** → for web handling under the hood
* **uvicorn** → ASGI server (runs synchronous & asynchronous apps)
* **python-multipart** → required for handling form data

---

## ⚡ Why Uvicorn is Used

* Uvicorn is an **ASGI-based server**.
* Supports both **synchronous** and **asynchronous** services.
* Makes FastAPI the **fastest Python framework** at the time of writing.

---

## 🚀 Next Step

After the installation and configuration of:

* 🛠️ Python
* 🛠️ VS Code
* 📦 FastAPI & modules
* ⚡ Uvicorn

👉 You’re ready to **start your first API implementation** using FastAPI. 🎉

---

# 🚀 **Initializing and Configuring FastAPI**

## 📂 Project Setup

Creating applications with **FastAPI** is easy and straightforward.
A simple application can be created by making a file named **`main.py`** inside your project folder:

```
/01-setup-fastapi/main.py
```

---

## 🐍 Basic FastAPI Application

Here’s the very first code snippet to start with:

```python
from fastapi import FastAPI

app = FastAPI()
```

### 🔎 Line-by-Line Explanation

1. **`from fastapi import FastAPI`**

   * Imports the **FastAPI class** from the `fastapi` module.
   * This class is the **core building block** for any FastAPI app.

2. **`app = FastAPI()`**

   * Instantiates the **FastAPI application object**.
   * The variable `app` is the **reference** to this object.
   * Later, this object will be used with **decorators** like `@app.get()` or `@app.post()`.

👉 You can replace `app` with any valid Python variable name (e.g., `main_app`, `forum`, `myapp`).

---

## 🧩 Using the @app Decorator

The `app` object is used as a **decorator** to provide your application with features like:

* 📌 Routes
* 🧩 Middleware
* ⚠️ Exception Handlers
* 🔀 Path Operations

### 🔹 Available Path Operations

FastAPI supports **8 HTTP methods** through decorators:

* `@app.get()`
* `@app.post()`
* `@app.delete()`
* `@app.put()`
* `@app.head()`
* `@app.patch()`
* `@app.trace()`
* `@app.options()`

These decorators are placed **on top of Python functions** that handle incoming requests and send responses.

---

## 📝 First API Endpoint Example

```python
@app.get("/index")
def index():
    return {"message": "Welcome Aspiring FastAPI!"}
```

### 🔎 Line-by-Line Explanation

1. **`@app.get("/index")`**

   * Defines a **GET endpoint** at the URL path `/index`.
   * This means: whenever someone sends a GET request to `http://localhost:8000/index`, this function will run.

2. **`def index():`**

   * Defines a **Python function** named `index`.
   * Acts as the **handler** for the `/index` request.

3. **`return {"message": "Welcome Aspiring FastAPI!"}`**

   * Returns a **JSON response** to the client.
   * FastAPI automatically converts Python dictionaries into JSON format.

💡 Example Response when visiting `/index`:

```json
{
  "message": "Welcome Aspiring FastAPI!"
}
```

---

## ▶️ Running the Application

Use the following command to run your application locally:

```bash
uvicorn main:app --reload
```

### 🔎 Command Breakdown

* **`uvicorn`** → Starts the Uvicorn ASGI server.
* **`main:app`** →

  * `main` = the filename (`main.py` without `.py`).
  * `app` = the FastAPI instance created (`app = FastAPI()`).
* **`--reload`** → Enables **live reload**, meaning the server restarts automatically when you change the code.

---

## 📋 Example Console Output

```bash
> uvicorn main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\Hashim\\Desktop\\resources\\fastapi\\01-setup-fastapi']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [7876] using WatchFiles
INFO:     Started server process [11656]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 🔎 Explanation

* Uvicorn runs the app on **localhost (127.0.0.1)** using **port 8000**.
* Default URL for your endpoint: 👉 [http://localhost:8000/index](http://localhost:8000/index)
* To stop the server → Press **CTRL + C**

---

# 🌐 **Designing and Implementing REST APIs with FastAPI**

## 🔎 What is a REST API?

The **Representation State Transfer (REST) API** defines the **rules, processes, and tools** that allow **interaction among microservices**.

* REST APIs are composed of **method services**, which are:

  * Identified by **endpoint URLs**
  * Executed via **HTTP request methods** (`GET`, `POST`, `PUT`, `DELETE`, etc.)

---

## 🚀 API-First Microservices Development

One of the most effective modern strategies is **API-first microservices development**:

* 🎯 Focuses first on **client needs**
* 🏗️ Then identifies **what API services** are needed

👉 In our **online academic discussion forum app**, we prioritized features like:

* 👤 User **sign-up**
* 🔑 User **login**
* 📝 Profile management
* 💬 Posting messages
* 💬 Managing post replies

These are implemented as **FastAPI service methods** using Python’s `def` keyword and decorated with the appropriate **HTTP method** (`@app.get`, `@app.post`, etc.).

---

# 🔑 Login Service Example (GET Method)

The **login service** requires **username** and **password** request parameters.

```python
from bcrypt import hashpw, gensalt, checkpw

valid_users = dict()

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
```

---

### 📝 Code Walkthrough (Line-by-Line)

1. **`from bcrypt import hashpw, gensalt, checkpw`**

   * Imports functions from **bcrypt** for password encryption and validation.
   * `checkpw` → checks if entered password matches the stored hashed password.

2. **`valid_users = dict()`**

   * A dictionary to **store valid registered users**.
   * Keys = usernames, Values = user objects.

3. **`@app.get("/login")`**

   * Defines a **GET endpoint** at `/login`.
   * Requires query parameters: `username` and `password`.

4. **`if valid_users.get(username) == None:`**

   * Checks if the username exists.
   * If not → returns: `{"message": "User Does Not Exist"}`.

5. **`else: user = valid_users.get(username)`**

   * Retrieves the user object.

6. **`if checkpw(password.encode(), user.passphrase.encode()):`**

   * Encodes the entered password.
   * Compares with the stored hashed password (`user.passphrase`).

7. **Return values:**

   * ✅ If valid → returns the **user object**.
   * ❌ If invalid → returns `{"message": "Invalid User"}`.

---

## 🔐 How Password Validation Works (Dry Run Example)

Suppose we have:

```python
valid_users = {
    "ali": User(username="ali", passphrase="$2b$12$...")
}
```

* Input → `username="ali", password="mypassword"`
* `checkpw("mypassword".encode(), stored_hash)` → ✅ returns True if hash matches.
* Response → User object for `"ali"`.

---

# 📝 Validating Request Bodies with Pydantic

## 🔎 Why Validation?

Validation ensures that **only defined data** is received → prevents:

* 🚫 Malicious attacks
* 🚫 Unexpected data

## 📦 Pydantic

* A **Python library** used by FastAPI for validation.
* Uses **Python type annotations**.
* Models are created by subclassing **`BaseModel`**.

Example:

```python
from pydantic import BaseModel

class User(BaseModel):
    username: str
    password: str
```

---

# 🆕 Sign-Up Service Example (POST Method)

The **sign-up service** allows users to register with a username and password.

```python
from pydantic import BaseModel

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
```

---

### 📝 Code Walkthrough (Line-by-Line)

1. **`class User(BaseModel):`**

   * Defines a **Pydantic model**.
   * Ensures request body has `username` (string) and `password` (string).

2. **`pending_users = dict()`**

   * Stores **newly registered users** before moving them to `valid_users`.

3. **`@app.post("/login/signup")`**

   * Defines a **POST endpoint** at `/login/signup`.

4. **Function `signup(uname: str, passwd: str):`**

   * Takes username and password from the client.

5. **Condition Checks:**

   * If both `uname` and `passwd` are missing → returns `{"message": "Invalid User"}`.
   * If `uname` already exists in `valid_users` → returns `{"message": "User Already Exists"}`.

6. **Creating a New User:**

   * `user = User(username=uname, password=passwd)` → creates a new Pydantic user object.
   * Adds it to `pending_users`.
   * Returns the newly created user.

---

## ⚡ Flow of Signup & Login

1. 📝 **Sign-up (POST)** → User provides credentials → stored in `pending_users`.
2. 🔑 **Login (GET)** → System checks against `valid_users`.
3. 🔒 **bcrypt checkpw()** ensures passwords match securely.

---

# 👤 **Profile Management with FastAPI (PUT Method**)

## 📌 Update Profile Service

Among the **profile management services**, the `update_profile()` service acts as a **PUT API service**.

* It requires:

  * The client’s **username** (as a key).
  * A **new UserProfile model object** to replace existing profile information.

---

## 🐍 Code Implementation

```python
from uuid import UUID, uuid1
from typing import Optional, List, Dict
from datetime import date, datetime
from enum import Enum

valid_profiles = dict()

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
            return {"message": "User Does Not Exist"}
```

---

## 📝 Line-by-Line Explanation

### 📦 Imports

1. **`from uuid import UUID, uuid1`**

   * `UUID` → Used for unique identifiers for each user.
   * `uuid1()` → Generates unique IDs based on timestamp and machine info.

2. **`from typing import Optional, List, Dict`**

   * `Optional` → Allows fields to be optional with default values.
   * `List` and `Dict` → For handling collections (not directly used here but available for extension).

3. **`from datetime import date, datetime`**

   * `date` → Used for birthdays.
   * `datetime` → Available for timestamp operations.

4. **`from enum import Enum`**

   * Provides enumerations for fixed categories (like user roles).

---

### 🏷️ User Type Enum

```python
class UserType(str, Enum):
    admin = "admin"
    teacher = "teacher"
    alumni = "alumni"
    student = "student"
```

* Defines **user categories**.
* Ensures `user_type` is one of these four → `"admin"`, `"teacher"`, `"alumni"`, `"student"`.

---

### 👤 User Profile Model

```python
class UserProfile(BaseModel):
    firstname: str
    lastname: str
    middle_initial: str
    age: Optional[int] = 0
    salary: Optional[int] = 0
    birthday: date
    user_type: UserType
```

* A **Pydantic model** for structured profile data.
* Fields:

  * `firstname`, `lastname`, `middle_initial` → Required strings.
  * `age` → Optional, defaults to `0`.
  * `salary` → Optional, defaults to `0`.
  * `birthday` → Must be a valid `date`.
  * `user_type` → Must match one of the **UserType Enum values**.

💡 Validation Example:

* ✅ `user_type="student"` → Accepted.
* ❌ `user_type="doctor"` → Rejected.

---

### 🔄 Update Profile Endpoint

```python
@app.put("/account/profile/update/{username}")
def update_profile(username: str, id: UUID, new_profile: UserProfile):
```

* **`@app.put`** → Defines a **PUT endpoint**.
* Endpoint URL: `/account/profile/update/{username}`

  * `{username}` → Path parameter (the user to update).
* Parameters:

  * `username: str` → Path variable.
  * `id: UUID` → User’s unique identifier (security check).
  * `new_profile: UserProfile` → Request body (new profile data).

---

### 🧩 Logic Flow

```python
if valid_users.get(username) == None:
    return {"message": "User Does Not Exist"}
```

* If username doesn’t exist in `valid_users` → return error.

```python
else:
    user = valid_users.get(username)
    if user.id == id:
        valid_profiles[username] = new_profile
        return {"message": "Profile Successfully Updated", "profile": new_profile}
    else:
        return {"message": "User Does Not Exist"}
```

* Retrieves user object.
* Compares `user.id` with provided `id`.

  * ✅ If match → profile is replaced with `new_profile`.
  * ❌ If mismatch → error returned.

---

## ⚡ Dry Run Example

### Input Request:

```http
PUT /account/profile/update/ali?id=550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
  "firstname": "Ali",
  "lastname": "Khan",
  "middle_initial": "A",
  "age": 25,
  "salary": 50000,
  "birthday": "2000-01-01",
  "user_type": "student"
}
```

### Server Logic:

* Checks if `ali` exists in `valid_users`.
* Verifies if `id` matches stored UUID.
* Updates `valid_profiles["ali"]` with new profile.

### Response:

```json
{
  "message": "Profile Successfully Updated",
  "profile": {
    "firstname": "Ali",
    "lastname": "Khan",
    "middle_initial": "A",
    "age": 25,
    "salary": 50000,
    "birthday": "2000-01-01",
    "user_type": "student"
  }
}
```
---

# ✂️ **Partial Updates with PATCH in FastAPI**

## 📌 Why PATCH Instead of PUT?

* **PUT** → Requires a **full replacement** of an object.
* **PATCH** → Used for **partial updates** where only some fields change.
* ✅ Lightweight and efficient for small modifications.
* ❌ PUT would be “overkill” if only a few fields need to be updated.

In this case, we only want to update **names** (first, last, and middle initial) of a profile → so we use **PATCH**.

---

## 🐍 Code Implementation

```python
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
```

---

## 📝 Line-by-Line Explanation

### 🔹 Decorator

```python
@app.patch("/account/profile/update/names/{username}")
```

* Defines a **PATCH endpoint** at `/account/profile/update/names/{username}`.
* `{username}` → path parameter (target user).

---

### 🔹 Function Definition

```python
def update_profile_names(username: str, id: UUID, new_names: Dict[str, str]):
```

* `username: str` → The username whose profile will be updated.
* `id: UUID` → Unique identifier for the user (to verify authenticity).
* `new_names: Dict[str, str]` → Request body containing new values for names in dictionary format.

---

### 🔹 Validation

```python
if valid_users.get(username) == None:
    return {"message": "User Does Not Exist"}
```

* If user doesn’t exist → return error message.

```python
elif new_names == None:
    return {"message": "new names are required"}
```

* If client didn’t send new names → return error.

---

### 🔹 Update Logic

```python
else:
    user = valid_users.get(username)
    if user.id == id:
        profile = valid_profiles[username]
        profile.firstname = new_names['fname']
        profile.lastname = new_names['lname']
        profile.middle_initial = new_names['mi']
        valid_profiles[username] = profile
        return {"message": "Profile Names Successfully Updated", "profile": profile}
```

* ✅ If user exists AND `id` matches →

  * Retrieves user’s current profile.
  * Updates only **first name, last name, and middle initial**.
  * Saves updated profile back to `valid_profiles`.
  * Returns success message + updated profile.

```python
else:
    return {"message": "User Does Not Exist"}
```

* If UUID doesn’t match → return error.

---

## ⚡ Dry Run Example

### Input Request

```http
PATCH /account/profile/update/names/ali?id=550e8400-e29b-41d4-a716-446655440000
Content-Type: application/json

{
  "fname": "Ali",
  "lname": "Khan",
  "mi": "A"
}
```

### Processing

1. Finds user `"ali"` in `valid_users`.
2. Confirms `id` matches stored UUID.
3. Updates only:

   * `firstname` → "Ali"
   * `lastname` → "Khan"
   * `middle_initial` → "A"

### Response

```json
{
  "message": "Profile Names Successfully Updated",
  "profile": {
    "firstname": "Ali",
    "lastname": "Khan",
    "middle_initial": "A",
    "age": 25,
    "salary": 50000,
    "birthday": "2000-01-01",
    "user_type": "student"
  }
}
```

💡 Notice that other profile fields like `age`, `salary`, `birthday`, and `user_type` remain **unchanged**.

---

## 📌 Key Differences: PUT vs PATCH

| Feature        | PUT (Full Update) 🏗️ | PATCH (Partial Update) ✂️ |
| -------------- | --------------------- | ------------------------- |
| Scope          | Entire object         | Specific fields only      |
| Request Body   | Full object required  | Partial object allowed    |
| Use Case       | Replace profile       | Update just names         |
| Example Fields | All user info         | First/last/middle names   |

---

# 🗑️ **Deleting Records with FastAPI (DELETE Method)**

## 📌 Why DELETE?

* The **DELETE** HTTP method is used to **remove records or information**.
* Typically requires:

  * A **unique identifier** (e.g., UUID).
  * A **valid user key** (e.g., username).
* Ensures only the rightful owner or admin can remove data.

---

## 🐍 Example: Delete Discussion Post

```python
discussion_posts = dict()

@app.delete("/discussion/posts/remove/{username}")
def delete_discussion(username: str, id: UUID):
    if valid_users.get(username) == None:
        return {"message": "User Does Not Exist"}
    elif discussion_posts.get(id) == None:
        return {"message": "Post Does Not Exist"}
    else:
        del discussion_posts[id]
        return {"message": "Post Successfully Deleted"}
```

---

## 📝 Line-by-Line Explanation

### 🔹 Data Store

```python
discussion_posts = dict()
```

* Dictionary to store all discussion posts.
* Keys = post UUIDs, Values = post objects.

---

### 🔹 Endpoint

```python
@app.delete("/discussion/posts/remove/{username}")
```

* Defines a **DELETE endpoint**.
* Path = `/discussion/posts/remove/{username}`.
* `{username}` → path parameter (the user requesting the deletion).

---

### 🔹 Function Definition

```python
def delete_discussion(username: str, id: UUID):
```

* Parameters:

  * `username: str` → path parameter.
  * `id: UUID` → the unique identifier of the post to be deleted.

---

### 🔹 Validation Checks

```python
if valid_users.get(username) == None:
    return {"message": "User Does Not Exist"}
```

* Checks if the requesting user is valid.

```python
elif discussion_posts.get(id) == None:
    return {"message": "Post Does Not Exist"}
```

* Ensures the post with that UUID exists.

---

### 🔹 Deletion Logic

```python
else:
    del discussion_posts[id]
    return {"message": "Post Successfully Deleted"}
```

* If user exists **and** post exists → deletes post from `discussion_posts`.
* Returns a success confirmation.

---

## ⚡ Dry Run Example

### Input Request

```http
DELETE /discussion/posts/remove/ali?id=550e8400-e29b-41d4-a716-446655440000
```

### Possible Scenarios

1. ❌ If `"ali"` not found in `valid_users`:

   ```json
   { "message": "User Does Not Exist" }
   ```

2. ❌ If post with UUID doesn’t exist:

   ```json
   { "message": "Post Does Not Exist" }
   ```

3. ✅ If both checks pass:

   ```json
   { "message": "Post Successfully Deleted" }
   ```

---

## 📌 Best Practices for Path Operations

* Every path operation should have a **unique endpoint URL** in `str` format.
* Good practice:

  * Use a **common top-level base path** (e.g., `/ch01`).
  * Differentiate by **subdirectories** (e.g., `/ch01/discussion/posts/remove/{username}`).

---

## 📊 API Documentation with OpenAPI

After running the Uvicorn server, you can **validate all endpoints** via FastAPI’s built-in OpenAPI docs:

👉 Open in browser: [http://localhost:8000/docs](http://localhost:8000/docs)

This opens the **Swagger UI** dashboard (Figure 1.2), listing all created API methods with interactive testing options.

---
\