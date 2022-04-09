import PyPDF2
from PyPDF2.pdf import *  


def myExtractText(self, distance=None):
    
    text = u_("")

    content = self["/Contents"].getObject()

    if not isinstance(content, ContentStream):
        content = ContentStream(content, self.pdf)
    
    prev_x = 0
    prev_y = 0
    
    for operands, operator in content.operations:
        # used only for test to see values in variables
        #print('>>>', operator, operands)

        if operator == b_("Tj"):
            _text = operands[0]
            if isinstance(_text, TextStringObject):
                text += _text
        elif operator == b_("T*"):
            text += "\n"
        elif operator == b_("'"):
            text += "\n"
            _text = operands[0]
            if isinstance(_text, TextStringObject):
                text += operands[0]
        elif operator == b_('"'):
            _text = operands[2]
            if isinstance(_text, TextStringObject):
                text += "\n"
                text += _text
        elif operator == b_("TJ"):
            for i in operands[0]:
                if isinstance(i, TextStringObject):
                    text += i
            text += "\n"
            
        if operator == b_("Tm"):
            
            if distance is True: 
                text += '\n'
                
            elif isinstance(distance, int):
                x = operands[-2]
                y = operands[-1]
               
                diff_x = prev_x - x
                diff_y = prev_y - y

                
                if diff_y > distance or diff_y < 0:
                    text += '\n'
                   
                    
                prev_x = x
                prev_y = y
            
    return text
        
# --- main ---
def getCHICAGOAuthor(Title):
    Title+='.pdf'
    pdfFileObj = open(Title, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    text = ''
    for page in pdfReader.pages:
        text += myExtractText(page, 17)  # modified function (add `\n` only if distance is bigger then `17`)   

# get only text after word `References`
    pos = text.lower().find('references')
    if not (pos):
        pos= text.lower().find('bibliography')

# only referencers as text

    references = text[pos+len('references '):]

# referencers as list
    references = references.split('\n')

# remove empty lines and lines which have 2 chars (ie. page number)
    references = [item.strip() for item in references if len(item.strip()) > 2]

    data = []
    for nubmer, line in enumerate(references, 1): # skip last element with page number
        line = line.strip()
        if line:  # skip empty line
            authors_and_year = re.match('((.*)\. (\d{4})\.)', line)
        text, authors, year = authors_and_year.groups()
        
        names = re.split(',[ ]*and |,[ ]*| and ', authors)
        data.append((authors, names, year))
    Author_Year=[]
    for authors, names, year in data:
        if re.search("et al.",names):
            names.replace("et al.","")
        Author_Year.append((names[-1],year))
    return Author_Year

