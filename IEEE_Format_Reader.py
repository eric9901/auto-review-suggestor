from cgitb import reset
import PyPDF2
import re
import time
def checkNum(inputString):
    return not bool(re.search(r'\d', inputString))
def getIEEEfAuthor(Title):
    Title+='.pdf'
    pdfFileObject = open(Title,'rb')
    pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject,strict=False)
    NumPage=pdfReaderObject.getNumPages()
    res=''
    for k in reversed(range(NumPage)): 
        page=pdfReaderObject.getPage(k)
        PaperText=page.extractText()
    #get Reference List
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
            Author.append((i,'2003'))

    return(Author)




