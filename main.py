import pygame
import random

# Initalize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))
# Change title
pygame.display.set_caption("Space Invaders")
# Change icon pygame
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

background = pygame.image.load("images/background.png")

#Player
playerImg = pygame.image.load('images/player.png')  # thêm hình ảnh tàu chiến
playerX = 370  # Vị trí xuất hiện theo chiều ngang - tính từ bên trái
playerY = 480  # Vị trí xuất hiện theo chiều cao - tính từ trên xuống
playerX_change = 0
playerY_change = 0
def player(x,y):
    screen.blit(playerImg, (x, y))

enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50,370)
enemyX_change = 3
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemyImg, (x, y))

# Flag check game running: like threading python
running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    # playerX += 0.5
    # print(playerX)
    # catch event QUIT
    for event in pygame.event.get():
        # without the window open/close immediately
        if event.type == pygame.QUIT: # Catch when user click X to close pygame window
            running = False
        # elif event.type == pygame.KEYDOWN:
        # playerX += 0.1 => player chuyển động từ từ 0.1px sang bên phải
        # playerX -= 0.1 => player chuyển động từ từ 0.1px sang bên trái
        # playerY -= 0.1 => player chuyển động từ từ 0.1px lên trên
        # player += 0.1 => player chuyển động từ từ 0.1px xuống dưới
        # keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:  # Nếu phím đã được nhấn thì kiểm tra đó là trái hay phải
            # print('Phím đang được nhấn')
            if event.key == pygame.K_LEFT:  # Kiểm tra xem phím mũi tên trái có đang được nhấn không
                # print('Phím mũi tên trái đang được nhấn')
                playerX_change = -3.0
                # playerX -= 3
            if event.key == pygame.K_RIGHT:  # Kiểm tra xem phím mũi tên phải có đang được nhấn không
                # print('Phím mũi tên phải đang được nhấn')
                playerX_change = 3.0
                # playerX += 3
            if event.key == pygame.K_UP:  # Kiểm tra xem phím mũi tên trái có đang được nhấn không
                # print('Phím mũi tên trái đang được nhấn')
                playerY_change = -3.0
                # playerX -= 3
            if event.key == pygame.K_DOWN:  # Kiểm tra xem phím mũi tên phải có đang được nhấn không
                # print('Phím mũi tên phải đang được nhấn')
                playerY_change = 3.0
                # playerX += 3
        if event.type == pygame.KEYUP:  # Nếu phím được ngừng nhấn
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # Phím mũi tên trái hoặc phải được nhấc lên
                # print("Ngừng nhấn tổ hợp phím")
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # Phím mũi tên trái hoặc phải được nhấc lên
                # print("Ngừng nhấn tổ hợp phím")
                playerY_change = 0
    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800-64(chiều rộng của phi thuyền)
        playerX = 736
        enemyX += enemyX_change
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change
        # enemyY += enemyY_change
    
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # Update while running
    pygame.display.update()