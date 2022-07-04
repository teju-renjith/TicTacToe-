import pygame
import os
import numpy as np
pygame.font.init()
from pygame.locals import *

width=600
height=600
winner=None
draw=None
xo=3 #3 is x 5 is o

displayfont=pygame.font.SysFont('comicsans',40)

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("TIC TAC TOE")
line1=pygame.Rect(200-15/2,0,15,600)
line2=pygame.Rect(400-15/2,0,15,600)
line3=pygame.Rect(0,200-15/2,600,15)
line4=pygame.Rect(0,400-15/2,600,15)
line5=pygame.Rect(-15/2,-15/2,600,15)
line6=pygame.Rect(-15/2,600-15/2,610,15)
line7=pygame.Rect(-15/2,-15/2,15,600)
line8=pygame.Rect(600-15/2,-15/2,15,610)

x_icon=pygame.image.load(os.path.join('TicTacToe','cross.png'))
o_icon=pygame.image.load(os.path.join('TicTacToe','zero.png'))
x_icon=pygame.transform.scale(x_icon,(155,155))
o_icon=pygame.transform.scale(o_icon,(155,155))
board=np.zeros([3,3])

def nextround():
    global draw
    
    if winner is None:
        text=" "
    else:
        if xo==3:
            text="O WON" 
        else:
            text="X WON"

    if draw is True:
        text="GAME DRAW"

    messagefont=pygame.font.SysFont('Open Sans',100)
    output_text = messagefont.render(text, 1, (0, 0, 0))
    box=pygame.Rect(300-output_text.get_width()/2,300-output_text.get_height()/2,output_text.get_width(),output_text.get_height())
    if winner is not None or draw is True:
        pygame.draw.rect(win,(255,141,87),box)
    win.blit(output_text,(300-output_text.get_width()/2,300-output_text.get_height()/2))
    pygame.display.update()


def win_condition():
    global board,winner,draw

    for rows in range(0,3):
        if (board[rows][0]==board[rows][1]==board[rows][2]) and board[rows][0] != 0:
            winner=board[rows][0]
            break
    
    for cols in range(0,3):
        if (board[0][cols]==board[1][cols]==board[2][cols]) and board[0][cols] != 0:
            winner=board[0][cols]
            break

    if (board[0][0]==board[1][1]==board[2][2]) and board[1][1] != 0:
        winner=board[0][0]
    
    if (board[2][0]==board[1][1]==board[0][2]) and board[1][1] != 0:
        winner=board[2][0]

    count=0
    for row in range(0,3):
        for col in range(0,3):
            if board[row][col]!=0 and winner is None:
                count+=1
    if count==9:
        draw=True
    nextround()
    

def draw_OX(r,c):
    global board, xo
    board[r][c]=xo

    if r==0:
        xpos=30-15/2
    elif r==1:
        xpos=width/3+30-15/2
    elif r==2:
        xpos=width*2/3+30-15/2
    else:
        xpos=None

    if c==0:
        ypos=30-15/2
    elif c==1:
        ypos=width/3+30-15/2
    elif c==2:
        ypos=width*2/3+30-15/2
    else:
        ypos=None
  
    if xo==3: 
        win.blit(x_icon,(xpos,ypos))
        pygame.display.update()
        xo=5
    else:
        win.blit(o_icon,(xpos,ypos))
        pygame.display.update()
        xo=3

   
def clicktask():
    x,y=pygame.mouse.get_pos()
    row=-1
    col=-1

    if x<width/3:
        row=0
    elif x>width/3 and x<width*2/3:
        row=1
    else:
        row=2

    if y<height/3:
        col=0
    elif y>height/3 and y<height*2/3:
        col=1
    else:
        col=2

    if (row != -1) and (col != -1) and board[row][col] == 0:
        global xo
        draw_OX(row,col)
        win_condition()

def draw_win():

    win.fill((255,141,87))

    pygame.draw.rect(win,(128,64,0),line1)
    pygame.draw.rect(win,(128,64,0),line2)
    pygame.draw.rect(win,(128,64,0),line3)
    pygame.draw.rect(win,(128,64,0),line4)
    pygame.draw.rect(win,(128,64,0),line5)
    pygame.draw.rect(win,(128,64,0),line6)
    pygame.draw.rect(win,(128,64,0),line7)
    pygame.draw.rect(win,(128,64,0),line8)

    pygame.display.update()

def restart():
    global board, winner, xo, draw
    winner=None
    draw=None
    xo=3
    board=np.zeros([3,3])
    draw_win()
    main()

def main():

    clock=pygame.time.Clock()
    clock.tick(60)
    run=True
    draw_win()

    while run:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run=False
            if event.type == MOUSEBUTTONDOWN:
                clicktask()
                if winner is not None or draw is True:
                    pygame.time.delay(1350)
                    restart()                  
    pygame.quit()

if __name__=="__main__":
    main()