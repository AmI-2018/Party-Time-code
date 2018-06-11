from ftplib import FTP
import os
"""
# ftp settings
settings = {
    'ftp': {
        'url': 'ftp.some-server.com',
        'username': 'your-account-name',
        'password': 'your-password',
        'remote-directory': '/path/to/files'
    }
}

# local paths
paths = {
    'local-directory': 'my-files/'
}

# list of local files
files = os.listdir(paths['local-directory'])

# connect and store
for f in files:
    ftp = FTP(settings['ftp']['url'])
    ftp.login(settings['ftp']['username'], settings['ftp']['password'])
    ftp.cwd(settings['ftp']['remote-directory'])
    ftp.storbinary('STOR ' + f, open(paths['local-directory'] + f, 'rb'))
    ftp.close()
"""

import ftplib
#connect to ftp
def ftp_connect():
    while True:
        site_address = "ftp address"
        try:
            with ftplib.FTP(site_address) as ftp:
                ftp.login()
            print(ftp.getwelcome())
            print("current directory", ftp.pwd())  # ftp.pwd return the current directory
            ftp.dir()  # print contents of the directory
            print("valid commands are cd/get/list/exit")
            ftp_command(ftp)
            break  #once ftp_command() exit, end this function
            except ftplib.all_errors as e:
        print("failed to connect check address and credentials.":e)


#take commands from the user
def ftp_command(ftp):
    while True: #run until exit command
        command = input("enter a command")
        commands = command.split()  #split command and file/directory into list

        if command[0] == 'cd' : #change directory
            ftp.cwd(command[1])
            print('directory of', ftp.pwd())
            ftp.dir()
            print('current directory', ftp.pwd)
            except ftplib.error_perm as e:  #handle 550 (not found/no permission errore
            errore_code = str(e).split(None, 1)
        if errore_code[0] == '550':
            print(errore_code[1], 'directory may not exist ore you may not have the permission to view it')
        elif commands[0] == 'get'   #download file
            try:
                ftp.retrbinary('RETR' + commands[1], open(commands[1], 'wb').write)
                print('file succesfully downloaded.')
            except ftplib.error_perm as e:  # handle 550 (not found/no permission errore
                errore_code = str(e).split(None, 1)
                if errore_code[0] == '550':
                    print(errore_code[1], 'file may not exist ore you may not have the permission to view it')
        elif command[0] == 'list':  #print directory listing
            print('directory of', ftp.pwd())
        ftp.dir()
        elif command[0] == 'exit':  #exit application
            ftp.quit()
            print('stop')
            break
    else :
         print('invalid try again')

print('welcome to python ftp')
ftp.connect()
