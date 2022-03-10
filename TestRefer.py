from cgitb import reset
import PyPDF2
import re
import time
def checkNum(inputString):
    return not bool(re.search(r'\d', inputString))
def getRefAuthor(Title):
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
    authors_and_year = re.split('(.*)(\d{4})\.', res)
    if authors_and_year:
        print(authors_and_year)
    else:
        print("Not match")
    year, month, day, hour, min = map(int, time.strftime("%Y %m %d %H %M").split())
    Author=[]
    temp2=''
#check element is it the author name 
    for i in authors_and_year:
    #Name length check for avoid paper title
    #digit check 
        if len(i) == 4 and i.isdigit() and int(i)<=year:
            Author.append(temp2)
        temp2=i
    return(Author)
file = input("input pdf file name: ")
#get Author in reference list
Author=getRefAuthor(file)
print(Author)