# Soldier vs Zombie 

**Soldier vs Zombie** là một trò chơi được phát triển bằng ngôn ngữ Python sử dụng thư viện `pygame`. Người chơi điều khiển một người lính tiêu diệt các zombie để bảo vệ căn cứ của mình. 

---

## 🎮 Cách chơi
1. **Mục tiêu:**  
   - Tiêu diệt zombie để ghi điểm.  
   - Ngăn không cho quá 5 zombie vượt qua màn hình.  

2. **Điều khiển:**  
   - **Phím mũi tên**: Di chuyển nhân vật.  
   - **Phím Space**: Bắn đạn tiêu diệt zombie.

3. **Trò chơi kết thúc:**  
   - Nếu để 5 zombie vượt qua màn hình, trò chơi sẽ kết thúc.

---

## 🛠️ Các tính năng chính
- **Hệ thống menu:**  
  Gồm các nút **Start**, **Setting**, và **Quit**.  

- **Nhạc nền & hiệu ứng âm thanh:**  
  - Nhạc nền tạo không khí hấp dẫn.  
  - Âm thanh súng khi bắn đạn.

- **Zombie hoạt họa:**  
  Kẻ thù có nhiều trạng thái: **đi bộ**, **tấn công**, và **chết** với hoạt ảnh mượt mà.  

- **Điểm số:**  
  Hiển thị điểm hiện tại của người chơi.  

---

## 📁 Cấu trúc thư mục
My game project ├── assets │   ├── images │   │   ├── background.jpg │   │   ├── menu_background.jpg │   │   ├── player.png │   │   ├── base_image.png │   │   ├── bullet.png │   │   ├── enemy.png │   │   ├── idle/ │   │   ├── walk/ │   │   ├── attack/ │   │   └── dead/ │   ├── sounds │   │   ├── background.wav │   │   └── laser.wav └── main.py
---

## 🖥️ Hướng dẫn cài đặt
1. **Yêu cầu hệ thống:**  
   - Python 3.8 trở lên.  
   - Thư viện `pygame` (cài đặt bằng `pip install pygame`).

2. **Chạy game:**  
   - Clone hoặc tải mã nguồn về máy.  
   - Đảm bảo các tài nguyên (ảnh, âm thanh) được đặt đúng cấu trúc thư mục.  
   - Mở terminal/cmd và chạy lệnh:  
     ```bash
     python main.py
     ```

---

## 🌟 Tương lai phát triển
- Thêm cửa hàng nâng cấp vũ khí và nhân vật.  
- Nhiều chế độ chơi hơn (sinh tồn, thời gian giới hạn, v.v.).  
- Hệ thống bảng xếp hạng điểm cao.  

---

## ✍️ Tác giả
- Tên: Nhóm ...
- Mã Lớp: D24CQCC02-B
- Liên hệ: nghung25030@gmail.com

---

## 📜 Bản quyền
Dự án này được phát triển cho mục đích học tập. Tất cả hình ảnh và âm thanh trong trò chơi thuộc bản quyền của tác giả hoặc nguồn miễn phí.
