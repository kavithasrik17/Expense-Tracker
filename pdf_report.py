from reportlab.pdfgen import canvas
def generate_pdf(date, data, grand_total):
    pdf = canvas.Canvas("expense_report.pdf")
    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(160, 820, "Daily Expense Report")
    pdf.setFont("Helvetica", 12)
    pdf.drawString(50, 780, f"Date: {date}")
    pdf.setFont("Helvetica-Bold", 10)
    pdf.drawString(50, 740, "Category")
    pdf.drawString(300, 740, "Total")
    y = 710
    pdf.setFont("Helvetica", 10)
    for item in data:
        pdf.drawString(50, y, item["category"])
        pdf.drawString(300, y, str(item["total"]))
        y -= 20
    pdf.setFont("Helvetica-Bold", 12)
    pdf.drawString(50, y - 20, f"Grand Total: {grand_total}")
    pdf.save()
