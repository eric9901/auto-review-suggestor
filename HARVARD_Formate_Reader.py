from cgitb import reset
import PyPDF2
import re
import time
def checkNum(inputString):
    return not bool(re.search(r'\d', inputString))
def getHarvardAuthor(Title):
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
    Temp=res.split('.;')
    Author=[]
    refYear=re.findall("(\d{4})",res)
#check element is it the author name 
    for i in len(Temp):
    #Name length check
        if(len(Temp[i])<=20 and len(Temp[i])>3):
            Author.append((i,refYear[i]))

    return(Author)




