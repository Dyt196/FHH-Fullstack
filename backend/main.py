from fastapi import FastAPI, Query
from pydantic import BaseModel
import sqlite3
from typing import List

app = FastAPI()

# ----------- MODELS -----------

class Consultation(BaseModel):
    patient_name: str
    notes: str
    diagnosis_codes: List[str]

# ----------- DATABASE SETUP -----------

def init_db():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS diagnosis (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        code TEXT,
        description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS consultation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        notes TEXT,
        diagnosis_codes TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ----------- ROUTES -----------

@app.get("/diagnosis")
def search_diagnosis(search: str = Query("")):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT code, description FROM diagnosis WHERE description LIKE ?",
        (f"%{search}%",)
    )

    result = cursor.fetchall()
    conn.close()

    return [{"code": r[0], "description": r[1]} for r in result]


@app.post("/consultation")
def create_consultation(data: Consultation):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO consultation (patient_name, notes, diagnosis_codes) VALUES (?, ?, ?)",
        (data.patient_name, data.notes, ",".join(data.diagnosis_codes))
    )

    conn.commit()
    conn.close()

    return {"message": "Saved successfully"}


@app.get("/consultation")
def list_consultation():
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM consultation")
    rows = cursor.fetchall()
    conn.close()

    return rows