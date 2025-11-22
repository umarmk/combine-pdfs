from pypdf import PdfWriter
from reportlab.pdfgen import canvas

def create_pdf(filename, text):
    c = canvas.Canvas(filename)
    c.drawString(100, 750, text)
    c.save()

create_pdf("test1.pdf", "This is the first PDF.")
create_pdf("test2.pdf", "This is the second PDF.")
