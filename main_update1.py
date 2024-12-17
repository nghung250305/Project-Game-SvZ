import pygame
from pygame import mixer
import random
import math
import time  # Thêm thư viện time để xử lý thời gian chờ

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((900, 600))

# Tải hình nền cho giao diện menu
menu_background = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background, (900, 600))

# Tải hình nền cho game
game_background = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/background.jpg")
game_background = pygame.transform.scale(game_background, (900, 600))

# Tải hình ảnh các nút trên menu
start_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/start_button.png")
start_button_img = pygame.transform.scale(start_button_img, (200, 60))

shop_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/shop_button.png")
shop_button_img = pygame.transform.scale(shop_button_img, (200, 60))

setting_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/setting_button.png")
setting_button_img = pygame.transform.scale(setting_button_img, (200, 60))

quit_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/quit_button.png")
quit_button_img = pygame.transform.scale(quit_button_img, (200, 60))

# Tải hình ảnh cho biểu tượng mạng của người chơi
life_image = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/life.png')  
life_image = pygame.transform.scale(life_image, (40, 40))  

# Tạo các nút cho menu
start_button_rect = start_button_img.get_rect(center=(450, 350))  
setting_button_rect = setting_button_img.get_rect(center=(300, 420))  
quit_button_rect = quit_button_img.get_rect(center=(600, 420))  

# Tải hình ảnh nút cho các cấp độ
easy_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/easy_button.png")
easy_button_img = pygame.transform.scale(easy_button_img, (200, 60))

medium_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/medium_button.png")
medium_button_img = pygame.transform.scale(medium_button_img, (200, 60))

hard_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/hard_button.png")
hard_button_img = pygame.transform.scale(hard_button_img, (200, 60))

# Tạo các nút cho chọn cấp độ
easy_button_rect = easy_button_img.get_rect(center=(450, 300))
medium_button_rect = medium_button_img.get_rect(center=(450, 360))
hard_button_rect = hard_button_img.get_rect(center=(450, 420))

# Tải nhạc nền cho trò chơi
mixer.music.load("C:/Users/Admin/Documents/My game project/assets/sounds/background.wav")
mixer.music.play(-1)  

# Tiếng súng
laser_sound = mixer.Sound("C:/Users/Admin/Documents/My game project/assets/sounds/laser.wav")

# Thiết lập tiêu đề và biểu tượng của trò chơi
pygame.display.set_caption("Soldier vs Zombie")

icon = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/enemy.png')
pygame.display.set_icon(icon)

# Người chơi
playerImg = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/player.png')
playerImg = pygame.transform.scale(playerImg, (70, 70))  
playerX = 836  # Vị trí ban đầu của người chơi theo trục X
playerY = 300  # Vị trí ban đầu của người chơi theo trục Y
playerX_change = 0  # Biến thay đổi vị trí theo trục X
playerY_change = 0  # Biến thay đổi vị trí theo trục Y

player_base_img = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/base_image.png')  
player_base_img = pygame.transform.scale(player_base_img, (70, 70))  

# Kẻ thù
enemy_idle = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/idle/enemy_idle_{i}.png') for i in range(1, 16)]
enemy_walk = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/walk/enemy_walk_{i}.png') for i in range(1, 11)]
enemy_attack = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/attack/enemy_attack_{i}.png') for i in range(1, 9)]
enemy_dead = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/dead/enemy_dead_{i}.png') for i in range(1, 13)]

# Thay đổi kích thước hình ảnh kẻ thù
enemy_idle = [pygame.transform.scale(img, (64, 64)) for img in enemy_idle]
enemy_walk = [pygame.transform.scale(img, (64, 64)) for img in enemy_walk]
enemy_attack = [pygame.transform.scale(img, (64, 64)) for img in enemy_attack]
enemy_dead = [pygame.transform.scale(img, (64, 64)) for img in enemy_dead]

# Load boss idle animation frames
boss_idle = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/boss_idle/boss_idle_{i}.png') for i in range(1, 6)]
boss_idle = [pygame.transform.scale(img, (128, 128)) for img in boss_idle]  # Tùy chỉnh kích thước boss

# Khởi tạo các giá trị kẻ thù
num_of_enemies = 5  

# Vị trí ban đầu của các kẻ thù
enemyX = [random.randint(0, 50) for _ in range(num_of_enemies)]  
enemyY = [random.randint(50, 550) for _ in range(num_of_enemies)]
enemyX_change = [2 for _ in range(num_of_enemies)]  
enemyY_change = [0 for _ in range(num_of_enemies)]  
enemy_state = ["idle" for _ in range(num_of_enemies)]  
enemy_dead_frame = [0 for _ in range(num_of_enemies)]  

# Đạn
bulletImg = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (30, 20))  
bulletX = 0  
bulletY = 300  
bulletX_change = -20  
bullet_state = "ready"  # Trạng thái của đạn, "ready" nghĩa là đạn chưa được bắn

# Điểm số
score_value = 0  
font = pygame.font.Font('C:/Users/Admin/Documents/My game project/timesnewroman.ttf', 32)

textX = 10  # Vị trí hiển thị điểm số theo trục X
testY = 10  # Vị trí hiển thị điểm số theo trục Y

# Thông báo khi kết thúc trò chơi
over_font = pygame.font.Font('C:/Users/Admin/Documents/My game project/timesnewroman.ttf', 64)

level = "Easy"  # Cấp độ ban đầu

zombies_passed = 0

player_lives = 5  # Nhân vật có 5 mạng ban đầu

# Boss variables
bossX = 400  # Tọa độ X của boss
bossY = 300  # Tọa độ Y của boss
boss_health = 15  # Lượng máu của boss
boss_active = False  # Boss chưa xuất hiện
boss_state = "idle"  # Trạng thái ban đầu là idle

# Biến theo dõi số lần đạn trúng boss
bullet_hit_count = 0  # Số đạn đã trúng boss

# Biến xác định xem boss có xuất hiện hay không
boss_active = False

# Hàm hiển thị số mạng của người chơi
def show_lives(x, y, lives):
    for i in range(lives):
        screen.blit(life_image, (x + i * 20, y))  # Hiển thị mỗi hình mạng cách nhau 20 pixel
        
# Hàm hiển thị điểm số
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (0, 0, 0))  
    screen.blit(score, (x, y))  

# Hàm hiển thị thông báo khi game over
def game_over_text():
    over_text = over_font.render("Game Over", True, (0, 0, 0))  
    screen.blit(over_text, (300, 250))  


def show_level(x, y):
    font = pygame.font.Font("C:/Users/Admin/Documents/My game project/timesnewroman.ttf", 30)  # Kích thước font là 48
    level_text = font.render("Level : " + level, True, (0,0,0))  # Màu đỏ
    screen.blit(level_text, (x+75, y))  # Vẽ cấp độ lên màn hình

# Hàm vẽ màn hình chọn cấp độ
def draw_select_level():
    screen.blit(menu_background, (0, 0))  # Sử dụng lại background của menu
    screen.blit(easy_button_img, easy_button_rect)
    screen.blit(medium_button_img, medium_button_rect)
    screen.blit(hard_button_img, hard_button_rect)

# Hàm xử lý khi người dùng nhấn vào nút chọn cấp độ
def handle_level_click(pos):
    if easy_button_rect.collidepoint(pos):
        return "easy"
    elif medium_button_rect.collidepoint(pos):
        return "medium"
    elif hard_button_rect.collidepoint(pos):
        return "hard"
    return None

# Hàm vẽ người chơi
def player(x, y):
    screen.blit(playerImg, (x, y))  
    screen.blit(player_base_img, (x, y + 30))  

# Hàm vẽ kẻ thù
def enemy(x, y, i, frame_count):
    if enemy_state[i] == "dead":
        screen.blit(enemy_dead[enemy_dead_frame[i] // 10], (x, y))  # Hiển thị hình ảnh kẻ thù chết
        enemy_dead_frame[i] += 1
        if enemy_dead_frame[i] >= len(enemy_dead) * 10:  
            enemy_state[i] = "removed"  # Đặt trạng thái kẻ thù thành "removed"
            enemyX[i] = random.randint(100, 200)  
            enemyY[i] = random.randint(50, 550)  
            enemy_state[i] = "idle"  
            enemy_dead_frame[i] = 0  

    elif enemy_state[i] == "removed":
        pass  # Không làm gì nếu kẻ thù đã bị loại bỏ
    else:
        screen.blit(enemy_walk[(frame_count // 20) % len(enemy_walk)], (x, y))  # Hiển thị hình ảnh kẻ thù đang đi

# Function to draw boss
def draw_boss(x, y, frame_count):
    screen.blit(boss_idle[(frame_count // 20) % len(boss_idle)], (x, y))  # Hiển thị hoạt ảnh idle

# Hàm kiểm tra va chạm giữa đạn và boss
def isCollisionBoss(bossX, bossY, bulletX, bulletY):
    distance = math.sqrt(math.pow(bossX - bulletX, 2) + math.pow(bossY - bulletY, 2))
    if distance < 40:  # Nếu khoảng cách giữa đạn và boss nhỏ hơn 40, coi như có va chạm
        return True
    return False

# Hàm bắn đạn
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"  
    screen.blit(bulletImg, (x, y + 16))  

# Hàm kiểm tra va chạm giữa đạn và kẻ thù
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))  
    if distance < 40:  # Nếu khoảng cách giữa đạn và kẻ thù nhỏ hơn 40, coi như có va chạm
        return True
    else:
        return False

# Hàm vẽ menu
def draw_menu():
    screen.blit(menu_background, (0, 0))
    screen.blit(start_button_img, start_button_rect)
    screen.blit(setting_button_img, setting_button_rect)
    screen.blit(quit_button_img, quit_button_rect)

# Hàm xử lý khi người dùng nhấn vào nút trên menu
def handle_menu_click(pos):
    if start_button_rect.collidepoint(pos):
        return "start"
    elif setting_button_rect.collidepoint(pos):
        return "settings"
    elif quit_button_rect.collidepoint(pos):
        return "quit"
    return None

# Hàm reset lại trò chơi khi bắt đầu lại
def reset_game():
    global player_lives, score_value, zombies_passed, bullet_state, bulletX
    global enemyX, enemyY, enemy_state, enemy_dead_frame, num_of_enemies, enemyX_change

    player_lives = 5  # Đặt lại số mạng
    score_value = 0  # Đặt lại điểm số
    zombies_passed = 0  # Đặt lại số lượng zombie vượt qua
    bullet_state = "ready"  # Đặt lại trạng thái đạn
    bulletX = playerX  # Đặt lại vị trí của đạn
    
    # Điều chỉnh số lượng kẻ thù và tốc độ dựa theo cấp độ đã chọn
    if level == "Easy":
        num_of_enemies = 5
        enemyX_change = [1.5 for _ in range(num_of_enemies)]  # Tốc độ chậm hơn
    elif level == "Medium":
        num_of_enemies = 7
        enemyX_change = [2.5 for _ in range(num_of_enemies)]  # Tốc độ vừa
    elif level == "Hard":
        num_of_enemies = 9
        enemyX_change = [3.5 for _ in range(num_of_enemies)]  # Tốc độ nhanh hơn 
        
    # Đặt lại vị trí và trạng thái của kẻ thù
    enemyX = [random.randint(0, 50) for _ in range(num_of_enemies)]
    enemyY = [random.randint(50, 550) for _ in range(num_of_enemies)]
    enemy_state = ["idle" for _ in range(num_of_enemies)]
    enemy_dead_frame = [0 for _ in range(num_of_enemies)]

# Vòng lặp chính của trò chơi
running = True
menu = True  
frame_count = 0  
game_over = False  
game_over_time = None  

while running:
    screen.fill((0, 0, 0))  # Làm mới màn hình
    frame_count += 1  # Tăng số lượng khung hình

    if menu:
        draw_menu()  # Vẽ menu
    elif select_level:
        draw_select_level()  # Vẽ màn hình chọn cấp độ
    else:
        screen.blit(game_background, (0, 0))  # Vẽ nền game
        show_score(textX, testY)  # Hiển thị điểm số
        show_lives(textX, testY + 40, player_lives)  # Hiển thị mạng
        show_level(650, 17)  # Hiển thị cấp độ ở góc phải trên

        if game_over:
            game_over_text()  # Hiển thị thông báo kết thúc game
            if pygame.time.get_ticks() - game_over_time >= 2000:  # Đợi 2 giây trước khi quay lại menu
                menu = True  
                game_over = False  
            pygame.display.update()
            continue   # Tiếp tục vòng lặp nếu game over

        player(playerX, playerY)  # Vẽ người chơi

        for i in range(num_of_enemies):
            if enemy_state[i] != "dead" and enemy_state[i] != "removed":
                enemyX[i] += enemyX_change[i]  # Di chuyển kẻ thù

            if enemyX[i] >= 836:  # Nếu kẻ thù vượt qua màn hình
                zombies_passed += 1  
                enemy_state[i] = "removed"  
                enemyX[i] = random.randint(100, 200)  
                enemyY[i] = random.randint(50, 550)  
                enemy_state[i] = "idle"  
                player_lives -= 1  # Mất 1 mạng mỗi khi zombie vượt qua

            enemy(enemyX[i], enemyY[i], i, frame_count)  # Vẽ kẻ thù

        # Nếu hết mạng thì trò chơi kết thúc
        if player_lives <= 0:
            game_over = True  
            game_over_time = pygame.time.get_ticks()
        
        # Hiển thị số mạng dưới điểm số
        show_lives(textX, testY + 40, player_lives)  # Hiển thị mạng bên dưới điểm số

        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletX += bulletX_change

        if bulletX <= 0:
            bullet_state = "ready"  # Đặt lại trạng thái đạn

        # Kiểm tra va chạm giữa zombie và đạn
        for i in range(num_of_enemies):
            if enemy_state[i] == "idle" and bullet_state == "fire":  # Chỉ kiểm tra khi zombie "idle" và đạn đang ở trạng thái "fire"
                collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
                if collision:
                    bulletX = 836  # Đưa đạn về bên phải sau khi trúng
                    bullet_state = "ready"  # Đặt trạng thái đạn về "ready"
                    score_value += 1  # Cộng điểm khi bắn trúng kẻ thù
                    enemy_state[i] = "dead"  # Zombie bị tiêu diệt
                    laser_sound.play()  # Phát âm thanh súng
                    break  # Ngừng kiểm tra sau khi trúng zombie
        
        # Kiểm tra nếu boss đã xuất hiện
        if score_value >= 35 and not boss_active:
            boss_active = True  # Boss sẽ xuất hiện khi đạt đủ điểm số

        # Vẽ boss nếu boss active
        if boss_active:
            draw_boss(bossX, bossY, frame_count)  # Vẽ boss

            # Kiểm tra va chạm giữa đạn và boss
            if bullet_state == "fire":
                collision = isCollisionBoss(bossX, bossY, bulletX, bulletY)
                if collision:
                    bullet_hit_count += 1  # Tăng số lần đạn trúng boss
                    bulletX = 836  # Đưa đạn về vị trí ban đầu
                    bullet_state = "ready"  # Đặt lại trạng thái đạn
                    laser_sound.play()  # Phát âm thanh súng

            # Nếu số lần đạn trúng đủ 15, boss sẽ chết
            if bullet_hit_count >= 15:
                boss_active = False  # Tắt trạng thái boss
                bullet_hit_count = 0  # Reset số lần đạn trúng
                score_value += 10  # Cộng điểm khi boss bị tiêu diệt 
                
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5  # Di chuyển sang trái
            if event.key == pygame.K_RIGHT:
                playerX_change = 5  # Di chuyển sang phải
            if event.key == pygame.K_UP:
                playerY_change = -5  # Di chuyển lên
            if event.key == pygame.K_DOWN:
                playerY_change = 5  # Di chuyển xuống
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX  
                bulletY = playerY
                fire_bullet(bulletX, bulletY)
                laser_sound.play()  # Phát âm thanh khi bắn


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # Ngừng di chuyển theo trục X khi không bấm phím
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0  # Ngừng di chuyển theo trục Y khi không bấm phím

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()  # Lấy vị trí chuột
    
            if menu:  # Nếu đang ở màn hình menu
                menu_action = handle_menu_click(pos)  # Xử lý nhấn nút trong menu
                if menu_action == "start":
                    menu = False
                    select_level = True  # Chuyển sang màn hình chọn cấp độ
                elif menu_action == "quit":
                    running = False  # Thoát trò chơi

            elif select_level:  # Nếu đang ở màn hình chọn cấp độ
                level_selected = handle_level_click(pos)  # Xử lý nhấn cấp độ
                if level_selected == "easy":
                    level = "Easy"
                    select_level = False  # Thoát màn hình chọn cấp độ và vào game
                    score_value = 0
                    zombies_passed = 0
                    reset_game()  # Đặt lại trạng thái trò chơi
                    game_over = False  # Đảm bảo trạng thái game over được reset
                elif level_selected == "medium":
                    level = "Medium"
                    select_level = False
                    score_value = 0
                    zombies_passed = 0
                    reset_game()
                    game_over = False
                elif level_selected == "hard":
                   level = "Hard"
                   select_level = False
                   score_value = 0
                   zombies_passed = 0
                   reset_game()
                   game_over = False


    # Cập nhật vị trí người chơi để không ra ngoài màn hình
    playerX += playerX_change
    playerY += playerY_change

    # Kiểm tra nếu người chơi đi ra ngoài màn hình, sẽ dừng lại ở biên
    if playerX <= 0:
        playerX = 0
    elif playerX >= 836:  # 836 là giới hạn bên phải màn hình
        playerX = 836

    if playerY <= 0:
        playerY = 0
    elif playerY >= 536:
        playerY = 536

    # Giới hạn số khung hình mỗi giây (FPS)
    clock = pygame.time.Clock()
    clock.tick(120)  # FPS = 120 
    pygame.display.update()  # Cập nhật màn hình
