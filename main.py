from os import pipe
import random # imported for randomness in game
import sys
from typing import Mapping #imported to use exit 
import pygame
from pygame import transform
from pygame.event import get 
from pygame.locals import*

FPS=32
SCREENWIDTH=300
SCREENHEIGHT=568
SCREEN=pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
GROUNDY=(SCREENHEIGHT*0.8)
game_sprites={}
game_sounds={}
player='gallery/sprites/bird.png'
background='gallery/sprites/background.jpg'
PIPE='gallery/sprites/pipe.png'
def welcomescreen():
    messagex=int(SCREENWIDTH/2)
    messagey=int(SCREENHEIGHT/2)
    basex=0
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                return
            else:
                SCREEN.blit(game_sprites['background'],(0 ,0) )
                SCREEN.blit(game_sprites['player'],( playerx,playery) )
                # SCREEN.blit(game_sprites['message'],( messagex,messagey) )
                SCREEN.blit(game_sprites['base'],( 0,400) )

                # SCREEN.blit(game_sprites['over'],(0,0))  
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def gameover():
    messagex=int(SCREENWIDTH/2)
    messagey=int(SCREENHEIGHT/2)
    basex=0
    playerx=int(SCREENWIDTH/5)
    playery=int(SCREENHEIGHT/2)
    while True:
        # for event in pygame.event.get():
        #     if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
        #         pygame.quit()
        #         sys.exit()
                
            # elif event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
            #     return
            # else:
                # SCREEN.blit(game_sprites['background'],(0 ,0) )
                # SCREEN.blit(game_sprites['player'],( playerx,playery) )
                # # SCREEN.blit(game_sprites['message'],( messagex,messagey) )
                # SCREEN.blit(game_sprites['base'],( 0,400) )

            SCREEN.blit(game_sprites['over'],(SCREENWIDTH/3,SCREENHEIGHT/3))  
            pygame.display.update()
            FPSCLOCK.tick(FPS)                
     
def maingame():
        score=0
        basex=0
    # while True:
        playerx=int(SCREENWIDTH/5)
        playery=int(SCREENHEIGHT/2)
        # SCREEN.blit(game_sprites['player']),(SCREENWIDTH/5,SCREENHEIGHT/2)
        # pygame.display.update()
        # SCREEN.blit(game_sprites['background'],(0,0))
        # SCREEN.blit(game_sprites['base'],(0,400))
        newpipe1=getrandompipe()
        newpipe2=getrandompipe()
        upperpipe=[
            {'x':SCREENWIDTH+200,'y':newpipe1[0]['y']},
            {'x':SCREENWIDTH+400+SCREENWIDTH/2,'y':newpipe2[0]['y']}
        ]
        lowerpipe=[
            {'x':SCREENWIDTH+200,'y':newpipe1[1]['y']},
            {'x':SCREENWIDTH+400+SCREENWIDTH/2,'y':newpipe2[1]['y']}
        ]
        pipexvel=-4
        playervely=-9
        playermaxvely=10
        playerminvely=-8
        playeraccy=1
        playerflapaccv=-8
        playerflaped=False

        while True:
            for event in pygame.event.get():
                if event.type==QUIT or (event.type==KEYDOWN and event.key==K_ESCAPE):
                    pygame.exit()
                    sys.exit()
                if event.type==KEYDOWN and (event.key==K_SPACE or event.key==K_UP):
                    if playery>0:
                        playervely=playerflapaccv
                        playerflaped=True
            
            playermid=playerx+(game_sprites['player'].get_width()/2)
            for pipe in upperpipe:
                upperpipemid=pipe['x']+game_sprites['pipe'][0].get_width()/2
                if upperpipemid<=playermid<upperpipemid+4:
                    score+=1
                    print(f"your score is{score}")
            if playervely<playermaxvely:
                playervely+=playeraccy    
            if playerflaped:
                playerflaped=False
            playerheight=game_sprites['player'].get_height()
            playery=playery+min(playervely,400-playery-playerheight)
            for upperpip,lowerpip in zip(upperpipe,lowerpipe):
                upperpip['x']+=pipexvel
                lowerpip['x']+=pipexvel
            if 0<upperpipe[0]['x']<5:
                newpipe=getrandompipe()
                upperpipe.append(newpipe[0])
                lowerpipe.append(newpipe[1])   
            if upperpipe[0]['x'] < -(game_sprites['pipe'][0].get_width())-5:
                upperpipe.pop(0)
                lowerpipe.pop(0)
            # crashtest=iscolide(playerx,playery,upperpipe,lowerpipe)
            # if crashtest==True:
            #     SCREEN.blit(game_sprites['gameover'],(SCREENWIDTH/2,SCREENHEIGHT/2))
            #     return 
            SCREEN.blit(game_sprites['background'],(0,0))
            SCREEN.blit(game_sprites['base'],(basex,400))
            SCREEN.blit(game_sprites['player'],(playerx,playery))
            # SCREEN.blit(game_sprites['over'],(100,150))
            for upperpip,lowerpip in zip(upperpipe,lowerpipe):
                SCREEN.blit(game_sprites['pipe'][0],(upperpip['x'],upperpip['y']))
                SCREEN.blit(game_sprites['pipe'][1],(lowerpip['x'],lowerpip['y']))
            # if iscolide==True:
            crashtest=iscolide(playerx,playery,upperpipe,lowerpipe)
            if crashtest:
                # SCREEN.blit(game_sprites['gameover'],(0,0))
                return True
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)
           

# def iscolides:(iscolide)
#     if iscolide==True:
#         pi=SCREEN.blit()


def iscolide(playerx,playery,upperpipe,lowerpipe):
    pipewidth=game_sprites['pipe'][0].get_width()
    playerwidth=game_sprites['player'].get_width()
    playerheight=game_sprites['player'].get_height()
    pipeheight=game_sprites['pipe'][0].get_height()

    if lowerpipe[0]['x']<=playerx+playerwidth<=lowerpipe[0]['x']+pipewidth and playery+playerheight>=lowerpipe[0]['y']:
        
        return True
        
    elif playery+playerheight==400:
        return True
    elif upperpipe[0]['x']<=playerx+playerwidth<=upperpipe[0]['x']+pipewidth and playery<=upperpipe[0]['y']+pipeheight:    
        return False


def getrandompipe():
    pipehieght=game_sprites['pipe'][0].get_height()
    offset=int(SCREENHEIGHT/3)
    y2=offset+random.randrange(0,int(400-(1.2*offset)))
    pipex=SCREENWIDTH+10
    y1=pipehieght-y2+offset
    pipe=[
        {'x': pipex,'y':-y1},
        {'x': pipex,'y': y2}
    ]
    return pipe

                # SCREEN.blit(game_sprites['over'],(0,0))   


    
    # SCREEN.blit(game_sprites['gameover'],(0,0))




if __name__=="__main__":
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    # pygame.display.pygame.display.set_caption('Flappy bird by Ashwani')
    game_sprites['numbers']=(pygame.image.load('gallery/sprites/0.png').convert_alpha(),
    pygame.image.load('gallery/sprites/1.png').convert_alpha(),
    pygame.image.load('gallery/sprites/2.png').convert_alpha(),
    pygame.image.load('gallery/sprites/3.png').convert_alpha(),
    pygame.image.load('gallery/sprites/4.png').convert_alpha(),
    pygame.image.load('gallery/sprites/5.png').convert_alpha(),
    pygame.image.load('gallery/sprites/6.png').convert_alpha(),
    pygame.image.load('gallery/sprites/7.png').convert_alpha(),
    pygame.image.load('gallery/sprites/8.png').convert_alpha(),
    pygame.image.load('gallery/sprites/9.png').convert_alpha())
    game_sprites['base']=pygame.image.load('gallery/sprites/ground.png').convert_alpha()
    game_sprites['pipe']=(pygame.transform.rotate(pygame.image.load(PIPE),180).convert_alpha(),
    pygame.image.load(PIPE).convert_alpha())
    game_sprites['player']=pygame.image.load('gallery/sprites/bird.png').convert_alpha()
    game_sprites['background']=pygame.image.load('gallery/sprites/background.jpg').convert_alpha()
    game_sprites['message']=pygame.image.load('gallery/sprites/message.png').convert_alpha()
    game_sprites['over']=pygame.image.load('gallery/sprites/over.png').convert_alpha()
    while True:
       welcomescreen()
       
       maingame()
       gameover()
       
       
            #  SCREEN.blit(game_sprites['gameover'],(0,0))
       
       # global SCREEN
    #    gameover()
    #    SCREEN.blit(game_sprites['gameover'],(SCREENWIDTH/2,SCREENHEIGHT/2))

