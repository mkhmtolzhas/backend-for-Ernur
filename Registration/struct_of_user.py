from pydantic import BaseModel


class User(BaseModel):
    first_name : str
    second_name: str
    email: str
    phone_number: str
    password : str
    address: str
    city: str
    sex: str = None

class User_for_autorization(BaseModel):
    email: str
    phone_number: str
    
