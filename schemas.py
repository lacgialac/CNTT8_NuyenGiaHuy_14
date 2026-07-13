from pydantic import BaseModel


class createdish(BaseModel):
    id:int
    item_name:str
    category:str
    price:float
    status:str
    
class updatedish(BaseModel):
    item_name:str
    category:str
    price:float
    status:str
    

    
    