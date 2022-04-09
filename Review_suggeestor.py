from numpy import equal
from email_crawler import getUrl
from email_crawler import getEmail
from HARVARD_Formate_Reader import getHarvardAuthor
from CHICAGO_Format_Reader import getCHICAGOAuthor
from APA_Format_Reader import getAPAAuthor
import csv
#input file name
file = input("Please input pdf file name: ")
#get Author in reference list
format= input("Please Input Research paper format: A(APA),C(CHICAGO), H(Hazard): ")
limitYear=input("Please input the Year Range: ")
Num = input("Please number of reviewer you want: ")
if format.lower()=='c':
    Author_Year=getCHICAGOAuthor(file)
elif format.lower()=='h':
    Author_Year=getHarvardAuthor(file)
else:
    Author_Year=getAPAAuthor(file)
ReviewerNum=Num
#suggested reviewer list
suggest=[]
for name,Year in Author_Year:
    if(Year>limitYear):
        print("Finding "+name+" email.")
        Urls=getUrl(name)
        email=getEmail(Urls)
        if email != '':
            suggest+=((f"Reviewer: {name}"),(f" Contact email: {email}"))
            print(suggest)
        else:
            print(name+' not found.')
        if len(suggest)>=2*int(ReviewerNum):
            break
print("Here are your reviewer suggestion result:")
for i in suggest:
    print(i)
with open('Reviewer Suggestion.csv', 'w', newline='',encoding='UTF-8') as file:
    writer = csv.writer(file)
    writer.writerow(suggest)
