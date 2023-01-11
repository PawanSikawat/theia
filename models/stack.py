from pydantic import BaseModel



class Stack(BaseModel):
    name: str
    project: str


