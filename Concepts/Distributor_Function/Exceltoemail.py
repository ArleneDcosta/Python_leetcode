import pyodbc
import win32com.client
import time
import os.path
import win32api
import sys
import os
from PIL import Image, ImageGrab
import img2pdf
import re
from PyPDF2 import PdfFileMerger, PdfFileReader
import pandas as pd
import smtplib

from email.message import EmailMessage
from email.utils import make_msgid

filepath = "E:\\Python\\Concepts\\Distributor_Function\\"
###*##########*###4/4444### Excel Graphs to Images to PDF #################################
xlapp = win32com.client.gencache.EnsureDispatch("Excel.Application")
#filepath where your Excel workbook is saved + the name of the workbook
wb = xlapp.Workbooks.Open(filepath + 'Check.xlsx')
#name of the sheet in which graph is present
ws1 = wb.Worksheets('Graph_1')

#give the cells for which the image/graph is present
win32c = win32com.client.constants
ws1.Range("G6:O20").CopyPicture(Format=win32c.xlBitmap)
img1 = ImageGrab.grabclipboard()
#save the image
img1.save(filepath + 'Graph_1.jpeg',quality=55)

#storing pdf path
pdf_path1 = (filepath + 'Graph_1.pdf' )

#image
image1 = Image.open(filepath + 'Graph_1.jpeg')

#converting into chunks using img2pdf
pdf_bytes1 = img2pdf.convert(image1.filename)

#opening or creating pdf file
file1 = open(pdf_path1, "wb")
#writing pdf files with chunks

file1.write(pdf_bytes1)

#Call the PdfFileMerger
mergedObject = PdfFileMerger()
#Loop through all of the file hem and append their pages
'''for fileNumber in range( 1,5 ):
    mergedObject.append(PdfFileReader(filepath + 'Graph_' + str(fileNumber)+ '.pdf', 'rb'))
'''
mergedObject.append(PdfFileReader(filepath + 'Graph_' + str(1) + '.pdf', 'rb'))
    #Write all the files into a file which is named as shown below
mergedObject.write(filepath + 'All_Graphs_Together.pdf')

# closing image file
image1.close()
#closing pdf file
file1.close()
##closing excel workbook
wb.Close()
xlapp.Quit()

###################### Send Email ######################
'''olMailItem = 0x0
obj = win32com.client.GetActiveObject("Outlook.Application")
newMail = obj.CreateItem(olMailItem)
newMail.Subject = "WEEKLY REPORT"
newMail.To = "arlenedcosta77@gmail.com"
newMail.CC = "Arlene.Dcosta@outlook.com"
newMail.Attachments.Add(filepath + 'All_Graphs_Together.pdf')
newMail.GetInspector
bodystart = re.search("<body.*?>", newMail.HTMLBody)
newMail.HTMLBody = re.sub(bodystart.group(),bodystart.group() + """Good day, 
<br />,
<br />Weekly report has been updated. 
<br /> 
<br /> Please see attached pdf containing graphs. 
<br /> """, newMail.HTMLBody)
newMail.Send()'''



msg = EmailMessage()

asparagus_cid = make_msgid()
msg.set_content('This is a text message')
msg.add_alternative("""\
<html>
  <head></head>
  <body>
    <p>Hello</p>
    <p>
		Here is an example of sending attachments in email using Python.        
    </p>
	<img src="cid:{asparagus_cid}" />
  </body>
</html>
""".format(asparagus_cid=asparagus_cid[1:-1]), subtype='html')

'''with open("sample.jpg", 'rb') as img:
    msg.get_payload()[1].add_related(img.read(), 'image', 'jpeg', cid=asparagus_cid)'''

with open(filepath + 'All_Graphs_Together.pdf', 'rb') as fp:
    pdf_data = fp.read()
    ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    msg.add_attachment(pdf_data, maintype=maintype, subtype=subtype, filename='All_Graphs_Together.pdf')

fromEmail = 'arlenedcosta77@gmail.com'
toEmail = 'arlenedcosta77@gmail.com,dhruvilmody98@gmail.com'

msg['Subject'] = 'HTML message with attachments'
msg['From'] = fromEmail
msg['To'] = toEmail

s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login(fromEmail, 'F@1lower2')
s.send_message(msg)
s.quit()



