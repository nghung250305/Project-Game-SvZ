Soldier vs Zombie (SvZ)

Mô tả:
"Soldier vs Zombie" là một trò chơi bắn súng 2D nơi bạn hóa thân thành người lính chiến đấu chống lại đội quân zombie đang tràn ngập. Nhiệm vụ của bạn là tiêu diệt kẻ thù, bảo vệ bản thân và đạt điểm số cao nhất.

Tính năng chính

Chọn cấp độ chơi: Easy, Medium, Hard.

Nhiều loại kẻ thù: Zombie thường và boss với hành vi di chuyển, tấn công, và chết.

Tương tác hấp dẫn: Hệ thống bắn đạn, tính điểm, số mạng sống.

Giao diện đẹp: Hình nền, âm thanh và đồ họa bắt mắt.


Cài đặt

1. Yêu cầu hệ thống

Python: 3.7 hoặc mới hơn.

Pygame: Thư viện đồ họa Python.


2. Cài đặt thư viện cần thiết

Chạy lệnh sau để cài đặt pygame nếu chưa có:

pip install pygame

3. Cấu trúc thư mục

Tạo cấu trúc thư mục như sau:

project/
├── assets/
│   ├── images/
│   │   ├── menu_background.jpg
│   │   ├── background.jpg
│   │   ├── background_easy.jpg
│   │   ├── background_medium.png
│   │   ├── background_hard.jpg
│   │   ├── start_button.png
│   │   ├── shop_button.png
│   │   ├── setting_button.png
│   │   ├── quit_button.png
│   │   ├── life.png
│   │   ├── player.png
│   │   ├── base_image.png
│   │   ├── bullet.png
│   │   ├── idle/
│   │   ├── walk/
│   │   ├── attack/
│   │   ├── dead/
│   │   ├── boss_idle/
│   │   └── logo.jpg
│   └── sounds/
│       ├── background.wav
│       └── laser.wav
└── main.py

4. Chạy trò chơi

Trong thư mục chứa file main.py, chạy lệnh:

python main.py

Hướng dẫn chơi

1. Bắt đầu trò chơi

Khởi động game và vào menu chính.

Chọn "Start" để bắt đầu.


2. Cách điều khiển

Phím mũi tên: Di chuyển nhân vật.

Phím Space: Bắn đạn tiêu diệt zombie.


3. Mục tiêu

Ngăn không để zombie vượt qua màn hình.

Giữ mạng sống của nhân vật, tiêu diệt càng nhiều zombie càng tốt.

Đối mặt và đánh bại boss khi xuất hiện.


4. Cấp độ

Easy: Zombie di chuyển chậm, ít zombie.

Medium: Zombie nhanh hơn, số lượng tăng.

Hard: Zombie đông, tốc độ di chuyển rất nhanh.


Đóng góp

Nếu bạn có ý tưởng hoặc đóng góp, hãy liên hệ qua email hoặc tạo pull request trên GitHub.

Chúc bạn chơi game vui vẻ!
