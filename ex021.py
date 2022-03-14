import pygame
pygame.init()

pygame.mixer.music.load('/storage/emulated/0/download/w.mp3')
pygame.mixer.music.play()
pygame.event.wait()