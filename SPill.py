import pygame
import random
pygame.init()

# Display coden, koden for bakgrunnen
skjerm = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Djevel VS Engler") #tittelen for spillet
skjermbredde = 500 #setter bredden for spillet
surface = pygame.image.load('Bakgrunnen.png').convert() #importer bakgrunnen som jeg lagde i photoshop

#definerer verdier til spilleren    
y = 350 #hvor spilleren spawner y verdi
x = 0 #hvor spilleren spawner x verdi
width = 50 #tykkelsen
height = 50 #høyden
vel = 20 #hvor ført karakteren beveger seg

#jump koden
isJump = False 
JumpCount = 10

#Definerer farger
BLA  = (0, 0, 255, 128)
RØD   = (255, 0, 0)
GRØNN = (0, 255, 0, 128)
SVART = (0, 0, 0)
HVIT = (255, 255, 255)

#Karakteren, loader inn bildene
player = pygame.image.load('djevel.png').convert()

#enemy l
enemyimg = pygame.image.load('engel.png').convert()
enemyX = 450
enemyY = random.randint(300, 340)
enemyX_speed = -10

liv = []  #liste over livet til spilleren
#bakgrunnen samlet under en "funskjon"
def redrawgamewindow():
    skjerm.blit(surface, (0,0))
    skjerm.blit(player, (x, y)) 
    skjerm.blit(enemyimg, (enemyX, enemyY))
    enemyhitbox = (enemyX, enemyY, width, height) #lager hitbox for enemyen
    enemy_rec = pygame.draw.rect(skjerm, (HVIT), enemyhitbox,2)
    playerhitbox = (x, y, width, height) #lager hitbox for spilleren
    player_rec = pygame.draw.rect(skjerm, (RØD), playerhitbox,2) 
    if player_rec.colliderect(enemy_rec): # tegner en rektangel rundt begge figurene og tester om de kolliderer så legger jeg til i listen liv og tester om den stiger i main loopen
        if abs(enemy_rec.top - player_rec.bottom) < 10:
            liv.append(1)
        if abs(enemy_rec.bottom - player_rec.top) < 10:
            liv.append(1)
        if abs(enemy_rec.right - player_rec.left) < 10:
            liv.append(1)
        if abs(enemy_rec.left - player_rec.right) < 10:
            liv.append(1)

nivå = 0

#loopen for spillet, eller såkalt "main loop"
run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          run = False
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > 0: # fikser sånn at figuren ikke klarer å flytte seg igjennom skjermen, derfor definerer jeg en barriere for å holde figuren innenfor et gitt område.
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width: 
        x += vel            
    if not(isJump): #lager en jumpkommando, ved at figuren hopper hver gang jeg trykker på space
        if keys[pygame.K_UP]:
            isJump = True
    else: #Hoppekommandoen sin fysikk, lager en form for tyngdekraft sånn at figuren skal oppføre seg realitstisk når den hopper. 
        if JumpCount >= -10:
            neg = 1
            if JumpCount < 0:
                neg = -1
            y -= (JumpCount **2) *0.5 * neg
            JumpCount -= 1
        else:
            isJump = False
            JumpCount = 10
                
    enemyX += enemyX_speed   
    
    if enemyX <=-50: #hvis enemyen treffer rammen ved x = 0 så vil enemyen spawne tilbake til start, som i pac man, og gå litt raskere hver gang.
        enemyX = 500 
        enemyX_speed *= (1.05)                  #øker farten random med 1.2, dette gjør det vanskeligere for hver runde og må time hoppet mere for å overleve
        nivå += 1
        

        
    if len(liv) > 0: #hvis liv listen når over 1 vil spillet printe ut antall runder du har overlevd og quite spillet
        print("gg du tapte, du overlevde totalt", nivå, "runder")
        pygame.quit()   
    
    redrawgamewindow()       
    
    pygame.display.update()        

pygame.quit()   

                
