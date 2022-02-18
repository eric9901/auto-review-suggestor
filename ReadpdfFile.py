import PyPDF2
import re
Title= input("Input the file name: ")
Title+='.pdf'
pdfFileObject = open(Title,'rb')
pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject)

NumPage=pdfReaderObject.getNumPages()
page=pdfReaderObject.getPage(NumPage-1)
PaperText=page.extractText()
ReferList=PaperText.partition('References');
res = ReferList[2]
Temp=res.split('.,')
Author=[]
#check element is it the author name 
for i in Temp:
    if(len(i)<=20 and len(i)>3):
       Author.append(i)
        


