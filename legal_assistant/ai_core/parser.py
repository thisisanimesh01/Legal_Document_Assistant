import fitz  # PyMuPDF
import docx

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        doc = fitz.open(file_path)
        return " ".join([page.get_text() for page in doc])
    elif file_path.endswith('.docx'):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return ""
