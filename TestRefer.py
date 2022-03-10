from cgitb import reset
import PyPDF2
import re
import time
def checkNum(inputString):
    return not bool(re.search(r'\d', inputString))
def getRefAuthor(Title):
    Author=[]
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
    a=re.split("\(\d{4}\)",res)
    refYear=re.findall("\(\d{4}\)",res)
    for i in a:
        t=re.findall(",.*",i)
        if t:
            print(t[-1])
    return(Author)
file = input("input pdf file name: ")
#get Author in reference list
Author=getRefAuthor(file)
print(Author)