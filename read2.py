import PyPDF2
from PyPDF2.pdf import *  # to import function used in origimal `extractText`

# --- functions ---

def myExtractText(self, distance=None):
    # original code from `page.extractText()`
    # https://github.com/mstamy2/PyPDF2/blob/d7b8d3e0f471530267827511cdffaa2ab48bc1ad/PyPDF2/pdf.py#L2645
    
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

                #print('>>>', diff_x, diff_y - y)
                #text += f'| {diff_x}, {diff_y - y} |'
                
                if diff_y > distance or diff_y < 0:  # (bigger margin) or (move to top in next column)
                    text += '\n'
                    #text += '\n' # to add empty line between elements
                    
                prev_x = x
                prev_y = y
            
    return text
        
# --- main ---
        
pdfFileObj = open('0.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

text = ''
for page in pdfReader.pages:
    #text += page.extractText()  # original function
    #text += myExtractText(page)        # modified function (works like original version)
    #text += myExtractText(page, True)  # modified function (add `\n` after every `Tm`)
    text += myExtractText(page, 17)  # modified function (add `\n` only if distance is bigger then `17`)   

# get only text after word `References`
pos = text.lower().find('references')

# only referencers as text
references = text[pos+len('references '):]
print(references)
print('\n------\n')
# doc without references
doc = text[:pos]

# referencers as list
references = references.split('\n')

# remove empty lines and lines which have 2 chars (ie. page number)
references = [item.strip() for item in references if len(item.strip()) > 2]

print('\n--- names ---\n')


data = []

for nubmer, line in enumerate(references, 1): # skip last element with page number
    line = line.strip()
    if line:  # skip empty line
    
        authors_and_year = re.match('((.*)\. (\d{4})\.)', line)
        text, authors, year = authors_and_year.groups()
        #print(text, '|', authors, '|', year)
        
        names = re.split(',[ ]*and |,[ ]*| and ', authors)
        #print(names)
        
        # [(name, last_name), ...]
        names = [(name, name.split(' ')[-1]) for name in names]
        #print(names)
        
        #print(' line:', line)
       
        data.append((authors, names, year))

print('\n--- counting ---\n')

# https://guides.lib.monash.edu/citing-referencing/APA-In-text
# Tapanainen and J/~rvine, 

for authors, names, year in data:
    print('authors:', authors)
    print('   year:', year)
    print('  names:', names)
    print(' et al.:', len(names) > 1)
    print('   and :', len(names) == 2)
    print('---')