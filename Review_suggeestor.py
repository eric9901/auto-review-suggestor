from numpy import equal
from email_crawler import getUrl
from email_crawler import getEmail
from Readpdf import getRefAuthor
#input file name
file = input("input pdf file name: ")
#get Author in reference list
Author=getRefAuthor(file)
ReviewerNum=5
#suggested reviewer list
suggest=[]
for i in Author:
    print("Finding "+i+" email.")
    Urls=getUrl(i)
    email=getEmail(Urls)
    if email != '':
        suggest.append('Reviewer: '+i+' Contact email:'+email)
        print(suggest)
    else:
        print(i+'not found.')
    if len(suggest)>ReviewerNum:
        break
print("Here are your reviewer suggestion result:")
for i in suggest:
    print(i)