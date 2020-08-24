from docx import Document

document = Document("Lista_samurai_X.docx")
for para in document.paragraphs:
    print(para.text)
