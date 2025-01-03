import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

# Select Character
characters = ['fighter','shield','hammer','spear']
properties = [{
        'char' : 'fighter',
        'maxHealth' : 100,
        'speed' : 5,
        'absorb' : 0,
        'dmg' : 3,
        'cool' : 15,
        'attackX' : [25,45],
        'attackY' : [0,20],
        'dmg1' : 10,
        'cool1' : 300,
        'attackX1' : [20,40],
        'attackY1' : [-20,20],
        'dmg2' : 20,
        'cool2' : 200,
        'attackX2' : [10,45],
        'attackY2' : [-20,20],
        'attackTime' : [1, 4, 1, 6, 20, 25],
},
{
        'char' : 'shield',
        'maxHealth' : 100,
        'speed' : 5,
        'absorb' : 1,
        'dmg' : 3,
        'cool' : 50,
        'attackX' : [20,35],
        'attackY' : [-5,20],
        'cool1' : 300,
        'dmg1' : 10,
        'attackX1' : [-60,60],
        'attackY1' : [15,20],
        'dmg2' : 0,
        'cool2' : 200,
        'attackX2' : [-800,800],
        'attackY2' : [-300,300],
        'attackTime' : [1, 6, 6, 10, 30, 330],
},
{
        'char' : 'hammer',
        'maxHealth' : 100,
        'speed' : 3,
        'absorb' : 0,
        'dmg' : 5,
        'cool' : 50,
        'attackX' : [20,35],
        'attackY' : [-20,15],
        'cool1' : 300,
        'dmg1' : 0,
        'attackX1' : [-800,800],
        'attackY1' : [-300,300],
        'dmg2' : 0,
        'cool2' : 150,
        'attackX2' : [-800,800],
        'attackY2' : [-300,300],
        'attackTime' : [20, 30, 30, 180, 30, 150],
},
{
        'char' : 'spear',
        'maxHealth' : 100,
        'speed' : 5,
        'absorb' : 0,
        'dmg' : 2,
        'cool' : 20,
        'attackX' : [20,70],
        'attackY' : [0,15],
        'cool1' : 100,
        'dmg1' : 3,
        'attackX1' : [10,210],
        'attackY1' : [0,15],
        'dmg2' : 0,
        'cool2' : 150,
        'attackX2' : [-800,800],
        'attackY2' : [-300,300],
        'attackTime' : [1, 3, 1, 10, 30, 330],
}]
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

running = True
while running:
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
    
# Initialize player 1
p1_P = properties[p1]
p1 = pygame.Rect(100, HEIGHT - PLAYER_HEIGHT + 30, 40, 40)

p1_health = p1_P['maxHealth']
p1_face = 1
p1_attack = p1_P['cool']
p1_skill1 = p1_P['cool1']
p1_skill2 = 0
p1_skill2_timer = 0
p1_jump = 0
p1_stun = 0

# Initialize player 2
p2_P = properties[p2]
p2 = pygame.Rect(WIDTH - 140, HEIGHT - PLAYER_HEIGHT + 30, 40, 40)

p2_health = p2_P['maxHealth']
p2_face = -1
p2_attack = p2_P['cool']
p2_skill1 = p2_P['cool1']
p2_skill2 = 0
p2_skill2_timer = 0
p2_jump = 0
p2_stun = 0

# Load player images
p1_image1 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}1.png")
p1_image1 = pygame.transform.scale(p1_image1, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image2 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}2.png")
p1_image2 = pygame.transform.scale(p1_image2, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image3 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}3.png")
p1_image3 = pygame.transform.scale(p1_image3, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image4 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}4.png")
p1_image4 = pygame.transform.scale(p1_image4, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image5 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}5.png")
p1_image5 = pygame.transform.scale(p1_image5, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image6 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}6.png")
p1_image6 = pygame.transform.scale(p1_image6, (PLAYER_WIDTH, PLAYER_HEIGHT))
p1_image7 = pygame.image.load(f"src/characters/{p1_P['char']}/{p1_P['char']}7.png")
p1_image7 = pygame.transform.scale(p1_image7, (PLAYER_WIDTH, PLAYER_HEIGHT))

p1_image = p1_image1

p2_image1 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}1.png"), True, False)
p2_image1 = pygame.transform.scale(p2_image1, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image2 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}2.png"), True, False)
p2_image2 = pygame.transform.scale(p2_image2, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image3 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}3.png"), True, False)
p2_image3 = pygame.transform.scale(p2_image3, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image4 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}4.png"), True, False)
p2_image4 = pygame.transform.scale(p2_image4, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image5 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}5.png"), True, False)
p2_image5 = pygame.transform.scale(p2_image5, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image6 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}6.png"), True, False)
p2_image6 = pygame.transform.scale(p2_image6, (PLAYER_WIDTH, PLAYER_HEIGHT))
p2_image7 = pygame.transform.flip(pygame.image.load(f"src/characters/{p2_P['char']}/{p2_P['char']}7.png"), True, False)
p2_image7 = pygame.transform.scale(p2_image7, (PLAYER_WIDTH, PLAYER_HEIGHT))

p2_image = p2_image1

shieldImg = pygame.image.load("src/effects/shield.png")
shieldImg = pygame.transform.scale(shieldImg, (40,40))
speedImg = pygame.image.load("src/effects/attackSpeed.png")
speedImg = pygame.transform.scale(speedImg, (40,40))
hammerImg1 = pygame.image.load("src/characters/hammer/flying_hammer.png")
hammerImg1 = pygame.transform.scale(hammerImg1, (35,35))
hammerImg2 = pygame.transform.flip(hammerImg1,True,False)
lightningImg = pygame.image.load("src/characters/hammer/lightning1.png")
lightningImg = pygame.transform.scale(lightningImg, (40,200))

hammer1 = pygame.Rect(765,0,35,35)
hammer2 = pygame.Rect(765,0,35,35)
hammer1_face = 1
hammer2_face = 1
lightning1 = pygame.Rect(-1,100,40,200)
lightning2 = pygame.Rect(-1,100,40,200)

hitSound1 = pygame.mixer.Sound('src/sound/punch1.mp3')

def damage(p,d):
    global p1_health, p2_health, p1_P, p2_P
    if p == 'p2':
        p2_health -= max(0, d - p2_P['absorb'])
    elif p == 'p1':
        p1_health -= max(0, d - p1_P['absorb'])
    hitSound1.play()

def setImg(p,face = None,img = None):
    global p1_image, p2_image
    if p == 'p1':
        if img:
            if face == -1: img = pygame.transform.flip(img, True, False)
            p1_image = img
        else:
            p1_image = pygame.transform.flip(p1_image, True, False)
    elif p == 'p2':
        if img: 
            if face == 1: img = pygame.transform.flip(img, True, False)
            p2_image = img
        else:
            p2_image = pygame.transform.flip(p2_image, True, False)

def isHit(px,py,ac,ax,ay,af):
    return pygame.Rect(px,py,40,40).colliderect(pygame.Rect(min(ac[0]+af * ax[0], ac[0]+af * ax[1]), ac[1] + ay[0], ax[1] - ax[0], ay[1] - ay[0]))

def stun(p,t):
    global p1_stun, p2_stun, p1_jump, j2_jump
    if p == 'p1':
        p1_stun = max(p1_stun, t)
        p1_jump = 0
    elif p == 'p2':
        p2_stun = max(p2_stun, t)
        p2_jump = 0

def jump(p,n):
    global p1_jump, p2_jump
    if p == 'p1':
        p1_jump = max(n, p1_jump + n)
    elif p == 'p2':
        p2_jump = max(n, p2_jump + n)

# Function to draw players and health bars
def draw():
    screen.fill(WHITE)

    # Draw players
    screen.blit(p1_image, (p1.x - 30, p1.y - 15))
    screen.blit(p2_image, (p2.x - 30, p2.y - 15))
    if p1_P['char'] == 'shield' and 600 - p1_P['attackTime'][5] <= p1_skill2_timer <= 600 - p1_P['attackTime'][4]: screen.blit(shieldImg, (p1.x, p1.y - 40))
    if p2_P['char'] == 'shield' and 600 - p2_P['attackTime'][5] <= p2_skill2_timer <= 600 - p2_P['attackTime'][4]: screen.blit(shieldImg, (p2.x, p2.y - 40))
    if p1_P['char'] == 'hammer' and p1_P['attackTime'][2]+1 <= p1_skill1 <= p1_P['attackTime'][3] and 0 < hammer1.x < 765: screen.blit(hammerImg1, (hammer1.x, hammer1.y))
    if p2_P['char'] == 'hammer' and p2_P['attackTime'][2] + 1 <= p2_skill1 <= p2_P['attackTime'][3] and 0 < hammer2.x < 765: screen.blit(hammerImg2, (hammer2.x, hammer2.y))
    if p1_P['char'] == 'hammer' and 600 - p1_P['attackTime'][4] >= p1_skill2_timer >= 600 - p1_P['attackTime'][5] and lightning1.x >= 0: screen.blit(lightningImg, lightning1)
    if p2_P['char'] == 'hammer' and 600 - p2_P['attackTime'][4] >= p2_skill2_timer >= 600 - p2_P['attackTime'][5] and lightning2.x >= 0: screen.blit(lightningImg, lightning2)
    if p1_P['char'] == 'spear' and 600 - p1_P['attackTime'][5] <= p1_skill2_timer <= 600 - p1_P['attackTime'][4]: screen.blit(speedImg, (p1.x, p1.y - 45))
    if p2_P['char'] == 'spear' and 600 - p2_P['attackTime'][5] <= p2_skill2_timer <= 600 - p2_P['attackTime'][4]: screen.blit(speedImg, (p2.x, p2.y - 45))

    # Draw health bars
    pygame.draw.rect(screen, BLACK, (45, 45, 210, 47))
    pygame.draw.rect(screen, BLACK, (WIDTH - 255, 45, 210, 47))
    pygame.draw.rect(screen, RED, (50, 50, 200/p1_P['maxHealth'] * p1_health, 20))
    pygame.draw.rect(screen, RED, (WIDTH - 250, 50, 200/p2_P['maxHealth'] * p2_health, 20))
    pygame.draw.rect(screen, BLUE, (50, 74, min(247, (200/p1_P['cool1']*p1_skill1)), 5))
    pygame.draw.rect(screen, BLUE, (WIDTH - 250, 74, min(247, (200/p2_P['cool1']*p2_skill1)), 5))
    pygame.draw.rect(screen, GREEN, (50, 83, min(247, (200/p1_P['cool2'] * min(p1_skill2,p1_P['cool2']))), 5))
    pygame.draw.rect(screen, GREEN, (WIDTH - 250, 83, min(247, (200/p2_P['cool2']*min(p2_skill2,p2_P['cool2']))), 5))
    
    # pygame.draw.rect(screen,RED,(lightning1.x,lightning1.y,lightning1.width,lightning1.height))
    # pygame.draw.rect(screen, BLUE, (min(p2.center[0]+p2_face * p2_P['attackX1'][0], p2.center[0]+p2_face * p2_P['attackX1'][1]), p2.center[1] + p2_P['attackY1'][0], p2_P['attackX1'][1] - p2_P['attackX1'][0], p2_P['attackY1'][1] - p2_P['attackY1'][0]))
    # pygame.draw.rect(screen, BLUE, (min(p1.center[0]+p1_face * p1_P['attackX1'][0], p1.center[0]+p1_face * p1_P['attackX1'][1]), p1.center[1] + p1_P['attackY1'][0], p1_P['attackX1'][1] - p1_P['attackX1'][0], p1_P['attackY1'][1] - p1_P['attackY1'][0]))
    # pygame.draw.rect(screen, GREEN, (min(p2.center[0]+p2_face * p2_P['attackX2'][0], p2.center[0]+p2_face * p2_P['attackX2'][1]), p2.center[1] + p2_P['attackY2'][0], p2_P['attackX2'][1] - p2_P['attackX2'][0], p2_P['attackY2'][1] - p2_P['attackY2'][0]))
    # pygame.draw.rect(screen, GREEN, (min(p1.center[0]+p1_face * p1_P['attackX2'][0], p1.center[0]+p1_face * p1_P['attackX2'][1]), p1.center[1] + p1_P['attackY2'][0], p1_P['attackX2'][1] - p1_P['attackX2'][0], p1_P['attackY2'][1] - p1_P['attackY2'][0]))

    pygame.display.flip()

def move():
    global p1_attack,p1_image, p1_face, p1_health, p2_attack, p2_image, p2_face,p2_health,p1_skill1, p1_skill2, p2_skill1, p2_skill2, p1_stun, p2_stun, p1_skill2_timer, p2_skill2_timer
    # Get keys
    keys = pygame.key.get_pressed()

    # Player 1 movement
    if p1_stun == 0:
        if keys[pygame.K_a] and p1.left > 0:
            p1.x -= p1_P['speed']
            if p1_face == 1:
                p1_face = -1
                setImg('p1')
        if keys[pygame.K_d] and p1.right < WIDTH:
            p1.x += p1_P['speed']
            if p1_face == -1:
                p1_face = 1
                setImg('p1')
        if keys[pygame.K_w] and p1.y == 260:
            jump('p1', 15)
        if keys[pygame.K_e] and p1_attack >= p1_P['cool'] and not(p1_P['char'] == 'hammer' and 0 < hammer1.x < 765):
            p1_attack = 0
        if keys[pygame.K_r] and p1_skill1 >= p1_P['cool1']:
            p1_skill1 = 0
        if keys[pygame.K_t] and p1_skill2 >= p1_P['cool2'] and not(p1_P['char'] == 'hammer' and 0 < hammer1.x < 765):
            p1_skill2 = 0
            p1_skill2_timer = 600
    else: p1_stun -= 1

    # Player 2 movement
    if p2_stun == 0:
        if keys[pygame.K_LEFT] and p2.left > 0:
            p2.x -= p2_P['speed']
            if p2_face == 1:
                p2_face = -1
                setImg('p2')
        if keys[pygame.K_RIGHT] and p2.right < WIDTH:
            p2.x += p2_P['speed']
            if p2_face == -1:
                p2_face = 1
                setImg('p2')
        if keys[pygame.K_UP] and p2.y == 260:
            jump('p2',15)
        if keys[pygame.K_SLASH] and p2_attack >= p2_P['cool'] and not(p2_P['char'] == 'hammer' and 0 < hammer2.x < 765):
            p2_attack = 0
        if keys[pygame.K_PERIOD] and p2_skill1 >= p2_P['cool1']:
            p2_skill1 = 0
        if keys[pygame.K_COMMA] and p2_skill2 >= p2_P['cool2'] and not(p2_P['char'] == 'hammer' and 0 < hammer2.x < 765):
            p2_skill2 = 0
            p2_skill2_timer = 600
    else: p2_stun -= 1

def update():
    global p1_image, p1_attack, p2_image, p2_attack, p1_skill1, p1_skill2, p2_skill1, p2_skill2, p1_skill2_timer, p2_skill2_timer, p1_P, p2_P, p1_jump, p2_jump, hammer1, hammer2, hammerImg1, hammerImg2, hammer1_face, hammer2_face

    # p1 attack
    if p1_attack < p1_P['cool']:
        if p1_attack == 0: 
            setImg('p1', p1_face,p1_image2)
        elif p1_attack == p1_P['attackTime'][0]:
            setImg('p1', p1_face,p1_image3)

            if isHit(p2.x, p2.y, p1.center, p1_P['attackX'], p1_P['attackY'], p1_face):
                if p1_P['char'] == 'fighter':
                    pass
                elif p1_P['char'] == 'shield':
                    pass
                elif p1_P['char'] == 'hammer':
                    stun('p2',10)
                elif p1_P['char'] == 'spear' and 600 - p1_P['attackTime'][4] >= p1_skill2_timer >= 600 - p1_P['attackTime'][5]:
                    p1_skill2 -= 10
                damage('p2',p1_P['dmg'])
                p1_skill2 += 10

        elif p1_attack == p1_P['attackTime'][1]: 
            setImg('p1', p1_face,p1_image1)
    p1_attack += 1

    # p1 skill1
    if p1_skill1 < p1_P['cool1']:
        if p1_skill1 == 0: 
            setImg('p1', p1_face,p1_image4)
        elif p1_skill1 == p1_P['attackTime'][2]: 
            setImg('p1', p1_face,p1_image5)
            if isHit(p2.x, p2.y, p1.center, p1_P['attackX1'], p1_P['attackY1'], p1_face):
                if p1_P['char'] == 'fighter':
                    jump('p1', 10)
                    jump('p2', 20)
                elif p1_P['char'] == 'shield':
                    stun('p2',30)
                elif p1_P['char'] == 'hammer':
                    hammer1.x = p1.center[0] - 15 + p1_face * 15
                    hammer1.y = p1.center[1] - 25
                    if p1_face == -1:
                        hammerImg1 = pygame.transform.flip(hammerImg1, True, False)
                    hammer1_face = p1_face
                    p1_skill2 -= 30
                elif p1_P['char'] == 'spear':
                    pass
                damage('p2',p1_P['dmg1'])
                p1_skill2 += 30
            if p1_P['char'] == 'spear':
                p1.x = min(760, p1.x + 200) if p1_face == 1 else max(0,p1.x - 200)
                stun('p1',10)

        elif p1_skill1 == p1_P['attackTime'][3]:
            setImg('p1', p1_face,p1_image1)
        p1_skill1 += 1

    # p1 skill2
    if p1_skill2_timer > 0:
        if p1_skill2_timer == 600:
            setImg('p1', p1_face,p1_image6)

            if p1_P['char'] == 'fighter':
                if isHit(p2.x, p2.y, p1.center, p1_P['attackX2'], p1_P['attackY2'], p1_face):
                    stun('p1', 25)
                    stun('p2', 120)
                    p2.x = p1.x + p1_face * 29
                    p2.y = p1.y - 10
                    damage('p2',1)
            elif p1_P['char'] == 'shield':
                stun('p1', 30)
            elif p1_P['char'] == 'hammer':
                pass
            elif p1_P['char'] == 'spear':
                stun('p1', 30)

        elif p1_skill2_timer == 600 - p1_P['attackTime'][4]:
            setImg('p1', p1_face,p1_image7)

            if isHit(p2.x, p2.y, p1.center, p1_P['attackX2'], p1_P['attackY2'], p1_face):
                if p1_P['char'] == 'fighter':
                    p2.x = WIDTH - 40 if p1_face == 1 else 0
                    damage('p2',p1_P['dmg2'])
                elif p1_P['char'] == 'shield':
                    p1_P['absorb'] = 4
                elif p1_P['char'] == 'hammer':
                    stun('p1',60)
                elif p1_P['char'] == 'spear':
                    p1_P['cool'] = 5

        elif p1_skill2_timer == 600 - p1_P['attackTime'][5]:
            setImg('p1', p1_face,p1_image1)

            if p1_P['char'] == 'fighter':
                pass
            elif p1_P['char'] == 'shield':
                p1_P['absorb'] = 1
            elif p1_P['char'] == 'hammer':
                pass
            elif p1_P['char'] == 'spear':
                p1_P['cool'] = 20

        p1_skill2_timer -= 1

    # p1 hammer 
    if p1_P['char'] == 'hammer' and p1_P['attackTime'][2]+1 <= p1_skill1 <= p1_P['attackTime'][3] and p1_skill1 % 3 == 0 and 0 < hammer1.x < 765:
        hammerImg1 = pygame.transform.rotate(hammerImg1,hammer1_face * 90.0)
        hammer1.x = min(hammer1.x + hammer1_face * 15, 765) if hammer1_face == 1 else max(hammer1.x + hammer1_face * 15, 0)
        if isHit(p2.x,p2.y, hammer1.center, (-17,17), (-17,17),hammer1_face):
            damage('p2', 10)
            p1_skill2 += 30
            hammer1.x = 765
            setImg('p1',p1_face,p1_image1)
        if hammer1.x == 765 or hammer1.x == 0:
            setImg('p1',p1_face,p1_image1)

    #p1 lightning
    if p1_P['char'] == 'hammer' and 600 - p1_P['attackTime'][5] <= p1_skill2_timer <= 600 - p1_P['attackTime'][4] and p1_skill2_timer % 10 == 0:
        lightning1[0] = random.random() * 400 + p1.center[0] - 200
        if isHit(p2.x,p2.y,lightning1.center,(-20,20),(-100,100),1):
            damage('p2', 15) 

    # p2 attack
    if p2_attack < p2_P['cool']:
        if p2_attack == 0:
            setImg('p2', p2_face,p2_image2)
        elif p2_attack == p2_P['attackTime'][0]:
            setImg('p2', p2_face,p2_image3)

            if isHit(p1.x, p1.y, p2.center, p2_P['attackX'], p2_P['attackY'], p2_face):
                damage('p1',p2_P['dmg'])
                if p2_P['char'] == 'fighter':
                    pass
                elif p2_P['char'] == 'shield':
                    pass
                elif p2_P['char'] == 'hammer':
                    stun('p1',10)
                elif p2_P['char'] == 'spear' and 600 - p2_P['attackTime'][4] >= p2_skill2_timer >= 600 - p2_P['attackTime'][5]:
                    p2_skill2 -= 10
                p2_skill2 += 10

        elif p2_attack == p2_P['attackTime'][1]:
            setImg('p2', p2_face,p2_image1)
        p2_attack += 1

    # p2 skill1
    if p2_skill1 < p2_P['cool1']:
        if p2_skill1 == 0:
            setImg('p2', p2_face,p2_image4)
        elif p2_skill1 == p2_P['attackTime'][2]:
            setImg('p2', p2_face,p2_image5)

            if isHit(p1.x, p1.y, p2.center, p2_P['attackX1'], p2_P['attackY1'], p2_face):
                if p2_P['char'] == 'fighter':
                    jump('p2', 10)
                    jump('p1', 20)
                elif p2_P['char'] == 'shield':
                    stun('p1', 30)
                elif p2_P['char'] == 'hammer':
                    hammer2.x = p2.center[0] - 15 + p2_face * 15
                    hammer2.y = p2.center[1] - 25
                    if p2_face == -1:
                        hammerImg2 = pygame.transform.flip(hammerImg2, True, False)
                    hammer2_face = p2_face
                    p2_skill2 -= 30
                damage('p1',p2_P['dmg1'])
                p2_skill2 += 30
            if p2_P['char'] == 'spear':
                p2.x = min(760, p2.x + 200) if p2_face == 1 else max(0,p2.x - 200)
                stun('p2',10)

        elif p2_skill1 == p2_P['attackTime'][3]:
            setImg('p2', p2_face,p2_image1)
        p2_skill1 += 1

    # p2 skill2
    if p2_skill2_timer > 0:
        if p2_skill2_timer == 600:
            setImg('p2', p2_face,p2_image6)

            if isHit(p1.x, p1.y, p2.center, p2_P['attackX2'], p2_P['attackY2'], p2_face):
                if p2_P['char'] == 'fighter':
                    stun('p2', 25)
                    stun('p1', 120)
                    p1.x = p2.x + p2_face * 29
                    p1.y = p2.y - 10
                    damage('p1',1)
                elif p2_P['char'] == 'shield':
                    stun('p2', 30)
                elif p2_P['char'] == 'hammer':
                    pass
                elif p2_P['char'] == 'spear':
                    stun('p2', 30)

        elif p2_skill2_timer == 600 - p2_P['attackTime'][4]:
            setImg('p2', p2_face,p2_image7)

            if isHit(p1.x, p1.y, p2.center, p2_P['attackX2'], p2_P['attackY2'], p2_face):
                if p2_P['char'] == 'fighter':
                    p1.x = WIDTH - 40 if p2_face == 1 else 0
                    damage('p1',p2_P['dmg2'])
                elif p2_P['char'] == 'shield':
                    p2_P['absorb'] = 4
                elif p2_P['char'] =='hammer':
                    stun('p2',60)
                elif p2_P['char'] == 'spear':
                    p2_P['cool'] = 5
                

        elif p2_skill2_timer == 600 - p2_P['attackTime'][5]:
            setImg('p2', p2_face,p2_image1)

            if p2_P['char'] == 'fighter':
                pass
            elif p2_P['char'] == 'shield':
                p2_P['absorb'] = 1
            elif p2_P['char'] == 'spear':
                p2_P['cool'] = 20

        p2_skill2_timer -= 1

    # p2 hammer 
    if p2_P['char'] == 'hammer' and p2_P['attackTime'][2]+1 <= p2_skill1 <= p2_P['attackTime'][3] and p2_skill1 % 3 == 0 and 0 < hammer2.x < 765:
        hammerImg2 = pygame.transform.rotate(hammerImg2,hammer2_face * 90.0)
        hammer2.x = min(hammer2.x + hammer2_face * 15, 765) if hammer2_face == 1 else max(hammer2.x + hammer2_face * 15, 0)
        if isHit(p1.x,p1.y, hammer2.center, (-17,17), (-17,17),hammer2_face):
            damage('p1', 10)
            p2_skill2 += 30
            hammer2.x = 765
            setImg('p2',p2_face,p2_image1)
        if hammer2.x == 765 or hammer2.x == 0:
            setImg('p2',p2_face,p2_image1)

    #p2 lightning
    if p2_P['char'] == 'hammer' and 600 - p2_P['attackTime'][5] <= p2_skill2_timer <= 600 - p2_P['attackTime'][4] and p2_skill2_timer % 10 == 0:
        lightning2[0] = random.random() * 400 + p2.center[0] - 200
        if isHit(p1.x,p1.y,lightning2.center,(-20,20),(-100,100),1):
            damage('p1', 15)
    
    if p1_stun == 0:
        p1.y = min(260 ,p1.y - p1_jump)
        p1_jump -= 1

    if p1_stun == 0:
        p2.y = min(260,p2.y - p2_jump)
        p2_jump -= 1


# Main game loop
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    move()
    update()
    draw()

    if p1_health <= 0 or p2_health <= 0:
        running = False
        winnerText = textFont.render(f"Player {'1' if p1_health > p2_health else '2' if p2_health > p1_health else '1,2'} Wins!", True, BLUE if p1_health >= p2_health else RED)
        screen.blit(winnerText, (270,120))
        pygame.display.flip()
        time.sleep(10)


pygame.quit()