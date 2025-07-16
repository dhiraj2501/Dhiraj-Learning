from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google_sheets_api import read_sheet_data, write_sheet_data

app = FastAPI()

origins = [
    "http://localhost:3000",  # React app address
    "http://127.0.0.1:3000", # React app address
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Student(BaseModel):
    name: str
    student_id: str
    email: str

@app.get("/")
async def root():
    return {"message": "QRtendence Backend is running!"}

@app.get("/sheet_data")
async def get_sheet_data(spreadsheet_id: str, range_name: str):
    data = read_sheet_data(spreadsheet_id, range_name)
    if data:
        return {"data": data}
    return {"message": "Could not retrieve data from Google Sheet."}

@app.post("/register_student")
async def register_student(student: Student):
    # Replace with your actual student registration spreadsheet ID and sheet name
    STUDENT_SPREADSHEET_ID = "YOUR_STUDENT_SPREADSHEET_ID_HERE"
    RANGE_NAME = "Students!A:C"  # Assuming columns A, B, C for Name, Student ID, Email

    values = [[student.name, student.student_id, student.email]]
    write_result = write_sheet_data(STUDENT_SPREADSHEET_ID, RANGE_NAME, values)

    if write_result:
        return {"message": "Student registered successfully!", "student": student}
    return {"message": "Failed to register student."}
