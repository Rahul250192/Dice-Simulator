import pygame, sys, random
pygame.init()
pygame.display.set_caption("Dice Simulator")
size=600
die=size//3
mid=size//2
spot=10
sp=die//4
clearcol= (255,255,255)
scr = pygame.display.set_mode((size,size))
scr.fill((255,255,255))
color = (0,0,0)
pygame.draw.rect(scr,color,(die,die,die,die),5)
mouseclicked = True
def rolling():
	n=random.randint(1,6) 
	scr.fill(clearcol) 							#clearing scene
	pygame.draw.rect(scr,color,(die,die,die,die),5)    #new box
	if n % 2 == 1:
		pygame.draw.circle(scr,color,(mid,mid),spot)  # middle spot
	if n==2 or n==3 or n==4 or n==5 or n==6:
		pygame.draw.circle(scr,color,(mid-sp,mid-sp),spot)  # left top
		pygame.draw.circle(scr,color,(mid+sp,mid+sp),spot)  # right bottom
	if n==4 or n==5 or n==6:
		pygame.draw.circle(scr,color,(mid+sp,mid-sp),spot)  # right top
		pygame.draw.circle(scr,color,(mid-sp,mid+sp),spot)  # left bottom
	if n==6:
		pygame.draw.circle(scr,color,(mid,mid+sp),spot)  # middle bottom
		pygame.draw.circle(scr,color,(mid,mid-sp),spot)  # middle top
	pygame.display.flip()
	
		
while (True):
	if (mouseclicked == True):
		rolling()
		mouseclicked = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
		elif event.type == pygame.MOUSEBUTTONUP:    # if type of event is mouse button up
           ##(mousex,mousey) = event.pos      # co-ordinates of point where mouse is clicked
			mouseclicked = True  