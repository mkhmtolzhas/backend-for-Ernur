from fastapi import FastAPI, HTTPException
import json
from struct_of_user import User

app = FastAPI()

def to_str(user):
    return str(user)

@app.post('/register/')
async def user_registration(user : User):
    user = user.dict()
    with open("user.json", "r") as users:
        data = json.load(users)


    for value in data.values():
        if user['email'] == value['email']:
            raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует")
        elif user['phone_number'] == value['phone_number']:
            raise HTTPException(status_code=400, detail="Пользователь с таким номером уже существует")
        
    try:
        data[f"user{len(data) + 1}"] = user
        with open("user.json", "w") as users:
            users.write(json.dumps(data, indent=4))
        return "Успешно"
    except HTTPException:
        return "Не удалось зарегестрироватся, попробуйте заново"
    

# @app.post('/authorization/')
# async def authorization()
