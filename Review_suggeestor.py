from numpy import equal
from email_crawler import getUrl
from email_crawler import getEmail
from IEEE_Format_Reader import getIEEEfAuthor
from hazard_Format_Reader import getHazardfAuthor
from APA_Format_Reader import getAPAAuthor
#input file name
file = input("Please input pdf file name: ")
#get Author in reference list
limitYear=input("Please input the Year Range: ")
format= input("Please Input Research paper format: I(IEEE), A(APA), H(Hazard): ")
if format.lower()=='i':
    Author_Year=getIEEEfAuthor(file)
elif format.lower()=='h':
    Author_Year=getHazardfAuthor(file)
else:
    Author_Year=getAPAAuthor(file)
ReviewerNum=5
#suggested reviewer list
suggest=[]
print(Author_Year)
for name,Year in Author_Year:
    if(Year>limitYear):
        print("Finding "+name+" email.")
        Urls=getUrl(name)
        email=getEmail(Urls)
        if email != '':
            suggest.append('Reviewer: '+name+' Contact email:'+email)
            print(suggest)
        else:
            print(name+'not found.')
        if len(suggest)>=ReviewerNum:
            break
print("Here are your reviewer suggestion result:")
for i in suggest:
    print(i)