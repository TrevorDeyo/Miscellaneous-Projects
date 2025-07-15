import PyPDF2
from PyPDF2 import PdfReader

print(PyPDF2.__version__)

# Load PDF
reader = PdfReader("AQA GCSE textbook.pdf")

# Extract text from each page
# for page in reader.pages:
i = 0
for page in reader.pages:
    if i < 2:
        print(page.extract_text())
        i += 1