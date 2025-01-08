import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.SCALED)
pygame.display.set_caption("Game")
textFont = pygame.font.SysFont(None, 50)

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Clock for frame rate
clock = pygame.time.Clock()
FPS = 60

PLAYER_WIDTH, PLAYER_HEIGHT = 100, 70

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
            self.dmg1 = 8
            self.cool1 = 200
            self.attackX1 = [20,40]
            self.attackY1 = [-20,20]
            self.dmg2 = 20
            self.cool2 = 200
            self.attackX2 = [10,45]
            self.attackY2 = [-20,20]
            self.attackTime = [1, 4, 1, 6, 20, 25]
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
            self.dmg1 = 10
            self.cool1 = 300
            self.attackX1 = [-60,60]
            self.attackY1 = [15,20]
            self.dmg2 = 0
            self.cool2 = 200
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime = [1, 6, 6, 10, 30, 330]
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
            self.dmg1 = 0
            self.cool1 = 300
            self.attackX1 = [-800,800]
            self.attackY1 = [-300,300]
            self.dmg2 = 0
            self.cool2 = 150
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime = [20, 30, 30, 180, 30, 150]
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
            self.cool1 = 100
            self.dmg1 = 3
            self.attackX1 = [10,210]
            self.attackY1 = [0,15]
            self.dmg2 = 0
            self.cool2 = 250
            self.attackX2 = [-800,800]
            self.attackY2 = [-300,300]
            self.attackTime = [1, 3, 1, 10, 30, 330]

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
        if self.char == 'hammer' and self.attackTime[2]+1 <= self.skill1 <= self.attackTime[3] and self.skill1 % 3 == 0 and 0 < self.hammer.x < 765:
            self.hammerImg = pygame.transform.rotate(self.hammerImg,self.hammerFace * 90.0)
            self.hammer.x = min(self.hammer.x + self.hammerFace * 15, 765) if self.hammerFace == 1 else max(self.hammer.x + self.hammerFace * 15, 0)
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

        if self.char == 'hammer' and 600 - self.attackTime[5] <= self.skill2_timer <= 600 - self.attackTime[4] and self.skill2_timer % 10 == 0:
            self.lightning[0] = random.random() * 400 + self.rect.center[0] - 200
            if self.isHit(opponent,(-20,20),(-100,100),self.lightning.center):
                opponent.damage(15) 

    def attackHandler(self,opponent):
        if self.attack == 0: 
            self.setImg(1)
        elif self.attack == self.attackTime[0]:
            self.setImg(2)

            if self.isHit(opponent,self.attackX,self.attackY):
                if self.char == 'fighter':
                    pass
                elif self.char == 'shield':
                    pass
                elif self.char == 'hammer':
                    self.addStun(10)
                elif self.char == 'spear' and 600 - self.attackTime[4] >= self.skill2_timer >= 600 - self.attackTime[5]:
                    self.skill2 -= 10
                    opponent.skill2 -= 4
                opponent.damage(self.dmg)
                self.skill2 += 10

        elif self.attack == self.attackTime[1]: 
            self.setImg(0)

    def skill1Handler(self,opponent):
        if self.skill1 == 0: 
            self.setImg(3)
        elif self.skill1 == self.attackTime[2]: 
            self.setImg(4)
            if self.isHit(opponent,self.attackX1,self.attackY1):
                if self.char == 'fighter':
                    self.addJump(10)
                    opponent.addJump(20)
                elif self.char == 'shield':
                    opponent.addStun(30)
                elif self.char == 'hammer':
                    self.hammer.x = self.rect.center[0] - 15 + self.face * 15
                    self.hammer.y = self.rect.center[1] - 25
                    if self.face == -1:
                        self.hammerImg = pygame.transform.flip(self.hammerImg, True, False)
                    self.hammerFace = self.face
                    self.skill2 -= 30
                elif self.char == 'spear':
                    pass
                opponent.damage(self.dmg1)
                self.skill2 += 30

            if self.char == 'spear':
                self.rect.x = min(760, self.rect.x + 200) if self.face == 1 else max(0,self.rect.x - 200)
                self.addStun(10)

        elif self.skill1 == self.attackTime[3]:
            self.setImg(0)

    def skill2Handler(self,opponent):
        if self.skill2_timer == 600:
            self.setImg(5)
                
            if self.char == 'fighter':
                if self.isHit(opponent,self.attackX2,self.attackY2):
                    self.addStun(25)
                    opponent.addStun(120)
                    opponent.rect.x = self.rect.x + self.face * 29
                    opponent.rect.y = self.rect.y - 10
                    opponent.damage(1)
            elif self.char == 'shield':
                self.addStun(30)
            elif self.char == 'hammer':
                pass
            elif self.char == 'spear':
                self.addStun(30)

        elif self.skill2_timer == 600 - self.attackTime[4]:
            self.setImg(6)
            if self.isHit(opponent,self.attackX2,self.attackY2):
                    
                if self.char == 'fighter':
                    opponent.rect.x = WIDTH - 40 if self.face == 1 else 0
                    opponent.damage(self.dmg2)
                elif self.char == 'shield':
                    self.absorb = 4
                elif self.char == 'hammer':
                    self.addStun(60)
                elif self.char == 'spear':
                    self.cool = 5

        elif self.skill2_timer == 600 - self.attackTime[5]:
            self.setImg(0)

            if self.char == 'fighter':
                pass
            elif self.char == 'shield':
                self.absorb = 1
            elif self.char == 'hammer':
                pass
            elif self.char == 'spear':
                self.cool = 20

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
    

# Function to draw players and health bars
def draw():
    global p1,p2
    screen.fill(WHITE)

    # Draw players
    screen.blit(p1.currentImg, (p1.rect.x - 30, p1.rect.y - 15))
    screen.blit(p2.currentImg, (p2.rect.x - 30, p2.rect.y - 15))
    if p1.char == 'shield' and 600 - p1.attackTime[5] <= p1.skill2_timer <= 600 - p1.attackTime[4]: screen.blit(p1.shieldImg, (p1.rect.x, p1.rect.y - 40))
    if p2.char == 'shield' and 600 - p2.attackTime[5] <= p2.skill2_timer <= 600 - p2.attackTime[4]: screen.blit(p2.shieldImg, (p2.rect.x, p2.rect.y - 40))
    if p1.char == 'hammer' and p1.attackTime[2] + 1 <= p1.skill1 <= p1.attackTime[3] and 0 < p1.hammer.x < 765: screen.blit(p1.hammerImg, (p1.hammer.x, p1.hammer.y))
    if p2.char == 'hammer' and p2.attackTime[2] + 1 <= p2.skill1 <= p2.attackTime[3] and 0 < p2.hammer.x < 765: screen.blit(p2.hammerImg, (p2.hammer.x, p2.hammer.y))
    if p1.char == 'hammer' and 600 - p1.attackTime[4] >= p1.skill2_timer >= 600 - p1.attackTime[5] and p1.lightning.x >= 0: screen.blit(p1.lightningImg, p1.lightning)
    if p2.char == 'hammer' and 600 - p2.attackTime[4] >= p2.skill2_timer >= 600 - p2.attackTime[5] and p2.lightning.x >= 0: screen.blit(p2.lightningImg, p2.lightning)
    if p1.char == 'spear' and 600 - p1.attackTime[5] <= p1.skill2_timer <= 600 - p1.attackTime[4]: screen.blit(p1.speedImg, (p1.rect.x, p1.rect.y - 45))
    if p2.char == 'spear' and 600 - p2.attackTime[5] <= p2.skill2_timer <= 600 - p2.attackTime[4]: screen.blit(p2.speedImg, (p2.rect.x, p2.rect.y - 45))

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

def selectChar():
    # Select Character
    global p1,p2
    characters = ['fighter','shield','hammer','spear','fighter','fighter','fighter','fighter']

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

    while True:
        p1_delay -= 1
        p2_delay -= 1
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and p1 > 0 and p1_delay <= 0 and not p1_selected:
            p1 -= 1
            p1_delay = 10
        elif keys[pygame.K_d] and p1 < len(imgs)-1 and p1_delay <= 0 and not p1_selected:
            p1 += 1
            p1_delay = 10
        if keys[pygame.K_LEFT] and p2 > 0 and p2_delay <= 0 and not p2_selected:
            p2 -= 1
            p2_delay = 10
        elif keys[pygame.K_RIGHT] and p2 < len(imgs)-1 and p2_delay <= 0 and not p2_selected:
            p2 += 1
            p2_delay = 10
        if keys[pygame.K_e]:
            p1_selected = True
        if keys[pygame.K_SLASH]:
            p2_selected = True
        if keys[pygame.K_r]:
            p1_selected = False
        if keys[pygame.K_PERIOD]:
            p2_selected = False

        screen.fill(WHITE)
        for i,img in enumerate(imgs):
            screen.blit(img,(10 + 110 * i, 15))
        pygame.draw.rect(screen, GREEN if p1_selected else BLUE, (10 + p1 * 110, 15, 100, 100), 4)
        pygame.draw.rect(screen, GREEN if p2_selected else RED, (14 + p2 * 110, 19, 92, 92), 4)

        pygame.display.flip()

        if p1_selected and p2_selected:
            break
    p1 = Player(characters[p1],1)
    p2 = Player(characters[p2],2)

selectChar()
# Main game loop
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw()
    p1.move()
    p2.move()
    p1.attackUpdate(p2)
    p2.attackUpdate(p1)
    p1.update()
    p2.update()

    if p1.health <= 0 or p2.health <= 0:
        running = False
        winnerText = textFont.render(f"Player {'1' if p1.health > p2.health else '2' if p2.health > p1.health else '1,2'} Wins!", True, BLUE if p1.health >= p2.health else RED)
        screen.blit(winnerText, (270,120))
        pygame.display.flip()
        time.sleep(10)

pygame.quit()