#!/usr/bin/env python3

import pdb

import time
import pygame
import pdb
import random
import math
from pygame.locals import *

# Block Dimensions
BWIDTH     = 20
BHEIGHT    = 20
BTHICK = 1



# Table Dimensinos
TABLE_HEIGHT     = 7
UPPER_MARGIN  = 40
TABLE_MARGIN     = 1

# Colors
ORANGE   = (255,0,0)
BLUE     = (0,0,255)
GREEN    = (0,255,0)
GOLD     = (255,125,0)
BLACK    = (255,255,255)
CYAN     = (0,255,255) 
RED      = (255,0,0)
PURPLE   = (122,0,122)


class Block(object):
    """
    Tetris Block
    """    

    def __init__(self, screen, color, size, x, y, rotate):

        self.blobs = []
        for sh in size:
            horiz = sh[0]*BWIDTH + x
            verti = sh[1]*BHEIGHT + y
            block = pygame.Rect(horiz,verti,BWIDTH,BHEIGHT)
            self.blobs.append(block)     

        # Set up variables
        self.rotate = rotate
        self.x = x
        self.y = y
        self.screen = screen
        self.color = color

    def draw(self):
        for bl in self.blobs:
            pygame.draw.rect(self.screen,self.color,bl)
            pygame.draw.rect(self.screen,BLACK,bl,BTHICK)
        



class Tet():

    def __init__(self, size, color, rotates):
        self.color = color
        self.size = size
        self.rotates = rotates
    


class Tetronimos():


    def __init__(self):
        self.cleve = Tet([[0,0],[1,0],[2,0],[0,1]],CYAN,True)
        self.blue = Tet([[0,0],[1,0],[2,0],[2,1]],BLUE,True)
        self.orange = Tet([[-1,0],[0,0],[0,1],[1,1]],GOLD,True)
        self.smash = Tet([[0,0],[0,1],[1,0],[1,1]],ORANGE,False)
        self.hero = Tet([[0,0],[1,0],[2,0],[3,0]],RED,True)
        self.teewee = Tet([[0,0],[1,0],[0,1],[-1,1]],BLUE,True)
        self.teeween = Tet([[0,0],[1,0],[2,0],[1,1]],PURPLE,True)
        self.options = [self.hero, self.teewee, self.blue, self.smash, self.orange, self.teeween, self.smash]

    def get_random(self):
        return self.options[random.randint(0,len(self.options)-1)]


class Tetris(object):

    def __init__(self,bx,by):
        self.new = True
        self.block_data = Tetronimos()
        self.x = TABLE_MARGIN + bx*BWIDTH+2*TABLE_HEIGHT
        self.y = TABLE_MARGIN +by*BHEIGHT+2*TABLE_HEIGHT
        self.up   = pygame.Rect(0,UPPER_MARGIN,self.x,TABLE_HEIGHT)
        self.down  = pygame.Rect(0,self.y-TABLE_HEIGHT,self.x,TABLE_HEIGHT)
        self.left  = pygame.Rect(0,UPPER_MARGIN,TABLE_HEIGHT,self.y)
        self.right = pygame.Rect(self.x-TABLE_HEIGHT,UPPER_MARGIN,TABLE_HEIGHT,self.y)
        self.blk_list    = []
        self.start_x = math.ceil(self.x/2.0)
        self.start_y = UPPER_MARGIN + TABLE_HEIGHT + TABLE_MARGIN
        self.block_data.__init__()
        self.game()

    def new_block(self):
        
        if self.new:
            data = self.block_data.get_random()
            self.current = Block(self.screen, data.color, data.size, self.start_x, self.start_y,data.rotates)
            self.blk_list.append(self.current)
            self.new = False

    
    def play(self):
        while True:
            self.game()

    def game(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.x,self.y))

        self.new_block()
        pygame.display.set_caption('Show Text')
        
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("""Let\'s play Tetris""", True, (0,255,0), (0,0,255))
        textRect = text.get_rect()
        textRect.center = (165, 200)

        
        self.screen.fill(BLACK)

        self.screen.blit(text, textRect)
        
        pygame.display.flip()

        going = True
        while going:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    going = False
            
        running = True
        while running:
            self.screen.fill(BLACK)
            pygame.draw.rect(self.screen,(0,0,255),self.up)
            pygame.draw.rect(self. screen,(0,0,255),self.down)
            pygame.draw.rect(self.screen,(0,0,255),self.left)
            pygame.draw.rect(self.screen,(0,0,255),self.right)

            for blk in self.blk_list:
                blk.draw()
            # Draw the screen buffer
            pygame.display.flip()

            for event in pygame.event.get():
                pass

            print(self.x)
            print(self.y)
            for blk in self.blk_list:
                blk.draw()


            pygame.display.flip()


        pygame.quit()

        self.print_status_line()

if __name__ == "__main__":
    Tetris(16,30).__init__()