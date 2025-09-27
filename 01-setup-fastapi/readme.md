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
