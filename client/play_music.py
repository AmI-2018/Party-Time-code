import os, random, time, sys
import time
import pygame
import json

initial = True
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
                print('non ho file')
                time.sleep(1)
            print('attendere 10 secondi')
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
                    print(element + ' non risulta gia aggiunto')
                #print()
                #print(i)
                #mp3s.add(path + '/' + i)
            #exit()
        #random.shuffle(mp3s)

        print(json.dumps(mp3s, indent=4, sort_keys=False))
        #exit()

        for mp3 in mp3s.keys():
            try:
                pygame.mixer.init()
                print('carico: ' + mp3)
                pygame.mixer.music.load(str(mp3))
                print('riproduco: ' + mp3 + ' per la ' + str(mp3s[mp3]) + ' volta')
                mp3s[mp3] = mp3s[mp3] + 1
                pygame.mixer.music.play()


                """
                while pygame.mixer.music.get_busy() == True:
                    time.sleep(0.2)
                """
                print('aggiornata:::: ' + str(mp3s[mp3]))
                time.sleep(3)
            except KeyboardInterrupt:
                pass
            except pygame.error as message:
                print('doh')
                print(message)
                mp3s[mp3] = -1
                pass
            finally:
                pygame.mixer.stop()


        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print('fine ciclo')
        print(json.dumps(mp3s, indent=4, sort_keys=False))





