from fastapi import FastAPI,Depends,HTTPException

from jose import jwt, JWSError
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
ALGORITHM = "HS256"
SECRET_KEY = "A Secure Secret Key"

def create_access_token(subject: str , expires_delta: timedelta) -> str:
    expire = datetime.utcnow() + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token:str):
    decode_data=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    return decode_data
app= FastAPI()
@app.get("/encodedata")
def get_access_token(user_name: str):
    access_token_expire= timedelta(minutes=1)
    access_token_generated= create_access_token(subject=user_name,expires_delta=access_token_expire)
    return {"token_username":access_token_generated}

@app.get("/decodedata")
def decodedstring(encodedstring:str):
    data_decode=decode_access_token(encodedstring)
    return data_decode

fake_users_db={
    "Talha":{
        "username":"talha",
        "password":"12345",
    },
    "Ali":{
        "username":"talha",
        "password":"12345"
    }
}

@app.post("/login")
def getuserdata(form_data:Annotated[OAuth2PasswordRequestForm,Depends(OAuth2PasswordRequestForm)]):
    user_in_fake_db = fake_users_db.get(form_data.username)
    if not user_in_fake_db:
        raise HTTPException(status_code=400, detail="Incorrect username")

    if not form_data.password == user_in_fake_db["password"]:
        raise HTTPException(status_code=400, detail="Incorrect password")

    access_token_expires = timedelta(minutes=1)

    access_token = create_access_token(
        subject=user_in_fake_db["username"], expires_delta=access_token_expires)
    return access_token