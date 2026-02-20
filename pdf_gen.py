from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create a PDF file
file_name = 'reportlab_example.pdf'
c = canvas.Canvas(file_name, pagesize=letter)

# Add content
c.drawString(100, 750, "Hello, this is a PDF generated with ReportLab!")
c.setFont("Helvetica-Bold", 12)
c.drawString(100, 730, "You can draw shapes, lines, and more.")

# Draw a line
c.line(50, 720, 550, 720)

# Save the PDF document
c.save()

print(f"PDF '{file_name}' generated successfully!")
