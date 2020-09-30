import PyPDF2
#import io
a = PyPDF2.PdfFileReader("gate.pdf", strict=True, warndest=None, overwriteWarnings=True)
#for document info
print(a.documentInfo)
#for total no. of pages
print(a.getNumPages())
str = ""
for i in range(5,10):
    str += a.getPages(i).extractText()

with open("text.txt", "w", encoding='utf-8') as f:
    f.write(str) 
