import os
import pygame

def find_game_path():
    paths = (r"D:\Google Drive Backup\Multi-Sync\gui games", r"C:\users\gfreu\Google Drive\Multi-Sync\gui games")
    for path in paths:
        if os.path.exists(path):
            return path

def colors():
	BLACK = (0, 0, 0)
	WHITE = (255, 255, 255)
	BLUE = (0, 0, 255)
	colors = [i for i in [BLACK, WHITE, BLUE]]
	return colors


def screen(path):
	 glogo = os.path.join(path, '_Resources', 'Images', 'G_logo.png')
	 if "D:" in path:
	 	screen_size = (2500,30)
	 elif 'gfreu' in path:
	 	screen_size = (5,5)
	 else:
	 	screen_size = (50,50)
	 return glogo,screen_size

def fonts(f):
	fonts = {i[0]:pygame.font.SysFont(i[1], i[2], bold=True if i[3]=='bold' else False, italic=True if i[4]=='italic' else False) for i in f}
	return fonts
