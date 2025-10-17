from pydantic import BaseModel


class userData(BaseModel):
    email : str
    name : str
    stack: str

class factResponse(BaseModel):
    status : str
    user : userData
    timestamp : str
    fact : str 

    class Config():
        from_atttributes = True