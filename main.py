from fastapi import FastAPI
from fastapi.responses import FileResponse
from database import connection, table
from models import Expense
from reports.pdf_report import generate_pdf

app = FastAPI(title="Daily Track Your Expenses")
table()
@app.post("/add")
def add_expense(expense: Expense):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO expenses
    (date, category, amount, description, payment_mode,
     merchant_name, location, notes, created_by)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        expense.date,
        expense.category,
        expense.amount,
        expense.description,
        expense.payment_mode,
        expense.merchant_name,
        expense.location,
        expense.notes,
        expense.created_by
    ))
    conn.commit()
    conn.close()
    return {"message": "Your expense added successfully"}
@app.get("/expenses")
def get_expenses():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]
@app.put("/update/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE expenses
    SET date = ?, category = ?, amount = ?, description = ?,
        payment_mode = ?, merchant_name = ?, location = ?,
        notes = ?, created_by = ?
    WHERE expense_id = ?
    """, (
        expense.date,
        expense.category,
        expense.amount,
        expense.description,
        expense.payment_mode,
        expense.merchant_name,
        expense.location,
        expense.notes,
        expense.created_by,
        expense_id
    ))
    conn.commit()
    conn.close()
    return {"message": "Expense updated successfully"}
@app.delete("/delete/{expense_id}")
def delete_expense(expense_id: int):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM expenses WHERE expense_id = ?",
        (expense_id,)
    )
    conn.commit()
    conn.close()
    return {"message": "Expense deleted Successfully"}
@app.get("/summary/category")
def category_summary():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT category, SUM(amount) AS total_expense
    FROM expenses
    GROUP BY category
    """)
    result = [
        {
            "category": row["category"],
            "total_expense": row["total_expense"]
        }
        for row in cursor.fetchall()
    ]
    conn.close()
    return result
@app.get("/summary/date/{date}")
def date_summary(date: str):
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT SUM(amount) AS total
    FROM expenses
    WHERE date = ?
    """, (date,))
    result = cursor.fetchone()
    conn.close()
    return {
        "date": date,
        "total_expense": result["total"] if result["total"] else 0
    }
@app.get("/report/pdf")
def download_pdf():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    GROUP BY category
    """)
    data = [
        {"category": row["category"], "total": row["total"]}
        for row in cursor.fetchall()
    ]
    conn.close()
    generate_pdf(data)
    return FileResponse(
        "expense_report.pdf",
        media_type="application/pdf",
        filename="expense_report.pdf"
    )
@app.get("/report/pdf/{date}")
def pdf_report(date: str):
    conn = connection()
    cursor = conn.cursor()

    # Category-wise totals for the date
    cursor.execute("""
    SELECT category, SUM(amount) AS total
    FROM expenses
    WHERE date = ?
    GROUP BY category
    """, (date,))

    data = [
        {"category": row["category"], "total": row["total"]}
        for row in cursor.fetchall()
    ]
    cursor.execute("""
    SELECT SUM(amount) AS grand_total
    FROM expenses
    WHERE date = ?
    """, (date,))
    grand_total = cursor.fetchone()["grand_total"] or 0
    conn.close()
    generate_pdf(date, data, grand_total)
    return FileResponse(
        "expense_report.pdf",
        media_type="application/pdf",
        filename="expense_report.pdf"
    )
