import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileReader

#for speak function
engine=pyttsx3.init("sapi5")
#sapi5 helps to enhance sppech-text recognition
#get some properties of pyttsx3
voices=engine.getProperty('voices')
engine.getProperty('rate')
engine.getProperty('volume')
#change the rate of reading a/q to you  
# suggestion : put it <150
engine.setProperty('rate', 165)
#this changes the volume level 
engine.setProperty('volume',200 )
engine.setProperty('voices' , voices[0].id)

# speaks out the read pdf
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# reads the pdf
def PDFreader(file_path):
    # Creating a pdf file object.
    pdf = open(file_path, "rb")
    # Creating pdf reader object.
    pdf_reader = PyPDF2.PdfFileReader(pdf)
    
    # getting basic info
    docInfo = pdf_reader.documentInfo
    print(f"Document was created by {docInfo["/creator"]}.")

# Checking total number of pages in a pdf file.
    total_pages = pdf_reader.numPages
    #loop for reading the file from 4th page to last
    for page_no in range(4,total_pages):
        page=pdf_reader.getPage(page_no)
        text=page.extractText()
        print(text)
        speak(text)
    pdf.close()
file_path=input("Enter the full path of file : ")  
if file_path.endswith('.pdf'):
    PDFreader(file_path)

else:
    print("This file type is unsupportable")
    speak("This file type is unsupportable")
