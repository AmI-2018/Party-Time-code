from ftplib import FTP
import os

# ftp settings
settings = {
    'ftp': {
        'url': ' 192.168.0.27',
        'username': 'party-time',
        'password': 'party-time',
        'remote-directory': '/'
    }
}

# local paths

paths = {
    'local-directory': r'C:\Users\lucag\Desktop\ftp_server'
}
print(paths['local-directory'])
# list of local files
files = os.listdir(paths['local-directory'])
print(files)

# connect and store
for f in files:
    ftp = FTP(settings['ftp']['url'])
    ftp.login(settings['ftp']['username'], settings['ftp']['password'])
    ftp.cwd(settings['ftp']['remote-directory'])
    ftp.storbinary('STOR ' + f, open(paths['local-directory'] + f, 'rb'))
    ftp.close()
