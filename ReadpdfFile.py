import PyPDF2
type = input ("Input the file type: D(Doc) P(PDF) ")
Title= input("Input the file name")
if type=='D':
    Title+='.doc'
elif type == 'P':
    Title+='.pdf'

pdfFileObject = open(Title,'rb')
pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject)
#firstPageObject =pdfReaderObject.getPage(0)
#print(firstPageObject.extractText())
docInfo = pdfReaderObject.getDocumentInfo()
print(docInfo.title)