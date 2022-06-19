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
enemyY = random.randint(50,250)
enemyX_change = 3
enemyY_change = 40

def enemy(x,y):
    screen.blit(enemyImg, (x, y))


bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 3
bulletY_change = 5
# Ready: Đạn của chúng ta ở trạng thái sẵn sàng được bắn khi và chỉ khi ta không còn nhìn thấy trên màn hình bất kỳ viên đạn nào nữa.
# Fire: Đạn đang trong trạng thái di chuyển, ở trạng thái này phi thuyền không được bắn đạn.
bullet_state = "ready"
score = 0

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire" # khi đạn được bắn, ta thay đổi trạng thái của đạn thành "fire" - đang di chuyển
    screen.blit(bulletImg, (x+16, y+10)) # việc cộng 16 vào x và cộng 10 vào y khiến cho viên đạn xuất hiện vào đúng mũi của phi phi thuyền

def is_collistion(enemyX, enemyY, bulletX, bulletY):
    distance = ((enemyX-bulletX)**2 +(enemyY-bulletY)**2)**0.5
    if distance < 27:
        return True
    else:
        return False
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
            # if event.key == pygame.K_UP:  # Kiểm tra xem phím mũi tên trái có đang được nhấn không
            #     # print('Phím mũi tên trái đang được nhấn')
            #     playerY_change = -3.0
            #     # playerX -= 3
            # if event.key == pygame.K_DOWN:  # Kiểm tra xem phím mũi tên phải có đang được nhấn không
            #     # print('Phím mũi tên phải đang được nhấn')
            #     playerY_change = 3.0
            #     # playerX += 3
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX  # Gán tọa độ X phi thuyền vào tọa độ X của viên đạn
                fire_bullet(bulletX, bulletY)  # thay đổi
        if event.type == pygame.KEYUP:  # Nếu phím được ngừng nhấn
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:  # Phím mũi tên trái hoặc phải được nhấc lên
                # print("Ngừng nhấn tổ hợp phím")
                playerX_change = 0
            # if event.key == pygame.K_UP or event.key == pygame.K_DOWN:  # Phím mũi tên trái hoặc phải được nhấc lên
            #     # print("Ngừng nhấn tổ hợp phím")
            #     playerY_change = 0
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
    if bulletY <= 0:
        bulletY = 480  # ngay khi viên đạn đi đến điểm cuối trên cùng của màn hình game thì viên đạn sẽ quay về điểm 480px
        bullet_state = "ready"  # Và khi viên đạn đi đến điểm cuối màn hình bên trên thì trạng thái của viên đạn sẽ từ "fire" (đang di chuyển) thành "ready" (sẵn sàng)
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    collison = is_collistion(enemyX, enemyY, bulletX, bulletY)
    if collison:
        bullety=480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 800)
        enemyY = random.randint(50,150)
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # Update while running
    pygame.display.update()