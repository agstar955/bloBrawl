import pygame
import random
import time
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SCALED)
pygame.display.set_caption("Game")
textFont = pygame.font.SysFont(None, 70)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GRAY = (125,125,125)

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 70

background_image = pygame.image.load("src/background.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def menu():
    global running, background_image
    font = pygame.font.SysFont("malgungothic", 20)

    title_text = textFont.render("BloBrawl", True, BLACK)
    start_text = font.render("Start", True, BLACK)
    setting_text = font.render("Setting", True, BLACK)
    quit_text = font.render("Quit", True, BLACK)

    button_width, button_height = 200, 40
    start_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, 120), (button_width, button_height))
    setting_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, 170), (button_width, button_height))
    quit_button_rect = pygame.Rect((WIDTH // 2 - button_width // 2, 220), (button_width, button_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button_rect.collidepoint(event.pos):
                    return
                if setting_button_rect.collidepoint(event.pos):
                    setting()
                elif quit_button_rect.collidepoint(event.pos):
                    running = False
                    return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            return
        if keys[pygame.K_ESCAPE]:
            running = False
            return

        screen.blit(background_image, (0, 0))

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 50))

        pygame.draw.rect(screen, GRAY, start_button_rect)
        pygame.draw.rect(screen, GRAY, setting_button_rect)
        pygame.draw.rect(screen, GRAY, quit_button_rect)

        screen.blit(start_text, (start_button_rect.x + (button_width - start_text.get_width()) // 2, start_button_rect.y + (button_height - start_text.get_height()) // 2))
        screen.blit(setting_text, (setting_button_rect.x + (button_width - setting_text.get_width()) // 2, setting_button_rect.y + (button_height - setting_text.get_height()) // 2))
        screen.blit(quit_text, (quit_button_rect.x + (button_width - quit_text.get_width()) // 2, quit_button_rect.y + (button_height - quit_text.get_height()) // 2))

        pygame.display.flip()

def setting():
    global running, background_image
    font = pygame.font.SysFont("malgungothic", 20)

    exitBtn = pygame.Rect((15, 15), (30, 30))
    exitText = font.render('×',True,BLACK)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exitBtn.collidepoint(event.pos):
                    return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            return



        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen,GRAY,exitBtn)
        screen.blit(exitText,(23,14,10,10))
        pygame.display.flip()

def selectChar():
    # Select Character
    global p1,p2, running, background_image
    font = pygame.font.SysFont("malgungothic", 20)
    characters = ['fighter','shield','hammer','spear','sword','fighter','fighter','fighter','fighter','fighter','fighter','fighter']

    imgs = []

    for i,char in enumerate(characters):
        image = pygame.image.load(f"src/characters/{char}/{char}.png")
        image = pygame.transform.scale(image, (100, 100))
        imgs.append(image)


    p1,p2 = 0,0
    p1_delay = 0
    p2_delay = 0
    p1_selected = False
    p2_selected = False

    exitBtn = pygame.Rect((15, 15), (30, 30))
    exitText = font.render('×',True,BLACK)

    while running:
        p1_delay -= 1
        p2_delay -= 1
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if exitBtn.collidepoint(event.pos):
                    running = False
                    return
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            return
        if keys[pygame.K_a] and p1_delay <= 0 and not p1_selected:
            p1 -= 1
            p1_delay = 10
            if p1 % 6 == 5: p1 += 6
        elif keys[pygame.K_d] and p1_delay <= 0 and not p1_selected:
            p1 += 1
            p1_delay = 10
            if p1 % 6 == 0: p1 -= 6
        if keys[pygame.K_w] and p1_delay <= 0 and not p1_selected:
            p1 -= 6
            p1_delay = 10
            if p1 < 0: p1 = len(characters) + p1
        elif keys[pygame.K_s] and p1_delay <= 0 and not p1_selected:
            p1 += 6
            p1_delay = 10
            if p1 >= len(characters): p1 = p1 - len(characters)
        if keys[pygame.K_LEFT] and p2_delay <= 0 and not p2_selected:
            p2 -= 1
            p2_delay = 10
            if p2 % 6 == 5: p2 += 6
        elif keys[pygame.K_RIGHT] and p2_delay <= 0 and not p2_selected:
            p2 += 1
            p2_delay = 10
            if p2 % 6 == 0: p2 -= 6
        if keys[pygame.K_UP] and p2_delay <= 0 and not p2_selected:
            p2 -= 6
            p2_delay = 10
            if p2 < 0: p2 = len(characters) + p2
        elif keys[pygame.K_DOWN] and p2_delay <= 0 and not p2_selected:
            p2 += 6
            p2_delay = 10
            if p2 >= len(characters): p2 = p2 - len(characters)
        if keys[pygame.K_e]:
            p1_selected = True
        if keys[pygame.K_SLASH]:
            p2_selected = True
        if keys[pygame.K_r]:
            p1_selected = False
        if keys[pygame.K_PERIOD]:
            p2_selected = False

        # screen.fill(WHITE)
        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen,GRAY,exitBtn)
        screen.blit(exitText,(23,14,10,10))
        
        for i,img in enumerate(imgs):
            img = pygame.transform.scale(img,(50,50))
            screen.blit(img,(250 + 50 * (i % 6), 50 + 50 * (i // 6)))
        pygame.draw.rect(screen, GREEN if p1_selected else BLUE, (250 + 50 * (p1 % 6), 50 + 50 * (p1 // 6), 50, 50), 2)
        pygame.draw.rect(screen, GREEN if p2_selected else RED, (252 + 50 * (p2 % 6), 52 + 50 * (p2 // 6), 46, 46), 2)

        screen.blit(imgs[p1],(130,100))
        screen.blit(imgs[p2],(570,100))
        pygame.draw.rect(screen, GREEN if p1_selected else BLUE, (130, 100, 100, 100), 4)
        pygame.draw.rect(screen, GREEN if p2_selected else RED, (570, 100, 100, 100), 4)

        pygame.display.flip()

        if p1_selected and p2_selected:
            break
    p1 = Player(characters[p1],1)
    p2 = Player(characters[p2],2)
    p1.setImg(0)
    p2.setImg(0)
    draw()

# Function to draw players and health bars
def draw():
    global p1,p2,background_image
    # screen.fill(WHITE)
    screen.blit(background_image, (0, 0))

    # Draw players
    screen.blit(p1.currentImg, (p1.rect.x - 30, p1.rect.y - 15))
    screen.blit(p2.currentImg, (p2.rect.x - 30, p2.rect.y - 15))
    # Draw Skills
    p1.skillImgs = list(filter(lambda x:x[3] > 0, p1.skillImgs))
    for i in range(len(p1.skillImgs)): # [img,type,pos,time]
        if type(p1.skillImgs[i][0]) == pygame.surface.Surface:
            if p1.skillImgs[i][1] == 'xy':
                screen.blit(p1.skillImgs[i][0], p1.skillImgs[i][2])
            elif p1.skillImgs[i][1] == 'self':
                screen.blit(p1.skillImgs[i][0], (p1.rect.center[0] - p1.skillImgs[i][0].get_width() // 2 + p1.skillImgs[i][2][0], p1.rect.center[1] - p1.skillImgs[i][0].get_height() // 2 + p1.skillImgs[i][2][1]))
            elif p1.skillImgs[i][1] == 'opponent':
                screen.blit(p1.skillImgs[i][0], (p2.rect.center[0] - p1.skillImgs[i][0].get_width() // 2 + p1.skillImgs[i][2][0], p2.rect.center[1] - p1.skillImgs[i][0].get_height() // 2 + p1.skillImgs[i][2][1]))
        else: # [rect,type,color,time]
            if p1.skillImgs[i][1] == 'xy':
                pygame.draw.rect(screen,p1.skillImgs[i][2],p1.skillImgs[i][0])
            elif p1.skillImgs[i][1] == 'self':
                pygame.draw.rect(screen,p1.skillImgs[i][2],(p1.rect.center[0] - p1.skillImgs[i][0][2] // 2 + p1.skillImgs[i][0][0], p1.rect.center[1] - p1.skillImgs[i][0][3] // 2 + p1.skillImgs[i][0][1], p1.skillImgs[i][0][2], p1.skillImgs[i][0][3]))
            elif p1.skillImgs[i][1] == 'opponent':
                pygame.draw.rect(screen,p1.skillImgs[i][2],(p2.rect.center[0] - p1.skillImgs[i][0][2] // 2 + p1.skillImgs[i][0][0], p2.rect.center[1] - p1.skillImgs[i][0][3] // 2 + p1.skillImgs[i][0][1], p1.skillImgs[i][0][2], p1.skillImgs[i][0][3]))
        p1.skillImgs[i][3] -= 1
    
    p2.skillImgs = list(filter(lambda x:x[3] > 0, p2.skillImgs))
    for i in range(len(p2.skillImgs)): # [img,type,pos,time]
        if type(p2.skillImgs[i][0]) == pygame.surface.Surface:
            if p2.skillImgs[i][1] == 'xy':
                screen.blit(p2.skillImgs[i][0], p2.skillImgs[i][2])
            elif p2.skillImgs[i][1] == 'self':
                screen.blit(p2.skillImgs[i][0], (p2.rect.center[0] - p2.skillImgs[i][0].get_width() // 2 + p2.skillImgs[i][2][0], p2.rect.center[1] - p2.skillImgs[i][0].get_height() // 2 + p2.skillImgs[i][2][1]))
            elif p2.skillImgs[i][1] == 'opponent':
                screen.blit(p2.skillImgs[i][0], (p1.rect.center[0] - p2.skillImgs[i][0].get_width() // 2 + p2.skillImgs[i][2][0], p1.rect.center[1] - p2.skillImgs[i][0].get_height() // 2 + p2.skillImgs[i][2][1]))
        else: # [rect,type,color,time]
            if p2.skillImgs[i][1] == 'xy':
                pygame.draw.rect(screen,p2.skillImgs[i][2],p2.skillImgs[i][0])
            elif p2.skillImgs[i][1] == 'self':
                pygame.draw.rect(screen,p2.skillImgs[i][2],(p2.rect.center[0] - p2.skillImgs[i][0][2] // 2 + p2.skillImgs[i][0][0], p2.rect.center[1] - p2.skillImgs[i][0][3] // 2 + p2.skillImgs[i][0][1], p2.skillImgs[i][0][2], p2.skillImgs[i][0][3]))
            elif p2.skillImgs[i][1] == 'opponent':
                pygame.draw.rect(screen,p2.skillImgs[i][2],(p1.rect.center[0] - p2.skillImgs[i][0][2] // 2 + p2.skillImgs[i][0][0], p1.rect.center[1] - p2.skillImgs[i][0][3] // 2 + p2.skillImgs[i][0][1], p2.skillImgs[i][0][2], p2.skillImgs[i][0][3]))
        p2.skillImgs[i][3] -= 1
    

    # Draw health bars
    pygame.draw.rect(screen, BLACK, (45, 45, 210, 47))
    pygame.draw.rect(screen, BLACK, (WIDTH - 255, 45, 210, 47))
    pygame.draw.rect(screen, RED, (50, 50, 200/p1.maxHealth * p1.health, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 250, 50, 200/p2.maxHealth * p2.health, 20))
    pygame.draw.rect(screen, BLUE, (50, 74, min(247, (200/p1.cool1*p1.skill1)), 5))
    pygame.draw.rect(screen, BLUE, (WIDTH - 250, 74, min(247, (200/p2.cool1*p2.skill1)), 5))
    pygame.draw.rect(screen, GREEN, (50, 83, min(247, (200/p1.cool2 * min(p1.skill2,p1.cool2))), 5))
    pygame.draw.rect(screen, GREEN, (WIDTH - 250, 83, min(247, (200/p2.cool2*min(p2.skill2,p2.cool2))), 5))
    
    pygame.display.flip()

class Player():
    def __init__(self, char, player):
        if char == 'fighter':
            self.char = 'fighter'
            self.maxHealth = 100
            self.speed = 5
            self.jumpPower = 15
            self.absorb = 0
            self.dmg = 3
            self.cool = 15
            self.knockbackPower = 10
            self.attackX = [25,45]
            self.attackY = [0,20]
            self.attackTime = [1,4]
            self.dmg1 = 8
            self.cool1 = 200
            self.attackX1 = [20,40]
            self.attackY1 = [-20,20]
            self.attackTime1 = [1,6]
            self.dmg2 = 20
            self.cool2 = 200
            self.attackX2 = [10,45]
            self.attackY2 = [-20,20]
            self.attackTime2 = [20, 25]
        elif char == 'shield':
            self.char = 'shield'
            self.maxHealth = 100
            self.speed = 5
            self.jumpPower = 15
            self.absorb = 1
            self.dmg = 3
            self.cool = 40
            self.knockbackPower = 10
            self.attackX = [20,35]
            self.attackY = [-5,20]
            self.attackTime = [1,6]
            self.dmg1 = 10
            self.cool1 = 300
            self.attackX1 = [-60,60]
            self.attackY1 = [15,20]
            self.attackTime1 = [6,10]
            self.dmg2 = 0
            self.cool2 = 200
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime2 = [30, 330]
        elif char == 'hammer':
            self.char = 'hammer'
            self.maxHealth = 100
            self.speed = 3
            self.jumpPower = 15
            self.absorb = 0
            self.dmg = 5
            self.cool = 50
            self.knockbackPower = 10
            self.attackX = [20,35]
            self.attackY = [-20,15]
            self.attackTime = [20,30]
            self.dmg1 = 0
            self.cool1 = 300
            self.attackX1 = [-800,800]
            self.attackY1 = [-300,300]
            self.attackTime1 = [30, 180]
            self.dmg2 = 0
            self.cool2 = 150
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime2 = [30, 150]
        elif char == 'spear':
            self.char = 'spear'
            self.maxHealth = 100
            self.speed = 5
            self.jumpPower = 15
            self.absorb = 0
            self.dmg = 2
            self.cool = 20
            self.knockbackPower = 10
            self.attackX = [20,70]
            self.attackY = [0,15]
            self.attackTime = [1,3]
            self.cool1 = 100
            self.dmg1 = 3
            self.attackX1 = [10,210]
            self.attackY1 = [0,15]
            self.attackTime1 = [1,10]
            self.dmg2 = 0
            self.cool2 = 250
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime2 = [30, 330]
        elif char == 'sword':
            self.char = 'sword'
            self.maxHealth = 100
            self.speed = 6
            self.jumpPower = 15
            self.absorb = 0
            self.dmg = 0.5
            self.cool = 40
            self.knockbackPower = 10
            self.attackX = [30,45]
            self.attackY = [-20,20]
            self.attackTime = [10,20]
            self.cool1 = 100
            self.dmg1 = 0.5
            self.attackX1 = [30,45]
            self.attackY1 = [-20,20]
            self.attackTime1 = [5,10,15,20,25,30]
            self.dmg2 = 20
            self.cool2 = 250
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime2 = [10, 60]

        self.rect = pygame.Rect(100 if player == 1 else 660, HEIGHT - PLAYER_HEIGHT + 30, 40, 40)
        self.player = player
        self.health = self.maxHealth
        self.face = 1 if player == 1 else -1
        self.attack = self.cool
        self.skill1 = self.cool1
        self.skill2 = 0
        self.skill2_timer = 0
        self.jump = 0
        self.stun = 0
        self.knockback = 0

        self.skillImgs = []

        self.Imgs = [None] * 8
        for i in range(7):
            self.Imgs[i] = pygame.image.load(f"src/characters/{self.char}/{self.char}{i+1}.png")
            self.Imgs[i] = pygame.transform.scale(self.Imgs[i], (PLAYER_WIDTH, PLAYER_HEIGHT))
        self.currentImg = self.Imgs[0]

        if self.char == 'shield':
            shieldImg = pygame.image.load("src/effects/shield.png")
            self.shieldImg = pygame.transform.scale(shieldImg, (40,40))
        if self.char == 'spear':
            speedImg = pygame.image.load("src/effects/attackSpeed.png")
            self.speedImg = pygame.transform.scale(speedImg, (40,40))
        if self.char == 'hammer':
            hammerImg = pygame.image.load("src/characters/hammer/flying_hammer.png")
            self.hammerImg = pygame.transform.scale(hammerImg, (35,35))
            lightningImg = pygame.image.load("src/characters/hammer/lightning1.png")
            self.lightningImg = pygame.transform.scale(lightningImg, (40,200))

            self.hammer = pygame.Rect(765,0,35,35)
            self.hammerFace = 1
            self.lightning = pygame.Rect(-1,100,40,200)

        self.hitSound = pygame.mixer.Sound('src/sound/punch1.mp3')

    def damage(self,damage):
        self.health -= max(0, damage - self.absorb)
        self.skill2 += 5
        self.hitSound.play()

    def setImg(self,imgNum = None,face = None):
        if imgNum != None:
            img = self.Imgs[imgNum]
            if face: self.face = face
            if self.face == -1: img = pygame.transform.flip(img,True,False)
            self.currentImg = img
        else:
            self.face = -self.face
            self.currentImg = pygame.transform.flip(self.currentImg,True,False)

    def isHit(self,opponent,attackX,attackY,attackCenter = None):
        if not attackCenter: attackCenter = self.rect.center
        attack = pygame.Rect(attackCenter[0] + min(self.face * attackX[0],self.face * attackX[1]), attackCenter[1] + attackY[0], attackX[1] - attackX[0], attackY[1] - attackY[0])
        # pygame.draw.rect(screen,RED,attack)
        # pygame.display.flip()
        return opponent.rect.colliderect(attack)


    def addStun(self,time):
        self.stun = max(self.stun, time)
        self.jump = 0
    
    def addJump(self,n = 0):
        if n == 0: n = self.jumpPower
        self.jump = max(n, self.jump + n)

    def knockback(self,opponent,face): # 미구현
        self.knockback += face * opponent.knockbackPower


    def moveX(self,face,n = 0):
        if n == 0: n = self.speed
        if self.face != face:
            self.setImg()
            self.face = face
        self.rect.x = max(0,self.rect.x - n) if face == -1 else min(WIDTH - 40, self.rect.x + n)
    
    def move(self):
        keys = pygame.key.get_pressed()

        if self.player == 1:
            keyset = [pygame.K_a,pygame.K_d,pygame.K_w,pygame.K_e,pygame.K_r,pygame.K_t]
        else:
            keyset = [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_SLASH,pygame.K_PERIOD,pygame.K_COMMA]
        
        if self.stun <= 0:
            if keys[keyset[0]] and self.rect.left > 0:
                self.moveX(-1)
            if keys[keyset[1]] and self.rect.right < WIDTH:
                self.moveX(1)
            if keys[keyset[2]] and self.rect.y == 260:
                self.addJump()
            if keys[keyset[3]] and self.attack >= self.cool and not(self.char == 'hammer' and 0 < self.hammer.x < 765):
                self.attack = 0
            if keys[keyset[4]] and self.skill1 >= self.cool1:
                self.skill1 = 0
            if keys[keyset[5]] and self.skill2 >= self.cool2 and not(self.char == 'hammer' and 0 < self.hammer.x < 765):
                self.skill2 = 0
                self.skill2_timer = 600

    def hammerHandler(self,opponent):
        if self.char == 'hammer' and self.attackTime1[0]+1 <= self.skill1 <= self.attackTime1[1] and self.skill1 % 3 == 0 and 0 < self.hammer.x < 765:
            self.hammerImg = pygame.transform.rotate(self.hammerImg,self.hammerFace * 90.0)
            self.hammer.x = min(self.hammer.x + self.hammerFace * 15, 765) if self.hammerFace == 1 else max(self.hammer.x + self.hammerFace * 15, 0)
            self.skillImgs.append([self.hammerImg,'xy',(self.hammer.x,self.hammer.y),3])
            if self.isHit(opponent,(-17,17),(-17,17),self.hammer.center):
                opponent.damage(10)
                self.skill2 += 30
                self.hammer.x = 765
                self.setImg(0)
                self.skill1 = self.cool1
            elif self.hammer.x == 765 or self.hammer.x == 0:
                self.setImg(0)
                self.skill1 = self.cool1
            else:
                self.setImg(4)

        if self.char == 'hammer' and 600 - self.attackTime2[1] < self.skill2_timer <= 600 - self.attackTime2[0]:
            self.setImg(6)
            if self.skill2_timer % 10 == 0:
                self.lightning[0] = random.random() * 400 + self.rect.center[0] - 200
                self.skillImgs.append([self.lightningImg,'xy',(self.lightning[0],self.lightning[1]),10])
                if self.isHit(opponent,(-20,20),(-100,100),self.lightning.center):
                    opponent.damage(15)

    def attackHandler(self,opponent):
        if self.char == 'fighter':
            if self.attack == 0: 
                self.setImg(1)
            elif self.attack == self.attackTime[0]:
                self.setImg(2)
                if self.isHit(opponent,self.attackX,self.attackY):
                    opponent.damage(self.dmg)
                    self.skill2 += 10
            elif self.attack == self.attackTime[1]:  
                self.setImg(0)
        
        elif self.char == 'shield':
            if self.attack == 0: 
                self.setImg(1)
            elif self.attack == self.attackTime[0]:
                self.setImg(2)
                if self.isHit(opponent,self.attackX,self.attackY):
                    opponent.damage(self.dmg)
                    self.skill2 += 10
            elif self.attack == self.attackTime[1]: 
                self.setImg(0)
        
        elif self.char == 'hammer':
            if self.attack == 0: 
                self.setImg(1)
            elif self.attack == self.attackTime[0]:
                self.setImg(2)
                if self.isHit(opponent,self.attackX,self.attackY):
                    self.addStun(10)
                    opponent.damage(self.dmg)
                    self.skill2 += 10
            elif self.attack == self.attackTime[1]: 
                self.setImg(0)

        elif self.char == 'spear':
            if self.attack == 0: 
                self.setImg(1)
            elif self.attack == self.attackTime[0]:
                self.setImg(2)
                if self.isHit(opponent,self.attackX,self.attackY):
                    if 600 - self.attackTime2[0] <= self.skill2_timer or self.skill2_timer <= 600 - self.attackTime2[1]:
                        self.skill2 += 10
                    else:
                        opponent.skill2 -= 4
                    opponent.damage(self.dmg)
            elif self.attack == self.attackTime[1]: 
                self.setImg(0)

        elif self.char == 'sword':
            if self.attack == 0: 
                self.setImg(1)
                if self.isHit(opponent,self.attackX,self.attackY):
                    opponent.damage(self.dmg)
                    self.skill2 += 10
                    opponent.skill2 -= 2
            elif self.attack == self.attackTime[0]:
                self.setImg(2)
                if self.isHit(opponent,self.attackX,self.attackY):
                    opponent.damage(self.dmg)
                    self.skill2 += 10
                    opponent.skill2 -= 2
            elif self.attack == self.attackTime[1]: 
                self.setImg(0)

    def skill1Handler(self,opponent):
        if self.char == 'fighter':
            if self.skill1 == 0: 
                self.setImg(3)
            elif self.skill1 == self.attackTime1[0]: 
                self.setImg(4)
                if self.isHit(opponent,self.attackX1,self.attackY1):
                    if self.char == 'fighter':
                        self.addJump(10)
                        opponent.addJump(20)
                        opponent.damage(self.dmg1)
                        self.skill2 += 30
            elif self.skill1 == self.attackTime1[1]:
                self.setImg(0)

        elif self.char == 'shield':
            if self.skill1 == 0: 
                self.setImg(3)
            elif self.skill1 == self.attackTime1[0]: 
                self.setImg(4)
                if self.isHit(opponent,self.attackX1,self.attackY1):
                        opponent.addStun(30)
                        opponent.damage(self.dmg1)
                        self.skill2 += 30
            elif self.skill1 == self.attackTime1[1]:
                self.setImg(0)

        elif self.char == 'hammer':
            if self.skill1 == 0: 
                self.setImg(3)
            elif self.skill1 == self.attackTime1[0]: 
                self.setImg(4)
                self.hammer.x = self.rect.center[0] - 15 + self.face * 15
                self.hammer.y = self.rect.center[1] - 25
                if self.face == -1:
                    self.hammerImg = pygame.transform.flip(self.hammerImg, True, False)
                self.hammerFace = self.face
            elif self.skill1 == self.attackTime1[1]:
                self.setImg(0)

        elif self.char == 'spear':
            if self.skill1 == 0: 
                self.setImg(3)
            elif self.skill1 == self.attackTime1[0]: 
                self.setImg(4)
                if self.isHit(opponent,self.attackX1,self.attackY1):
                    opponent.damage(self.dmg1)
                    self.skill2 += 30
                self.rect.x = min(760, self.rect.x + 200) if self.face == 1 else max(0,self.rect.x - 200)
                self.addStun(10)
            elif self.skill1 == self.attackTime1[1]:
                self.setImg(0)
                
        elif self.char == 'sword':
            if self.skill1 == 0: 
                self.setImg(3)
                if self.isHit(opponent,self.attackX1,self.attackY1):
                    opponent.damage(self.dmg1)
                    self.skill2 += 10
                    opponent.skill2 -= 2
            for i in range(0,6):
                if self.skill1 == self.attackTime1[i]:
                    self.setImg(3 if i%2 == 1 else 4)
                    if self.isHit(opponent,self.attackX1,self.attackY1):
                        opponent.damage(self.dmg1)
                        self.skill2 += 10
                        opponent.skill2 -= 2
                    if i == 5:
                        self.setImg(0)    


    def skill2Handler(self,opponent):
        if self.char == 'fighter':
            if self.skill2_timer == 600:
                self.setImg(5)
                if self.isHit(opponent,self.attackX2,self.attackY2):
                    self.addStun(25)
                    opponent.addStun(120)
                    opponent.rect.x = self.rect.x + self.face * 29
                    opponent.rect.y = self.rect.y - 10
                    opponent.damage(1)
            elif self.skill2_timer == 600 - self.attackTime2[0]:
                self.setImg(6)
                if self.isHit(opponent,self.attackX2,self.attackY2):
                    opponent.rect.x = WIDTH - 40 if self.face == 1 else 0
                    opponent.damage(self.dmg2)
            elif self.skill2_timer == 600 - self.attackTime2[1]:
                self.setImg(0)
        
        elif self.char == 'shield':
            if self.skill2_timer == 600:
                self.setImg(5)
                self.addStun(30)
            elif self.skill2_timer == 600 - self.attackTime2[0]:
                self.setImg(6)
                self.absorb = 4
                self.skillImgs.append([self.shieldImg,'self',(0,-40), self.attackTime2[1] - self.attackTime2[0]])
            elif self.skill2_timer == 600 - self.attackTime2[1]:
                self.setImg(0)
                self.absorb = 1

        elif self.char == 'hammer':
            if self.skill2_timer == 600:
                self.setImg(5)
            elif self.skill2_timer == 600 - self.attackTime2[0]:
                self.setImg(6)
                if self.isHit(opponent,self.attackX2,self.attackY2):
                    self.addStun(120)
            elif self.skill2_timer == 600 - self.attackTime2[1]:
                self.setImg(0)

        elif self.char == 'spear':
            if self.skill2_timer == 600:
                self.setImg(5)
                self.addStun(30)
            elif self.skill2_timer == 600 - self.attackTime2[0]:
                self.setImg(6)
                self.cool = 5
                self.skillImgs.append([self.speedImg,'self',(0,-40), self.attackTime2[1] - self.attackTime2[0]])
            elif self.skill2_timer == 600 - self.attackTime2[1]:
                self.setImg(0)
                self.cool = 20
        
        elif self.char == 'sword':
            if self.skill2_timer == 600:
                self.setImg(5)
                self.addStun(100)
            elif self.skill2_timer == 600 - self.attackTime2[0]:
                self.setImg(6)
            elif self.skill2_timer == 600 - self.attackTime2[1]:
                self.setImg(0)
                self.skillImgs.append([(0, 0, 160, 2),'opponent',WHITE,3])
                opponent.damage(self.dmg2 + opponent.absorb)

    def attackUpdate(self,opponent):
        if self.attack < self.cool:
            self.attackHandler(opponent)
        
        if self.skill1 < self.cool1:
            self.skill1Handler(opponent)
        
        if self.skill2_timer > 0:
            self.skill2Handler(opponent)

        self.hammerHandler(opponent)

    def update(self):
        if self.stun > 0: self.stun -= 1
        if self.attack < self.cool: self.attack += 1
        if self.skill1 < self.cool1: self.skill1 += 1
        if self.skill2_timer > 0: self.skill2_timer -= 1

        if self.stun == 0:
            self.rect.y = min(260 ,self.rect.y - self.jump)
            self.jump -= 1 
    


running = True
# Main game loop
while running:
    menu()
    if not running: break
    selectChar()
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        p1.move()
        p2.move()
        p1.attackUpdate(p2)
        p2.attackUpdate(p1)
        p1.update()
        p2.update()
        draw()

        if p1.health <= 0 or p2.health <= 0:
            running = False
            winnerText = textFont.render(f"Player {'1' if p1.health > p2.health else '2' if p2.health > p1.health else '1,2'} Wins!", True, BLUE if p1.health >= p2.health else RED)
            screen.blit(winnerText, (WIDTH // 2 - winnerText.get_width() // 2,120))
            pygame.display.flip()
            time.sleep(3)
    running = True

pygame.quit()