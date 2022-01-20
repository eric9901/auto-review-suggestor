import PyPDF2
type = input ("Input the file type: D(Doc) P(PDF) ")
Title= input("Input the file name")
if type=='D':
    Title+='.doc'
elif type == 'P':
    Title+='.pdf'

pdfFileObject = open(Title,'rb')
pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject)
for page in pdfReaderObject.pages:
    print(page.extractText())

#pageCount = pdfReaderObject.numPages
#pageObj = pdfReaderObject.getPage(pageCount-1)
#print(pageCount)
#text += pageObj.extractText()

