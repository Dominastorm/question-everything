'''Reads text from a PDF'''

import codecs
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def PDF_to_text(path,pagenos):
    
    ResourceManager = PDFResourceManager()
    retStr = StringIO()
    laParams = LAParams()
    Device = TextConverter(ResourceManager, retStr, laparams=laParams)
    interpreter = PDFPageInterpreter(ResourceManager, Device)

    file = open(path, "rb")

    #Reading the pages
    for page in PDFPage.get_pages(file, pagenos, maxpages=0, password="",caching=True, check_extractable=True):
        interpreter.process_page(page)

    ReadText = retStr.getvalue()

    file.close()
    Device.close()
    retStr.close()
    
    return ReadText


def ReadPDF(path):
    '''Takes path of PDF as argument and returns the text on it as required by the user'''
    
    Pagenos=[] #Will store the page nos to be read
    
    # print("Enter 0 to read full PDF")
    # print("Enter page numbers separated by a hyphen to read a range (upper bound exclusive)")
    # print("Enter space separated numbers to read specific pages")
    
    # while True:
        
    #     n=input("Enter your choice:")
    #     from pdfminer.pdfpage import PDFPage
    #     if n=="0":
    #         break
        
    #     elif "-" in n and n.replace("-","").isdigit():
    #         Hyphen=map(lambda x:int(x)-1,n.split("-"))
    #         Pagenos=range(*Hyphen)
    #         break
        
    #     elif n.replace(" ","").isdigit():
    #         Pagenos=list(map(lambda x:int(x)-1,n.split()))
    #         break
        
    #     else:
    #         print("Invalid input, try again.")

    Text=PDF_to_text(path,Pagenos)
    FilterText=Text.replace("","")
    return FilterText
