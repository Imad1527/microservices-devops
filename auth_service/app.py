from fastapi import FastAPI

app = FastAPI(title="Auth Service")

users = []

@app.get("/")
def health():
    return {"service": "auth", "status": "running"}

@app.post("/register")
def register_user(username: str, password: str):
    users.append({"username": username, "password": password})
    return {"message": "User registered successfully"}

@app.post("/login")
def login_user(username: str, password: str):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return {"message": "Login successful"}
    return {"message": "Invalid credentials"}
