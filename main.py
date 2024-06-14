from fastapi import FastAPI, Path, HTTPException
from typing import Optional
from data.students import students_db
from model.student import Student, StudentUpdate

app = FastAPI()

# concept of endpoints
"""
    HTTP requests : common
    GET : get and information
    POST : create something new
    PUT : update
    DELETE : delete something
"""


@app.get("/")
def index():
    return {
        "name" : "first data"
    }

@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    if student_id not in students_db.keys():
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    return students_db[student_id]

#gt = greater than, ge=greater than of equal to, similarly 'lt' and 'le'

@app.get("/get-by-name")
def get_student(* ,name: Optional[str] = None):
    for student_id in students_db:
        if students_db[student_id].name == name:
            return students_db[student_id]
    return {
        "Data" : "Not Found"
    }

# python doesn't allow Optional parameter to occur before the required params, thus use
# def func(*, optional_param, req_param): format

# by doing name: Optional[str] = None, we are providing None as a default value, if we set name: Optional[str] = 'Anuj Rayamajhi', it will be default value for name

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students_db.keys():
        return {
            'Error' : 'Id is already taken'
        }

    students_db[student_id] = student
    return students_db[student_id]

@app.put("/update-student/{student_id}")
async def update_student(student_id: int, student: StudentUpdate):
    if student_id not in students_db.keys():
        raise HTTPException(status_code=404, detail="Student Not Found")
    
    existing_student = students_db[student_id]

    if student.name is not None:
        existing_student.set_name(student.name)
    if student.year is not None:
        existing_student.set_year(student.year)
    if student.age is not None:
        existing_student.set_age(student.age)

    students_db[student_id] = existing_student

    return existing_student

# to update only certain parameters create a similar class with original data, then assign Student -> StudentUpdate, StudentUpdate has similar attribute to that of
# Student class, accept in StudentUpdate, assign to Student

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students_db.keys():
        raise HTTPException(
            status_code=404,
            detail="Student Not Found"
        )
    tempName = students_db[student_id].name
    del students_db[student_id]
    raise HTTPException(
        status_code=200,
        detail=f"{tempName}'s record has been deleted."
    )