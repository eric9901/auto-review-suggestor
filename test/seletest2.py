import pyautogui
from selenium
import webdriver
import pyperclip
import re
import random
import time
import sys

emailRegex = re.compile(r ''
   '([a - zA - Z0 - 9._ % + -] +  # username @ # @ symbol[a - zA - Z0 - 9. - ] + #domain(\.[a - zA - Z] {
      2,
      4
   })  # Dot and something
)
''
', re.VERBOSE)

# "/home/PYTHON/FOR BLOG/emails.txt"
Change this with path of file to save emails
File1=open("/home/AbhijitKokane/PYTHON/FOR BLOG/emails.txt", "a+")

if len(sys.argv) > 1:
   if sys.argv[1] == 'G':
   B=webdriver.Firefox()
B.get("https://www.google.com/search?q=" + "@gmail.com" + " " + "@yahoo.com" + \
      " " + "@rediffmail.com")  # Add more domains here and you will get more emails
time.sleep(2)
B.maximize_window()

while True:
   pyautogui.click(76, 820);
pyautogui.hotkey('ctrl', 'a');
pyautogui.hotkey('ctrl', 'c')
text=str(pyperclip.paste())

matches=[]

for groups in emailRegex.findall(text):
   matches.append(groups[0])

for x in matches:
   File1.write(" %s \n" % str(x))

# change pause time as per your requirement
time.sleep(random.randint(60, 100))
try:
B.find_element_by_id("pnnext").click()
except:
   exit()

elif sys.argv[1] == 'M':
   text=str(pyperclip.paste())

matches=[]

for groups in emailRegex.findall(text):
   matches.append(groups[0])

for x in matches:
   File1.write(" %s \n" % str(x))
else:
   print("Requires a command line argument")
