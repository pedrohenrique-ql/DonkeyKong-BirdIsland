import pygame
import os

MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]

def load_img(name):
    path = os.path.join(MAIN_DIR ,'../images', name)
    return pygame.image.load(path)

def load_font(name, size):
  path = os.path.join(MAIN_DIR, '../fonts', name)
  return pygame.font.Font(path, size)
