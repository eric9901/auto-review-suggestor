from numpy import equal
from email_crawler import getUrl
from email_crawler import getEmail
from Readpdf import getRefAuthor

file = input("input pdf file name: ")
Author=getRefAuthor('solar')
suggest=[]
for i in Author:
    print(i)
    Urls=getUrl(i)
    email=getEmail(Urls)
    if email != '':
        suggest.append('Reviewer: '+i+' Contact email:'+email)
        print(suggest)
    else:
        print(i+'not found.')
