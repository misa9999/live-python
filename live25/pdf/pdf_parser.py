from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.converter import PDFPageAggregator

fp = open("Lista_samurai_x.pdf", "rb")

parser = PDFParser(fp)

doc = PDFDocument(parser)
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize("")

rsrcmgr = PDFResourceManager()

laparamns = LAParams()
laparamns.line_margin = 0.3
laparamns.word_margin = 0.3

device = PDFPageAggregator(rsrcmgr, laparamns=laparamns)
interpreter = PDFPageInterpreter(rsrcmgr, device)

for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for ltobject in layout:
        print(ltobject.get_text())
