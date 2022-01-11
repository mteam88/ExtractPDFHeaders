#!/usr/bin/env python
import sys
import os
import time
start = time.time()
print("Installing dependencies...")
os.system('pip --disable-pip-version-check install -q pdfminer')
print("Processing...")
from pdfminer.layout import LAParams, LTTextBox
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator

fp = open('input.pdf', 'rb')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
pages = PDFPage.get_pages(fp)
sys.stdout = open('output.txt', 'w')

for page in pages:
    #print('Processing next page...')
    interpreter.process_page(page)
    layout = device.get_result()
    for lobj in layout:
        if isinstance(lobj, LTTextBox):
            x, y, text = lobj.bbox[0], lobj.bbox[3], lobj.get_text()
            if x == 138.0 or x == 162.0 or x == 162.5:
                #print("BING BING BING")
                print('<p><strong>' + text + '</strong></p><p>&nbsp;</p>')
    #input()
sys.stdout.close()
sys.stdout = sys.__stdout__
print("Processing Complete. See output.txt for output.")
end = time.time()
total = end - start
print("Program out in: ", total, " seconds")