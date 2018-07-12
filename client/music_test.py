import pygame

brano = '/home/ale-dell/Git/Party-Time-code/client/playlist/sejifh wyeyfw8ey8fy we8 yfaow ong.mp3'

pygame.mixer.init()
pygame.mixer.music.load(brano)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
