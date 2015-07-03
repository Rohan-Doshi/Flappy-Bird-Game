import pygame,random,sys
from pygame.locals import*

BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(255,0,0)
RED=(255,0,0)
BLUE=(0,0,255)
BROWN=(150,50,0)


winwidth=1366
winheight=768

keys={"player_up":False,"welcome":False,"playerdash":False,"continue":False}

done=True


pygame.init()
size=(winwidth,winheight)
screen=pygame.display.set_mode((size),pygame.FULLSCREEN)
pygame.display.set_caption("Flappy Bird")

back=pygame.image.load("url.png")
back1=pygame.image.load("welc.png")

playerimg=pygame.image.load("player3.png")
player=playerimg.get_rect()
#player.width=player.width-50
#player.height=player.height-10

clock=pygame.time.Clock()


#------------------------------------gameloop--------------------------------
def Gameloop():
    score=0
    temp=0
    player_x=224
    score_ref=player_x
    player_y=100
    pause=False    
    change_up=6
    change_down=3
    
    rect1_x=winwidth
    rect1_y=0
    rect2_x=winwidth
    rect2_y=0
    change_x=6 
    rect_width=70
    rect_height=300	#any value for 1st loop    
    rect_gap=150
    
    change_back=4
    back_x=0
    back_width=back.get_width()
    back_x1=back_width
    back_x2=back_width*2
    back_y=0
    
    while(done):

	
	if back_x1==0:
	    back_x=2*back_width
	elif back_x2==0:
	    back_x1=2*back_width
	elif back_x==0:
	    back_x2=2*back_width
	
	font=pygame.font.Font(None,30)
	text=font.render("Score : %s"%(score),True,BLACK)
	#text1=font.render("TopScore : %s"%(topscore),True,BLACK)
	
        
	for event in pygame.event.get():
	    if(event.type==pygame.KEYDOWN):
		if event.key==K_ESCAPE:
		    pygame.quit()
		    sys.exit()
		    
		elif event.key==K_UP:
		    keys["player_up"]=True
		    
		elif event.key==K_SPACE:
		    keys["playerdash"]=True

		elif event.key==K_1:
			pause=True
		
		elif event.key==K_2:
			pause=False
    
		
		    
	    elif(event.type==pygame.KEYUP):
		    
		if event.key==K_UP:
		    keys["player_up"]=False    
		elif event.key==K_SPACE:
		    keys["playerdash"]=False            
			
	if pause:
		continue;
	
	screen.blit(back,(back_x,back_y))
	screen.blit(back,(back_x1,back_y))
	screen.blit(back,(back_x2,back_y))
	back_x-=change_back
	back_x1-=change_back
	back_x2-=change_back

	player.topleft=(player_x,player_y)
	screen.blit(playerimg,[player_x,player_y])
	
	if keys["player_up"]:
	    player_y-=change_up
	else:
	    player_y+=change_down
	    
	if keys["playerdash"]:
	    rect1_x-=change_x*5
	
	if player_y>(768-60):
	    keys["player_up"]=False
	    break
	if player_y<=(0):
	    player_y=0
	    
	
	    
	#for rectangle
	
	rect1=pygame.draw.rect(screen,BROWN,[rect1_x,rect1_y,rect_width,rect_height-50])
	rect1_a=pygame.draw.rect(screen,BROWN,[rect1_x-10,rect_height-50,90,50])
	rect2=pygame.draw.rect(screen,BROWN,[rect1_x,rect_height+rect_gap+50,rect_width,rect_height+768])
	rect2_a=pygame.draw.rect(screen,BROWN,[rect1_x-10,rect_height+rect_gap,90,50])
	rect1_x-=change_x  
	if(rect1_x<0):
	    rect_height=random.randrange(0,winheight-rect_gap)
	    rect_gap=random.randrange(125,175)
	    rect1_x=winwidth
	    
	    
	#check collision
	if player.colliderect(rect1) or player.colliderect(rect2) or player.colliderect(rect1_a) or player.colliderect(rect2_a):
	    keys["player_up"]=False 
	    break
	
	elif score_ref==rect1_x+rect_width:
	    score+=1
	    temp+=1
	    
	
	    
	#setting level
	if temp>5:
	    change_down+=1
	    change_x+=1
	    change_up+=1
	    score_ref-=1
	    temp=0
	
	    
	screen.blit(text,[10,10])
	
	pygame.display.update()
	clock.tick(50)
	
    
    
    #Game Over
    while(done):
	
	screen.fill(0)
	screen.blit(back1,(180,0))
    
	font=pygame.font.Font(None,60)
	font2=pygame.font.Font(None,30)
	font1=pygame.font.Font(None, 100)
	text1=font1.render("GAME OVER !",True,RED)
	text=font.render("Your Score is : %s"%(score),True,BLUE)
	text2=font2.render("Hit SPACE to continue..",True,BLUE)
	
	    
	for event in pygame.event.get():
	    if(event.type==pygame.KEYDOWN):
		if event.key==K_ESCAPE:
		    pygame.quit()
		    sys.exit()
	    elif event.key==K_SPACE:
		keys["continue"]=True		    
		
	if keys["continue"]:
	    keys["continue"]=False
	    break
    
	screen.blit(text1,[winwidth/3,300])
	screen.blit(text2,[winwidth/2,500])
	screen.blit(text,[500,400])
	pygame.display.update()
#------------------------------------------Gameloop end------------------------------------------




#---------------------------------------Welcome screen-------------------
while(True):
    
    screen.fill(0)
    screen.blit(back1,(180,0))
    font=pygame.font.Font(None,50)
    text=font.render("Press SPACE to Continue..",True,BLUE)
    
   # pygame.display.update()
    screen.blit(text,(winwidth/5,winheight/2))

    for event in pygame.event.get():
	if(event.type==pygame.KEYDOWN):
	    if event.key==K_ESCAPE:
		pygame.quit()
		sys.exit()
	    elif event.key==K_SPACE:
		keys["welcome"]=True

    if keys["welcome"]:
	keys["welcome"]=False
	Gameloop()
	
    pygame.display.update()
#-------------------------------------------------------------------------

pygame.quit()
