from io import StringIO
import docx2txt
import PyPDF2


#Define function to read docx files
def docxextract(file):
  textdoc = []
  #print("HK: Reading txt file",file)
  textdoc = docx2txt.process(file)
  #print("docx hey isbelow:\n",textdoc)
  return textdoc

# Define a function to read pdf files
def pdfextract(file):
  #print("HK: Reading PDF file",file)
  fileReader = PyPDF2.PdfFileReader(open(file,'rb'))
  countpage = fileReader.getNumPages()
  count = 0
  text = []
  while count < countpage:
    pageObj = fileReader.getPage(count)
    count +=1
    t = pageObj.extractText()
    text.append(t)
  return text

def create_profile(file,os):
# Split the extension from the path and normalise it to lowercase.
  ext = os.path.splitext(file)[-1].lower()
# Now we can simply use == to check for equality, no need for wildcards.
  text=[]
  if ext == ".docx":
    text = docxextract(file)
    #print("docx hey isbelow:\n",text)
  elif ext == ".pdf":
    text = pdfextract(file) 
    #print("pdf urrrrrnnnyyy:Below \n",text)

    
  text = str(text)
  text = text.replace("\\n", "")
  text = text.lower()
  return text