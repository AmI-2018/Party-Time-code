
from ftplib import FTP
import os
import time

while True:
    # ftp settings
    settings = {
        'ftp': {
            'url': '192.168.2.34',
            'username': 'dietpi',
            'password': 'passwordComplessa',
            'remote-directory': r'/'
        }
    }


    # local paths
    paths = {
        'local-directory': r'playlist/'
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

time.sleep(5)