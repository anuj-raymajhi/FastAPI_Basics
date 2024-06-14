from main import app, HTTPException

teachers_db = {
    1: {
        "name": "Hari Bahadur",
        "qual": "Bachelors",
        "license" : False
    }
}

@app.get("/get-teachers/{teacher_id}")
def get_teacher(teacher_id: int):
    if teacher_id not in teachers_db.keys():
        raise HTTPException(
            status_code=404,
            detail="Teacher Not Found."
        )
    return teachers_db[teacher_id]