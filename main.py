import pygame
from pygame import mixer
import random
import math

# Khởi tạo Pygame
pygame.init()

# Kích thước màn hình
screen = pygame.display.set_mode((900, 600))

# Tải hình nền cho giao diện trước khi vào game
menu_background = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background, (900, 600))

# Tải nền cho game
game_background = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/background.jpg")
game_background = pygame.transform.scale(game_background, (900, 600))

# Tải hình ảnh các nút
start_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/start_button.png")
start_button_img = pygame.transform.scale(start_button_img, (200, 60))

shop_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/shop_button.png")
shop_button_img = pygame.transform.scale(shop_button_img, (200, 60))

setting_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/setting_button.png")
setting_button_img = pygame.transform.scale(setting_button_img, (200, 60))

quit_button_img = pygame.image.load("C:/Users/Admin/Documents/My game project/assets/images/quit_button.png")
quit_button_img = pygame.transform.scale(quit_button_img, (200, 60))

# Tạo các nút cho menu
start_button_rect = start_button_img.get_rect(center=(450, 350))  # Nút Start ở giữa trên cùng
setting_button_rect = setting_button_img.get_rect(center=(300, 420))  # Nút Setting lệch trái và cách xa Start
quit_button_rect = quit_button_img.get_rect(center=(600, 420))  # Nút Quit lệch phải và cách xa Start



# Tải nhạc nền
mixer.music.load("C:/Users/Admin/Documents/My game project/assets/sounds/background.wav")
mixer.music.play(-1)  # Chơi nhạc nền lặp lại vô hạn

# Tiếng súng
laser_sound = mixer.Sound("C:/Users/Admin/Documents/My game project/assets/sounds/laser.wav")

# Thiết lập tiêu đề và biểu tượng của trò chơi
pygame.display.set_caption("Soldier vs Zombie")
icon = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/enemy.png')
pygame.display.set_icon(icon)

# Người chơi
playerImg = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/player.png')
playerImg = pygame.transform.scale(playerImg, (70, 70))  # Thay đổi kích thước của hình ảnh người chơi
playerX = 836  # Vị trí ban đầu của người chơi ở bên phải màn hình
playerY = 300  # Vị trí theo chiều dọc của người chơi
playerX_change = 0  # Biến thay đổi vị trí người chơi theo chiều ngang
playerY_change = 0  # Biến thay đổi vị trí người chơi theo chiều dọc

# Tải hình ảnh dưới người chơi (ví dụ: một hình ảnh nền hoặc icon)
player_base_img = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/base_image.png')  # Thay đổi bằng hình ảnh của bạn
player_base_img = pygame.transform.scale(player_base_img, (70, 70))  # Điều chỉnh kích thước hình ảnh

# Kẻ thù
enemy_idle = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/idle/enemy_idle_{i}.png') for i in range(1, 16)]
enemy_walk = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/walk/enemy_walk_{i}.png') for i in range(1, 11)]
enemy_attack = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/attack/enemy_attack_{i}.png') for i in range(1, 9)]
enemy_dead = [pygame.image.load(f'C:/Users/Admin/Documents/My game project/assets/images/dead/enemy_dead_{i}.png') for i in range(1, 13)]

# Thay đổi kích thước của hình ảnh kẻ thù
enemy_idle = [pygame.transform.scale(img, (64, 64)) for img in enemy_idle]  
enemy_walk = [pygame.transform.scale(img, (64, 64)) for img in enemy_walk]  
enemy_attack = [pygame.transform.scale(img, (64, 64)) for img in enemy_attack]  
enemy_dead = [pygame.transform.scale(img, (64, 64)) for img in enemy_dead]

num_of_enemies = 5  # Số lượng kẻ thù ban đầu

# Khởi tạo danh sách các kẻ thù
enemyX = [random.randint(0, 50) for _ in range(num_of_enemies)]  # Đặt các kẻ thù ra ngoài màn hình (phía bên trái)
enemyY = [random.randint(50, 550) for _ in range(num_of_enemies)]
enemyX_change = [2 for _ in range(num_of_enemies)]  # Chuyển động kẻ thù theo hướng X từ trái sang phải
enemyY_change = [0 for _ in range(num_of_enemies)]  # Chuyển động kẻ thù theo hướng Y
enemy_state = ["idle" for _ in range(num_of_enemies)]  # Trạng thái của kẻ thù
enemy_dead_frame = [0 for _ in range(num_of_enemies)]  # Đếm frame cho mỗi zombie để điều khiển animation chết

# Đạn
bulletImg = pygame.image.load('C:/Users/Admin/Documents/My game project/assets/images/bullet.png')
bulletImg = pygame.transform.scale(bulletImg, (30, 20))  # Điều chỉnh kích thước của đạn
bulletX = 0  # Vị trí ban đầu của đạn
bulletY = 300  # Vị trí Y của đạn
bulletX_change = -20  # Tốc độ di chuyển của đạn
bullet_state = "ready"  # Trạng thái của đạn

# Điểm số
score_value = 0  # Điểm ban đầu
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10  # Vị trí X hiển thị điểm số
testY = 10  # Vị trí Y hiển thị điểm số

# Thông báo khi kết thúc trò chơi
over_font = pygame.font.Font('freesansbold.ttf', 64)

# Biến theo dõi số lượng zombie đã vượt qua màn hình
zombies_passed = 0

# Hàm hiển thị điểm số
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))  # Render điểm số với màu trắng
    screen.blit(score, (x, y))  # Hiển thị điểm trên màn hình

# Hàm hiển thị thông báo Game Over
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))  # Render Game Over với font lớn
    screen.blit(over_text, (200, 250))  # Hiển thị thông báo Game Over tại vị trí (200, 250)

# Hàm vẽ người chơi lên màn hình
def player(x, y):
    screen.blit(playerImg, (x, y))  # Vẽ người chơi
    screen.blit(player_base_img, (x, y + 30))  # Vẽ hình ảnh dưới chân người chơi (cộng thêm 70px vào Y để đặt dưới)
# Hàm vẽ kẻ thù lên màn hình
def enemy(x, y, i, frame_count):
    if enemy_state[i] == "dead":
        # Nếu kẻ thù đã chết, vẽ animation "dead" và chỉ vẽ 1 lần
        screen.blit(enemy_dead[enemy_dead_frame[i] // 10], (x, y))  # Giảm giá trị 20 thành 10 để animation nhanh hơn
        # Cập nhật frame chết
        enemy_dead_frame[i] += 1
        # Nếu animation chết đã hoàn tất, xóa kẻ thù khỏi màn hình và khởi tạo lại kẻ thù
        if enemy_dead_frame[i] >= len(enemy_dead) * 10:  # Điều chỉnh lại để phù hợp với việc giảm giá trị
            enemy_state[i] = "removed"  # Đánh dấu kẻ thù đã biến mất
            enemyX[i] = random.randint(100, 200)  # Khởi tạo lại vị trí kẻ thù từ khoảng 100 đến 200
            enemyY[i] = random.randint(50, 550)  # Vị trí ngẫu nhiên mới
            enemy_state[i] = "idle"  # Đặt lại trạng thái thành "idle"
            enemy_dead_frame[i] = 0  # Đặt lại frame chết

    elif enemy_state[i] == "removed":
        # Nếu trạng thái zombie là "removed", không vẽ nữa
        pass
    else:
        # Nếu kẻ thù chưa chết, vẽ animation "walk"
        screen.blit(enemy_walk[(frame_count // 20) % len(enemy_walk)], (x, y))

# Hàm bắn đạn
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"  # Thay đổi trạng thái của đạn khi bắn
    laser_sound.play()  # Phát âm thanh bắn đạn
    screen.blit(bulletImg, (x - 20, y + 17))  # Điều chỉnh vị trí Y của đạn thấp hơn một chút (y + 10)

def isCollision(x1, y1, x2, y2, i):
    bullet_width = bulletImg.get_width()  
    bullet_height = bulletImg.get_height()  
    enemy_width = enemy_idle[0].get_width()  
    enemy_height = enemy_idle[0].get_height()  

    bullet_y_adjusted = y1 + bullet_height // 2
    if math.sqrt(math.pow(x1 - x2, 2) + math.pow(bullet_y_adjusted - y2, 2)) < (bullet_width // 2 + enemy_width // 2):
        # Kiểm tra nếu kẻ thù chưa chết
        if enemy_state[i] != "dead" and enemy_state[i] != "removed":
            enemy_state[i] = "dead"  # Chuyển trạng thái zombie thành "dead" khi trúng đạn
        return True
    return False


# Hàm hiển thị menu chính
def show_main_menu():
    screen.blit(menu_background, (0, 0))  # Hiển thị hình nền menu
    screen.blit(start_button_img, start_button_rect)  # Hiển thị nút Start
    screen.blit(setting_button_img, setting_button_rect)  # Hiển thị nút Setting
    screen.blit(quit_button_img, quit_button_rect)  # Hiển thị nút Quit
    pygame.display.update()  # Cập nhật màn hình menu

# Vòng lặp chính của game
running = True
game_started = False  # Biến trạng thái xem game đã bắt đầu chưa
frame_count = 0  # Biến đếm frame animation của kẻ thù

while running:
    if not game_started:
        # Hiển thị menu chính
        show_main_menu()

        # Kiểm tra sự kiện khi người chơi tương tác với menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Kiểm tra nếu người chơi nhấp vào nút Start
                if start_button_rect.collidepoint(event.pos):
                    game_started = True  # Bắt đầu game
                    # Reset điểm số và trạng thái của các kẻ thù khi bắt đầu trò chơi
                    score_value = 0
                    zombies_passed = 0
                    enemy_state = ["idle" for _ in range(num_of_enemies)]  # Đảm bảo không có kẻ thù nào bị chết tự động

    else:
        # Cập nhật màn hình nền
        screen.blit(game_background, (0, 0))  # Hiển thị nền game

        # Kiểm tra sự kiện trong game (di chuyển người chơi và bắn đạn)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -5  # Di chuyển sang trái
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5  # Di chuyển sang phải
                if event.key == pygame.K_UP:
                    playerY_change = -5  # Di chuyển lên trên
                if event.key == pygame.K_DOWN:
                    playerY_change = 5  # Di chuyển xuống dưới
                if event.key == pygame.K_SPACE and bullet_state == "ready":
                    # Bắn đạn khi người chơi nhấn phím Space
                    bulletX = playerX
                    bulletY = playerY
                    fire_bullet(bulletX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playerY_change = 0

        # Cập nhật vị trí người chơi
        playerX += playerX_change
        playerY += playerY_change

        # Giới hạn vị trí người chơi trong màn hình
        if playerX <= 0:
            playerX = 0
        elif playerX >= 836:
            playerX = 836
        if playerY <= 0:
            playerY = 0
        elif playerY >= 530:
            playerY = 530

        # Cập nhật trạng thái đạn
        if bullet_state == "fire":
            fire_bullet(bulletX, bulletY)
            bulletX += bulletX_change

        if bulletX <= 0:
            bullet_state = "ready"
            bulletX = 0  # Đặt lại vị trí của đạn
            bulletY = 300

        # Cập nhật chuyển động của kẻ thù
        for i in range(num_of_enemies):
            if enemy_state[i] != "dead" and enemy_state[i] != "removed":
                enemyX[i] += enemyX_change[i]  # Chỉ di chuyển kẻ thù nếu chưa chết

            # Kiểm tra va chạm với kẻ thù
            if isCollision(bulletX, bulletY, enemyX[i], enemyY[i], i):
                score_value += 1  # Tăng điểm khi tiêu diệt kẻ thù
                bullet_state = "ready"  # Đặt lại trạng thái đạn
                bulletX = 0  # Đặt lại vị trí của đạn
                bulletY = 300
                enemy_state[i] = "dead"  # Chuyển trạng thái kẻ thù thành dead

            if enemyX[i] >= 836:
                zombies_passed += 1

        # Vẽ các kẻ thù
        for i in range(num_of_enemies):
            enemy(enemyX[i], enemyY[i], i, frame_count)

        # Vẽ người chơi
        player(playerX, playerY)

        # Hiển thị điểm số
        show_score(textX, testY)
        

        # Kiểm tra nếu có 5 zombie đã vượt qua màn hình, game over
        if zombies_passed >= 5:
            game_over_text()
            pygame.display.update()  # Cập nhật màn hình game
            pygame.time.wait(2000)  # Chờ 2 giây
            zombies_passed = 0  # Reset số zombie vượt qua
            game_started = False  # Quay lại màn hình menu chính
        
        clock = pygame.time.Clock()
        clock.tick(90)  # FPS = 90
        pygame.display.update()  # Cập nhật màn hình game

        # Tăng số frame để sử dụng cho animation
        frame_count += 1
        if frame_count >= 999:
            frame_count = 0