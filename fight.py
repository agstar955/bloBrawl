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

# Select Character
characters = ['fighter','shield','hammer','spear']
properties = [{
        'char' : 'fighter',
        'maxHealth' : 100,
        'speed' : 5,
        'absorb' : 0,
        'dmg' : 3,
        'cool' : 15,
        'knockbackPower' : 10,
        'attackX' : [25,45],
        'attackY' : [0,20],
        'dmg1' : 8,
        'cool1' : 200,
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
        'knockbackPower' : 10,
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
        'knockbackPower' : 10,
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
        'knockbackPower' : 10,
        'attackX' : [20,70],
        'attackY' : [0,15],
        'cool1' : 100,
        'dmg1' : 3,
        'attackX1' : [10,210],
        'attackY1' : [0,15],
        'dmg2' : 0,
        'cool2' : 250,
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
p1 = properties[p1].copy()
p1['rect'] = pygame.Rect(100, HEIGHT - PLAYER_HEIGHT + 30, 40, 40)

p1['health'] = p1['maxHealth']
p1['face'] = 1
p1['attack'] = p1['cool']
p1['skill1'] = p1['cool1']
p1['skill2'] = 0
p1['skill2_timer'] = 0
p1['jump'] = 0
p1['stun'] = 0
p1['knockback'] = 0

# Initialize player 2
p2 = properties[p2].copy()
p2['rect'] = pygame.Rect(WIDTH - 140, HEIGHT - PLAYER_HEIGHT + 30, 40, 40)

p2['health'] = p2['maxHealth']
p2['face'] = -1
p2['attack'] = p2['cool']
p2['skill1'] = p2['cool1']
p2['skill2'] = 0
p2['skill2_timer'] = 0
p2['jump'] = 0
p2['stun'] = 0
p2['knockback'] = 0

# Load player images
p1_imgs = [None] * 8
for i in range(7):
    p1_imgs[i] = pygame.image.load(f"src/characters/{p1['char']}/{p1['char']}{i+1}.png")
    p1_imgs[i] = pygame.transform.scale(p1_imgs[i], (PLAYER_WIDTH, PLAYER_HEIGHT))

p1['image'] = p1_imgs[0]


p2_imgs = [None] * 8
for i in range(7):
    p2_imgs[i] = pygame.image.load(f"src/characters/{p2['char']}/{p2['char']}{i+1}.png")
    p2_imgs[i] = pygame.transform.scale(p2_imgs[i], (PLAYER_WIDTH, PLAYER_HEIGHT))
    p2_imgs[i] = pygame.transform.flip(p2_imgs[i],True,False)

p2['image'] = p2_imgs[0]

if p1['char'] == 'shield' or p2['char'] == 'shield':
    shieldImg = pygame.image.load("src/effects/shield.png")
    shieldImg = pygame.transform.scale(shieldImg, (40,40))
if p1['char'] == 'spear' or p2['char'] == 'spear':
    speedImg = pygame.image.load("src/effects/attackSpeed.png")
    speedImg = pygame.transform.scale(speedImg, (40,40))
if p1['char'] == 'hammer':
    p1['hammerImg'] = pygame.image.load("src/characters/hammer/flying_hammer.png")
    p1['hammerImg'] = pygame.transform.scale(p1['hammerImg'], (35,35))
    lightningImg = pygame.image.load("src/characters/hammer/lightning1.png")
    lightningImg = pygame.transform.scale(lightningImg, (40,200))

    p1['hammer'] = pygame.Rect(765,0,35,35)
    p1['hammerFace'] = 1
    p1['lightning'] = pygame.Rect(-1,100,40,200)
if p2['char'] == 'hammer':
    p2['hammerImg'] = pygame.image.load("src/characters/hammer/flying_hammer.png")
    p2['hammerImg'] = pygame.transform.scale(p2['hammerImg'], (35,35))
    lightningImg = pygame.image.load("src/characters/hammer/lightning1.png")
    lightningImg = pygame.transform.scale(lightningImg, (40,200))

    p2['hammer'] = pygame.Rect(765,0,35,35)
    p2['hammerFace'] = 1
    p2['lightning'] = pygame.Rect(-1,100,40,200)

lightning1 = pygame.Rect(-1,100,40,200)
lightning2 = pygame.Rect(-1,100,40,200)

hitSound1 = pygame.mixer.Sound('src/sound/punch1.mp3')

def damage(p,damage):
    global p1, p2
    if p == 'p2':
        p2['health'] -= max(0, damage - p2['absorb'])
        p2['skill2'] += 5
    elif p == 'p1':
        p1['health'] -= max(0, damage - p1['absorb'])
        p1['skill2'] += 5
    hitSound1.play()

def setImg(p,face = None,img = None):
    global p1,p2
    if p == 'p1':
        if img:
            if face == -1: img = pygame.transform.flip(img, True, False)
            p1['image'] = img
        else:
            p1['image'] = pygame.transform.flip(p1['image'], True, False)
    elif p == 'p2':
        if img: 
            if face == 1: img = pygame.transform.flip(img, True, False)
            p2['image'] = img
        else:
            p2['image'] = pygame.transform.flip(p2['image'], True, False)

def isHit(px,py,ac,ax,ay,af):
    return pygame.Rect(px,py,40,40).colliderect(pygame.Rect(min(ac[0]+af * ax[0], ac[0]+af * ax[1]), ac[1] + ay[0], ax[1] - ax[0], ay[1] - ay[0]))

def stun(p,t):
    global p1, p2
    if p == 'p1':
        p1['stun'] = max(p1['stun'], t)
        p1['jump'] = 0
    elif p == 'p2':
        p2['stun'] = max(p2['stun'], t)
        p2['jump'] = 0

def jump(p,n):
    global p1, p2
    if p == 'p1':
        p1['jump'] = max(n, p1['jump'] + n)
    elif p == 'p2':
        p2['jump'] = max(n, p2['jump'] + n)

def knockback(p,d): # 미구현
    global p1, p2
    if p == 'p1':
        p1['knockback'] += d * p1['knockbackPower']
    elif p == 'p2':
        p2['knockback'] += d * p2['knockbackPower']

# def handleCharacterAttack(character, opponent):
#     if character == 'fighter':
#         pass
#     elif character == 'shield':
#         pass
#     elif character == 'hammer':
#         pass
#     elif character == 'spear':
    
    

# Function to draw players and health bars
def draw():
    screen.fill(WHITE)

    # Draw players
    screen.blit(p1['image'], (p1['rect'].x - 30, p1['rect'].y - 15))
    screen.blit(p2['image'], (p2['rect'].x - 30, p2['rect'].y - 15))
    if p1['char'] == 'shield' and 600 - p1['attackTime'][5] <= p1['skill2_timer'] <= 600 - p1['attackTime'][4]: screen.blit(shieldImg, (p1['rect'].x, p1['rect'].y - 40))
    if p2['char'] == 'shield' and 600 - p2['attackTime'][5] <= p2['skill2_timer'] <= 600 - p2['attackTime'][4]: screen.blit(shieldImg, (p2['rect'].x, p2['rect'].y - 40))
    if p1['char'] == 'hammer' and p1['attackTime'][2]+1 <= p1['skill1'] <= p1['attackTime'][3] and 0 < p1['hammer'].x < 765: screen.blit(p1['hammerImg'], (p1['hammer'].x, p1['hammer'].y))
    if p2['char'] == 'hammer' and p2['attackTime'][2] + 1 <= p2['skill1'] <= p2['attackTime'][3] and 0 < p2['hammer'].x < 765: screen.blit(p2['hammerImg'], (p2['hammer'].x, p2['hammer'].y))
    if p1['char'] == 'hammer' and 600 - p1['attackTime'][4] >= p1['skill2_timer'] >= 600 - p1['attackTime'][5] and lightning1.x >= 0: screen.blit(lightningImg, lightning1)
    if p2['char'] == 'hammer' and 600 - p2['attackTime'][4] >= p2['skill2_timer'] >= 600 - p2['attackTime'][5] and lightning2.x >= 0: screen.blit(lightningImg, lightning2)
    if p1['char'] == 'spear' and 600 - p1['attackTime'][5] <= p1['skill2_timer'] <= 600 - p1['attackTime'][4]: screen.blit(speedImg, (p1['rect'].x, p1['rect'].y - 45))
    if p2['char'] == 'spear' and 600 - p2['attackTime'][5] <= p2['skill2_timer'] <= 600 - p2['attackTime'][4]: screen.blit(speedImg, (p2['rect'].x, p2['rect'].y - 45))

    # Draw health bars
    pygame.draw.rect(screen, BLACK, (45, 45, 210, 47))
    pygame.draw.rect(screen, BLACK, (WIDTH - 255, 45, 210, 47))
    pygame.draw.rect(screen, RED, (50, 50, 200/p1['maxHealth'] * p1['health'], 20))
    pygame.draw.rect(screen, RED, (WIDTH - 250, 50, 200/p2['maxHealth'] * p2['health'], 20))
    pygame.draw.rect(screen, BLUE, (50, 74, min(247, (200/p1['cool1']*p1['skill1'])), 5))
    pygame.draw.rect(screen, BLUE, (WIDTH - 250, 74, min(247, (200/p2['cool1']*p2['skill1'])), 5))
    pygame.draw.rect(screen, GREEN, (50, 83, min(247, (200/p1['cool2'] * min(p1['skill2'],p1['cool2']))), 5))
    pygame.draw.rect(screen, GREEN, (WIDTH - 250, 83, min(247, (200/p2['cool2']*min(p2['skill2'],p2['cool2']))), 5))
    
    # pygame.draw.rect(screen,RED,(lightning1.x,lightning1.y,lightning1.width,lightning1.height))
    # pygame.draw.rect(screen, BLUE, (min(p2['rect'].center[0]+p2['face'] * p2['attackX1'][0], p2['rect'].center[0]+p2['face'] * p2['attackX1'][1]), p2['rect'].center[1] + p2['attackY1'][0], p2['attackX1'][1] - p2['attackX1'][0], p2['attackY1'][1] - p2['attackY1'][0]))
    # pygame.draw.rect(screen, BLUE, (min(p1['rect'].center[0]+p1_face * p1['attackX1'][0], p1['rect'].center[0]+p1_face * p1['attackX1'][1]), p1['rect'].center[1] + p1['attackY1'][0], p1['attackX1'][1] - p1['attackX1'][0], p1['attackY1'][1] - p1['attackY1'][0]))
    # pygame.draw.rect(screen, GREEN, (min(p2['rect'].center[0]+p2['face'] * p2['attackX2'][0], p2['rect'].center[0]+p2['face'] * p2['attackX2'][1]), p2['rect'].center[1] + p2['attackY2'][0], p2['attackX2'][1] - p2['attackX2'][0], p2['attackY2'][1] - p2['attackY2'][0]))
    # pygame.draw.rect(screen, GREEN, (min(p1['rect'].center[0]+p1_face * p1['attackX2'][0], p1['rect'].center[0]+p1_face * p1['attackX2'][1]), p1['rect'].center[1] + p1['attackY2'][0], p1['attackX2'][1] - p1['attackX2'][0], p1['attackY2'][1] - p1['attackY2'][0]))

    pygame.display.flip()

def move():
    global p1,p2
    # Get keys
    keys = pygame.key.get_pressed()

    # Player 1 movement
    if p1['stun'] == 0:
        if keys[pygame.K_a] and p1['rect'].left > 0:
            p1['rect'].x -= p1['speed']
            if p1['face'] == 1:
                p1['face'] = -1
                setImg('p1')
        if keys[pygame.K_d] and p1['rect'].right < WIDTH:
            p1['rect'].x += p1['speed']
            if p1['face'] == -1:
                p1['face'] = 1
                setImg('p1')
        if keys[pygame.K_w] and p1['rect'].y == 260:
            jump('p1', 15)
        if keys[pygame.K_e] and p1['attack'] >= p1['cool'] and not(p1['char'] == 'hammer' and 0 < p1['hammer'].x < 765):
            p1['attack'] = 0
        if keys[pygame.K_r] and p1['skill1'] >= p1['cool1']:
            p1['skill1'] = 0
        if keys[pygame.K_t] and p1['skill2'] >= p1['cool2'] and not(p1['char'] == 'hammer' and 0 < p1['hammer'].x < 765):
            p1['skill2'] = 0
            p1['skill2_timer'] = 600
    else: p1['stun'] -= 1

    # Player 2 movement
    if p2['stun'] == 0:
        if keys[pygame.K_LEFT] and p2['rect'].left > 0:
            p2['rect'].x -= p2['speed']
            if p2['face'] == 1:
                p2['face'] = -1
                setImg('p2')
        if keys[pygame.K_RIGHT] and p2['rect'].right < WIDTH:
            p2['rect'].x += p2['speed']
            if p2['face'] == -1:
                p2['face'] = 1
                setImg('p2')
        if keys[pygame.K_UP] and p2['rect'].y == 260:
            jump('p2',15)
        if keys[pygame.K_SLASH] and p2['attack'] >= p2['cool'] and not(p2['char'] == 'hammer' and 0 < p2['hammer'].x < 765):
            p2['attack'] = 0
        if keys[pygame.K_PERIOD] and p2['skill1'] >= p2['cool1']:
            p2['skill1'] = 0
        if keys[pygame.K_COMMA] and p2['skill2'] >= p2['cool2'] and not(p2['char'] == 'hammer' and 0 < p2['hammer'].x < 765):
            p2['skill2'] = 0
            p2['skill2_timer'] = 600
    else: p2['stun'] -= 1

def update():
    global p1, p2

    # p1 attack
    if p1['attack'] < p1['cool']:
        if p1['attack'] == 0: 
            setImg('p1', p1['face'],p1_imgs[1])
        elif p1['attack'] == p1['attackTime'][0]:
            setImg('p1', p1['face'],p1_imgs[2])

            if isHit(p2['rect'].x, p2['rect'].y, p1['rect'].center, p1['attackX'], p1['attackY'], p1['face']):
                if p1['char'] == 'fighter':
                    pass
                elif p1['char'] == 'shield':
                    pass
                elif p1['char'] == 'hammer':
                    stun('p2',10)
                elif p1['char'] == 'spear' and 600 - p1['attackTime'][4] >= p1['skill2_timer'] >= 600 - p1['attackTime'][5]:
                    p1['skill2'] -= 10
                    p2['skill2'] -= 4
                damage('p2',p1['dmg'])
                p1['skill2'] += 10

        elif p1['attack'] == p1['attackTime'][1]: 
            setImg('p1', p1['face'],p1_imgs[0])
    p1['attack'] += 1

    # p1 skill1
    if p1['skill1'] < p1['cool1']:
        if p1['skill1'] == 0: 
            setImg('p1', p1['face'],p1_imgs[3])
        elif p1['skill1'] == p1['attackTime'][2]: 
            setImg('p1', p1['face'],p1_imgs[4])
            if isHit(p2['rect'].x, p2['rect'].y, p1['rect'].center, p1['attackX1'], p1['attackY1'], p1['face']):
                if p1['char'] == 'fighter':
                    jump('p1', 10)
                    jump('p2', 20)
                elif p1['char'] == 'shield':
                    stun('p2',30)
                elif p1['char'] == 'hammer':
                    p1['hammer'].x = p1['rect'].center[0] - 15 + p1['face'] * 15
                    p1['hammer'].y = p1['rect'].center[1] - 25
                    if p1['face'] == -1:
                        p1['hammerImg'] = pygame.transform.flip(p1['hammerImg'], True, False)
                    p1['hammerFace'] = p1['face']
                    p1['skill2'] -= 30
                elif p1['char'] == 'spear':
                    pass
                damage('p2',p1['dmg1'])
                p1['skill2'] += 30
            if p1['char'] == 'spear':
                p1['rect'].x = min(760, p1['rect'].x + 200) if p1['face'] == 1 else max(0,p1['rect'].x - 200)
                stun('p1',10)

        elif p1['skill1'] == p1['attackTime'][3]:
            setImg('p1', p1['face'],p1_imgs[0])
        p1['skill1'] += 1

    # p1 skill2
    if p1['skill2_timer'] > 0:
        if p1['skill2_timer'] == 600:
            setImg('p1', p1['face'],p1_imgs[5])

            if p1['char'] == 'fighter':
                if isHit(p2['rect'].x, p2['rect'].y, p1['rect'].center, p1['attackX2'], p1['attackY2'], p1['face']):
                    stun('p1', 25)
                    stun('p2', 120)
                    p2['rect'].x = p1['rect'].x + p1['face'] * 29
                    p2['rect'].y = p1['rect'].y - 10
                    damage('p2',1)
            elif p1['char'] == 'shield':
                stun('p1', 30)
            elif p1['char'] == 'hammer':
                pass
            elif p1['char'] == 'spear':
                stun('p1', 30)

        elif p1['skill2_timer'] == 600 - p1['attackTime'][4]:
            setImg('p1', p1['face'],p1_imgs[6])

            if isHit(p2['rect'].x, p2['rect'].y, p1['rect'].center, p1['attackX2'], p1['attackY2'], p1['face']):
                if p1['char'] == 'fighter':
                    p2['rect'].x = WIDTH - 40 if p1['face'] == 1 else 0
                    damage('p2',p1['dmg2'])
                elif p1['char'] == 'shield':
                    p1['absorb'] = 4
                elif p1['char'] == 'hammer':
                    stun('p1',60)
                elif p1['char'] == 'spear':
                    p1['cool'] = 5

        elif p1['skill2_timer'] == 600 - p1['attackTime'][5]:
            setImg('p1', p1['face'],p1_imgs[0])

            if p1['char'] == 'fighter':
                pass
            elif p1['char'] == 'shield':
                p1['absorb'] = 1
            elif p1['char'] == 'hammer':
                pass
            elif p1['char'] == 'spear':
                p1['cool'] = 20

        p1['skill2_timer'] -= 1

    # p1 hammer 
    if p1['char'] == 'hammer' and p1['attackTime'][2]+1 <= p1['skill1'] <= p1['attackTime'][3] and p1['skill1'] % 3 == 0 and 0 < p1['hammer'].x < 765:
        p1['hammerImg'] = pygame.transform.rotate(p1['hammerImg'],p1['hammerFace'] * 90.0)
        p1['hammer'].x = min(p1['hammer'].x + p1['hammerFace'] * 15, 765) if p1['hammerFace'] == 1 else max(p1['hammer'].x + p1['hammerFace'] * 15, 0)
        if isHit(p2['rect'].x,p2['rect'].y, p1['hammer'].center, (-17,17), (-17,17),p1['hammerFace']):
            damage('p2', 10)
            p1['skill2'] += 30
            p1['hammer'].x = 765
            setImg('p1',p1['face'],p1_imgs[0])
            p1['skill1'] = p1['cool1']
        if p1['hammer'].x == 765 or p1['hammer'].x == 0:
            setImg('p1',p1['face'],p1_imgs[0])
            p1['skill1'] = p1['cool1']

    #p1 lightning
    if p1['char'] == 'hammer' and 600 - p1['attackTime'][5] <= p1['skill2_timer'] <= 600 - p1['attackTime'][4] and p1['skill2_timer'] % 10 == 0:
        lightning1[0] = random.random() * 400 + p1['rect'].center[0] - 200
        if isHit(p2['rect'].x,p2['rect'].y,lightning1.center,(-20,20),(-100,100),1):
            damage('p2', 15) 

    # p2 attack
    if p2['attack'] < p2['cool']:
        if p2['attack'] == 0:
            setImg('p2', p2['face'],p2_imgs[1])
        elif p2['attack'] == p2['attackTime'][0]:
            setImg('p2', p2['face'],p2_imgs[2])

            if isHit(p1['rect'].x, p1['rect'].y, p2['rect'].center, p2['attackX'], p2['attackY'], p2['face']):
                damage('p1',p2['dmg'])
                if p2['char'] == 'fighter':
                    pass
                elif p2['char'] == 'shield':
                    pass
                elif p2['char'] == 'hammer':
                    stun('p1',10)
                elif p2['char'] == 'spear' and 600 - p2['attackTime'][4] >= p2['skill2_timer'] >= 600 - p2['attackTime'][5]:
                    p2['skill2'] -= 10
                    p1['skill2'] -= 4
                p2['skill2'] += 10

        elif p2['attack'] == p2['attackTime'][1]:
            setImg('p2', p2['face'],p2_imgs[0])
        p2['attack'] += 1

    # p2 skill1
    if p2['skill1'] < p2['cool1']:
        if p2['skill1'] == 0:
            setImg('p2', p2['face'],p2_imgs[3])
        elif p2['skill1'] == p2['attackTime'][2]:
            setImg('p2', p2['face'],p2_imgs[4])

            if isHit(p1['rect'].x, p1['rect'].y, p2['rect'].center, p2['attackX1'], p2['attackY1'], p2['face']):
                if p2['char'] == 'fighter':
                    jump('p2', 10)
                    jump('p1', 20)
                elif p2['char'] == 'shield':
                    stun('p1', 30)
                elif p2['char'] == 'hammer':
                    p2['hammer'].x = p2['rect'].center[0] - 15 + p2['face'] * 15
                    p2['hammer'].y = p2['rect'].center[1] - 25
                    if p2['face'] == -1:
                        p2['hammerImg'] = pygame.transform.flip(p2['hammerImg'], True, False)
                    p2['hammerFace'] = p2['face']
                    p2['skill2'] -= 30
                damage('p1',p2['dmg1'])
                p2['skill2'] += 30
            if p2['char'] == 'spear':
                p2['rect'].x = min(760, p2['rect'].x + 200) if p2['face'] == 1 else max(0,p2['rect'].x - 200)
                stun('p2',10)

        elif p2['skill1'] == p2['attackTime'][3]:
            setImg('p2', p2['face'],p2_imgs[0])
        p2['skill1'] += 1

    # p2 skill2
    if p2['skill2_timer'] > 0:
        if p2['skill2_timer'] == 600:
            setImg('p2', p2['face'],p2_imgs[5])

            if isHit(p1['rect'].x, p1['rect'].y, p2['rect'].center, p2['attackX2'], p2['attackY2'], p2['face']):
                if p2['char'] == 'fighter':
                    stun('p2', 25)
                    stun('p1', 120)
                    p1['rect'].x = p2['rect'].x + p2['face'] * 29
                    p1['rect'].y = p2['rect'].y - 10
                    damage('p1',1)
                elif p2['char'] == 'shield':
                    stun('p2', 30)
                elif p2['char'] == 'hammer':
                    pass
                elif p2['char'] == 'spear':
                    stun('p2', 30)

        elif p2['skill2_timer'] == 600 - p2['attackTime'][4]:
            setImg('p2', p2['face'],p2_imgs[6])

            if isHit(p1['rect'].x, p1['rect'].y, p2['rect'].center, p2['attackX2'], p2['attackY2'], p2['face']):
                if p2['char'] == 'fighter':
                    p1['rect'].x = WIDTH - 40 if p2['face'] == 1 else 0
                    damage('p1',p2['dmg2'])
                elif p2['char'] == 'shield':
                    p2['absorb'] = 4
                elif p2['char'] =='hammer':
                    stun('p2',60)
                elif p2['char'] == 'spear':
                    p2['cool'] = 5
                

        elif p2['skill2_timer'] == 600 - p2['attackTime'][5]:
            setImg('p2', p2['face'],p2_imgs[0])

            if p2['char'] == 'fighter':
                pass
            elif p2['char'] == 'shield':
                p2['absorb'] = 1
            elif p2['char'] == 'spear':
                p2['cool'] = 20

        p2['skill2_timer'] -= 1

    # p2 hammer 
    if p2['char'] == 'hammer' and p2['attackTime'][2]+1 <= p2['skill1'] <= p2['attackTime'][3] and p2['skill1'] % 3 == 0 and 0 < p2['hammer'].x < 765:
        p2['hammerImg'] = pygame.transform.rotate(p2['hammerImg'],p2['hammerFace'] * 90.0)
        p2['hammer'].x = min(p2['hammer'].x + p2['hammerFace'] * 15, 765) if p2['hammerFace'] == 1 else max(p2['hammer'].x + p2['hammerFace'] * 15, 0)
        if isHit(p1['rect'].x,p1['rect'].y, p2['hammer'].center, (-17,17), (-17,17),p2['hammerFace']):
            damage('p1', 10)
            p2['skill2'] += 30
            p2['hammer'].x = 765
            setImg('p2',p2['face'],p2_imgs[0])
            p2['skill1'] = p2['cool1']
        if p2['hammer'].x == 765 or p2['hammer'].x == 0:
            setImg('p2',p2['face'],p2_imgs[0])
            p2['skill1'] = p2['cool1']

    #p2 lightning
    if p2['char'] == 'hammer' and 600 - p2['attackTime'][5] <= p2['skill2_timer'] <= 600 - p2['attackTime'][4] and p2['skill2_timer'] % 10 == 0:
        lightning2[0] = random.random() * 400 + p2['rect'].center[0] - 200
        if isHit(p1['rect'].x,p1['rect'].y,lightning2.center,(-20,20),(-100,100),1):
            damage('p1', 15)
    
    if p1['stun'] == 0:
        p1['rect'].y = min(260 ,p1['rect'].y - p1['jump'])
        p1['jump'] -= 1

    if p2['stun'] == 0:
        p2['rect'].y = min(260,p2['rect'].y - p2['jump'])
        p2['jump'] -= 1


# Main game loop
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    move()
    update()
    draw()

    if p1['health'] <= 0 or p2['health'] <= 0:
        running = False
        winnerText = textFont.render(f"Player {'1' if p1['health'] > p2['health'] else '2' if p2['health'] > p1['health'] else '1,2'} Wins!", True, BLUE if p1['health'] >= p2['health'] else RED)
        screen.blit(winnerText, (270,120))
        pygame.display.flip()
        time.sleep(10)


pygame.quit()