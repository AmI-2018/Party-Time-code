import os
import random
import shutil
import re
import time

while True:
    dir = r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist'
    filelist = [f for f in os.listdir(dir) if f.endswith(".m4a")]
    for f in filelist:
        os.remove(os.path.join(dir, f))

    files_pop = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\pop\\'))
    regex = r"(.m4a)"
    pop_people = 3  #here the effective number taken from the DB
    i = 0
    for f in files_pop:
        if i == pop_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_pop)
            f = os.path.join(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\pop\\', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1

    files_rock = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rock\\'))
    regex = r"(.m4a)"
    rock_people = 5  #here the effective number taken from the DB
    i = 0
    for f in files_rock:
        if i == rock_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_rock)
            f = os.path.join(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rock', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1




    files_rb = os.listdir(os.path.dirname(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rb\\'))
    regex = r"(.m4a)"
    rb_people = 2  #here the effective number taken from the DB
    i = 0
    for f in files_rb:
        if i == rb_people:
            break
        if (re.search(regex, f)):
            f = random.choice(files_rb)
            f = os.path.join(r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\music\rb\\', f)
            shutil.copy(f, r'C:\Users\lucag\Desktop\SCUOLA\3° ANNO\ambient intelligence\Party-Time-code\server\playlist')
            i= i+1
    time.sleep(5)