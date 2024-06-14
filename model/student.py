from typing import Optional
from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: int
    year: str

    def set_name(self, new_name: str):
        self.name = new_name

    def set_age(self, new_age: int):
        self.age = new_age

    def set_year(self, new_year: str):
        self.year = new_year

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None