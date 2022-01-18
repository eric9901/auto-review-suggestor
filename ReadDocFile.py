from docx import Document
##type = input ("Input the file type: D(Doc) P(PDF) T(TXT)")
type = input ("Input the file type: D(Doc) P(PDF) ")
Title= input("Input the file name")
if type=='D':
    Title+='.docx'
elif type == 'P':
    Title+='.pdf'
document = Document(Title)
all_paras=document.paragraphs
for para in all_paras:
    print(para.text)

document.save('AfterRead.docx')