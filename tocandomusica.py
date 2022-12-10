import pygame

pygame.init()
pygame.mixer.music.load("inferno.mp3")
pygame.mixer.music.play()
pygame.event.wait("inferno.mp3")