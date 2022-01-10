# importing required modules 
import PyPDF2 
    
# creating a pdf file object 
pdfFileObj = open('input.pdf', 'rb') 
    
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
    
# printing number of pages in pdf file 
print(pdfReader.numPages) 
    
# creating a page object 
pageObj = pdfReader.getPage(1) 
    
# extracting text from page 
extracted = pageObj.extractText()
extracted = extracted.replace("Õ", "'")
print(extracted)

# closing the pdf file object 
pdfFileObj.close() 