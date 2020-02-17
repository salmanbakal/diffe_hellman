from ftplib import FTP
import os
ftp = FTP('')
ftp.connect('localhost',2121)
ftp.login()
ftp.cwd('C:\Users\Salmaan\Desktop\Server')
ftp.retrlines('LIST')

def uploadFile():
    filename = 'tesla_corps.txt'
    ftp.storbinary('STOR' +filename, open(filename, 'rb'))
    ftp.quit()

def downloadFile():
    filename = 'tesla_corps.txt'
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' +filename, localfile.write, 2121)
    ftp.quit()
    localfile.close()

uploadFile()    
