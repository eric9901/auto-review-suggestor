import PyPDF2
import re
Title= input("Input the file name: ")
Title+='.pdf'
pdfFileObject = open(Title,'rb')
pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject)

NumPage=pdfReaderObject.getNumPages()
for k in range(NumPage,0): 
    page=pdfReaderObject.getPage(k)
    PaperText=page.extractText()
    #get Reference List
    res=''
    ReferList=PaperText.partition('References');
    if(ReferList[1]=='References'):
        res += ReferList[2]
        break;
    else:
        res +=PaperText
Temp=res.split('.,')
Author=[]
#check element is it the author name 
for i in Temp:
    #Name length check
    if(len(i)<=20 and len(i)>3):
       Author.append(i)
        


