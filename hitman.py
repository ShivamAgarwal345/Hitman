# HITMAN 

import random, pygame, sys
from pygame.locals import *
pygame.init()
FPS = 4 # frames per second, the general speed of the program
WINDOWWIDTH = 710# size of window's width in pixels
WINDOWHEIGHT = 600 # size of windows' height in pixels
REVEALSPEED = 8 # speed boxes' sliding reveals and covers
BOXSIZE = 40 # size of box height & width in pixels
GAPSIZE = 10 # size of gap between boxes in pixels
BOARDWIDTH = 10 # number of columns of icons
BOARDHEIGHT = 7 # number of rows of icons
assert (BOARDWIDTH * BOARDHEIGHT) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
BGCOLOR = WHITE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE
catImg = pygame.image.load('hitman.jpg')
catImg1 = pygame.image.load('hitman.jpg')
catx=10
caty=10
direction='right'
DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'
FPSCLOCK = pygame.time.Clock()
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, "Board is too big for the number of shapes/colors defined."
exp=pygame.image.load('explosion.jpg')	
gun=pygame.image.load('gun.jpg')
gun1=pygame.image.load('gun1.jpg')
gun2=pygame.image.load('gun2.jpg')	
#FPSCLOCK = pygame.time.Clock()
#DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
mousex = 0 # used to store x coordinate of mouse event
mousey = 0 # used to store y coordinate of mouse event
	
pygame.display.set_caption('Memory Game')
#firstSelection = None # stores the (x, y) of the first box clicked.
#DISPLAYSURF.fill(BGCOLOR)
def main():
	mousex = 0 # used to store x coordinate of mouse event
	mousey = 0 
	catx=10
	caty=10
	while True: # main game loop
		#mouseClicked = False
		
		DISPLAYSURF.fill(BGCOLOR) # drawing the window
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#elif event.type == MOUSEMOTION:
				#mousex, mousey = event.pos
			elif event.type == MOUSEBUTTONUP:
				mousex, mousey = event.pos
		"""if mousex <= 200:
			DISPLAYSURF.blit(gun1,(200,380))
			pygame.display.update()
			FPSCLOCK.tick(FPS)
		elif mousex >= 250:
			DISPLAYSURF.blit(gun2,(200,300))
		else:
			DISPLAYSURF.blit(gun,(200,300))"""				
		#mousex += 62
		#mousey += 40
	        #catx=catx+25
		#caty=caty+25    	
		catx=random.randint(1,600)
	        caty=random.randint(1,400)
		if(catx <= mousex <= catx + 20 and caty <= mousey <= caty + 40):
			drawHighlightBox(catx,caty)
		#print'no'
		i=random.randint(0,2)
		if i == 1 :	
			DISPLAYSURF.blit(catImg1, (catx,caty))
		else :
			DISPLAYSURF.blit(catImg,(catx,caty))
		pygame.display.update()
		FPSCLOCK.tick(FPS)

def drawHighlightBox(mousex, mousey):
	#print 'yes!'
	DISPLAYSURF.blit(exp,(mousex,mousey))
	#ctr++
	#if (ctr==1):
	#	catImg=
	pygame.display.update()
	FPSCLOCK.tick(FPS*2)
	if mousex>=WINDOWWIDTH/2:
		DISPLAYSURF.blit(gun1,(WINDOWWIDTH/2 - 15,WINDOWHEIGHT-30))#DISPLAYSURF.blit(gun1,(mousex,mousey))
	else:
		DISPLAYSURF.blit(gun2,(WINDOWWIDTH/2 - 15,WINDOWHEIGHT-30))#sys.wait(1000)
	
	pygame.display.update()
	FPSCLOCK.tick(FPS)
if __name__ == '__main__':
    main()

