# Функции для воспроизведения звуков

import pygame
pygame.init()

# Удар

def sound_punch():
	pygame.mixer.music.load("sounds/punch.mp3")
	pygame.mixer.music.play()

# Победа

def sound_win():
	pygame.mixer.music.load("sounds/win.mp3")
	pygame.mixer.music.play()