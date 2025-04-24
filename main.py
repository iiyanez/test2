from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AuthRequest(BaseModel):
    username: str
    password: str

FAKE_DB = {
    "isa": {"password": "1234", "data": {"plan": "premium", "status": "activo"}},
    "cat": {"password": "abcd", "data": {"plan": "free", "status": "suspendido"}},
}

@app.post("/auth")
def authenticate(user: AuthRequest):
    if user.username in FAKE_DB and FAKE_DB[user.username]["password"] == user.password:
        return {"success": True, "data": FAKE_DB[user.username]["data"]}
    raise HTTPException(status_code=401, detail="Credenciales inválidas")