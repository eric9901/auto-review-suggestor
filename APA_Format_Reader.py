from cgitb import reset
import PyPDF2
import re
import time
def checkNum(inputString):
    return not bool(re.search(r'\d', inputString))
def getAPAAuthor(Title):
    Author_Year=[]
    Title+='.pdf'
    pdfFileObject = open(Title,'rb')
    pdfReaderObject = PyPDF2.PdfFileReader(pdfFileObject,strict=False)
    NumPage=pdfReaderObject.getNumPages()
    res=''
    for k in reversed(range(NumPage)): 
        page=pdfReaderObject.getPage(k)
        PaperText=page.extractText()
    #get Reference List
        txt='References'
        ReferList1=PaperText.partition(txt);
        ReferList2=PaperText.partition(txt.upper());
        if ReferList1[1]:
            res+= ReferList1[2] 
            break;
        if ReferList2[1]:
            res+= ReferList2[2]
        res +=PaperText
    a=re.split("\(\d{4}\)",res)
    refYear=re.findall("\((\d{4})\)",res)
    for i in range(len(a)):
        t=re.search(".*,.\..*",a[i])
        #check and format
        if t:
            if (re.search("and",t.group(0))):
                d=re.split("and",t.group(0))
                Author_Year.append((d[-1],refYear[i]))
                #check etal format
            elif re.search("etal",t.group(0)):
                #if find remove it
                t.group(0).replace('etal','')
                Author_Year.append((t.group(0),refYear[i]))
            else:
                Author_Year.append((t.group(0),refYear[i]))
    return(Author_Year)
