import os, random, time, sys
import time
import pygame
import json
import telegram

token = '533153001:AAHs_Sgz-wn46qpKU4E2XbBsCjDBNkZcz28'
initial = True
#bot = telegram.Bot(token=token)
#updates = bot.get_updates()



def sendLogToAll(message):
    #try:
    #    chat_id = bot.get_updates()[-1].message.chat_id
    #    bot.send_message(chat_id=chat_id, text=message)
    #except telegram.TelegramError as mess:
    #    print(mess)
    #    pass
    print('from play_music ' + message)
if __name__ == '__main__':

    folder = './playlist'
    abspath = os.path.abspath(folder)
    mp3s = {}
    while True:
        #print(len(elements) for path, directory, elements in os.walk(abspath))
        #print(len([name for name in os.listdir(folder) if os.path.isfile(name)]))


        #print(len(os.listdir(abspath)))
        if initial==True:
            while len(os.listdir(abspath)) == 0:
                #print('non ho file')
                sendLogToAll('non ho file')
                time.sleep(1)
            #print('attendere 10 secondi')
            sendLogToAll('attendere 10 secondi')
            initial=False
            time.sleep(10)
        #exit()
        #mp3s = set()



        #print(abspath)
        #exit()
        for path, directory, elements in os.walk(abspath):
            #print(element)
            for element in elements:
                if str(path + '/' + element) not in mp3s.keys():
                    mp3s[path + '/' + element] = 0
                    #print(element + ' non risulta gia aggiunto')
                    sendLogToAll(element + ' non risulta gia aggiunto')
                #print()
                #print(i)
                #mp3s.add(path + '/' + i)
            #exit()
        #random.shuffle(mp3s)

        #print(json.dumps(mp3s, indent=4, sort_keys=False))
        sendLogToAll(json.dumps(mp3s, indent=4, sort_keys=False))
        #exit()

        for mp3 in mp3s.keys():
            if mp3s[mp3] != -1:
                try:
                    pygame.mixer.init()
                    #print('carico: ' + mp3)
                    sendLogToAll('carico: ' + mp3)
                    pygame.mixer.music.load(str(mp3))
                    #print('riproduco: ' + mp3 + ' per la ' + str(mp3s[mp3]) + ' volta')
                    sendLogToAll('riproduco: ' + mp3 + ' per la ' + str(mp3s[mp3]) + ' volta')
                    mp3s[mp3] = mp3s[mp3] + 1
                    pygame.mixer.music.play()


                    """
                    while pygame.mixer.music.get_busy() == True:
                        time.sleep(0.2)
                    """
                    #print('aggiornata:::: ' + str(mp3s[mp3]))
                    sendLogToAll('aggiornata:::: ' + str(mp3s[mp3]))
                    time.sleep(3)
                except KeyboardInterrupt:
                    exit(0)
                    pass
                except pygame.error as message:
                    print('doh')
                    print(message)
                    sendLogToAll('non sono riuscito a leggere il file')
                    mp3s[mp3] = -1
                    pass
                finally:
                    pygame.mixer.stop()


        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        #print('fine ciclo')
        sendLogToAll('fine ciclo')
        #print(json.dumps(mp3s, indent=4, sort_keys=False))
        sendLogToAll(json.dumps(mp3s, indent=4, sort_keys=False))
