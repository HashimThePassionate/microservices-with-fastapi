from fastapi import FastAPI

app = FastAPI()


@app.get("/index")
def index():
    return {"message": "Welcome Aspiring FastAPI!"}
