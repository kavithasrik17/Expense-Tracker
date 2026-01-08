# Expense Tracker API (FastAPI + SQLite)

A simple Expense Tracker REST API built using **FastAPI** and **SQLite** (without ORM).  
This project supports CRUD operations, summary reports, and PDF/Excel report generation.

---

## Features

- Add, update, delete expenses
- View all expenses
- Generate total expenses by category
- Generate total expenses for a specific date
- Export reports to PDF
- Uses raw SQL (no SQLAlchemy ORM)
- Beginner-friendly and interview-ready

---

## Tech Stack

- Backend: FastAPI
- Database: SQLite
- Server: Uvicorn
- PDF Report: ReportLab
- Excel Report: OpenPyXL
- API Testing: Postman

---

## Project Structure

expense_tracker
- main.py
- database.db
- reports/ pdf_report.py
- requirements.txt
- README.md


---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/kavithasrik17/Expense-Tracker
cd Expense-Tracker
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn main:app --reload
```

Server will run at:
http://127.0.0.1:8000

## API Endpoints
### Add Expense
POST /add

Request body:

{
  "date": "2026-01-08",
  "category": "Snacks",
  "amount": 250,
  "description": "Evening Snacks",
  "payment_mode": "Cash",
  "merchant_name": "Cafe",
  "location": "City",
  "notes": "",
  "created_by": "User1"
}

### Get All Expenses
GET /expenses

### Update Expense
PUT /update/{id}

### Delete Expense
DELETE /delete/{id}

### Reports
Category-wise Expense Summary (All Dates)
GET /summary/category

### Date-wise Expense Summary
GET /summary/date/{date}

### PDF Report (Date-wise with Category)
GET /report/pdf?date=2025-01-10


