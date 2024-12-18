# Soldier vs Zombie 

**Soldier vs Zombie** là một game 2D bắn súng, nơi bạn điều khiển nhân vật chống lại các zombie và boss để bảo vệ căn cứ.

---

## **Mục lục**
1. [Tính năng chính](#tính-năng-chính)
2. [Cách chơi](#cách-chơi)
3. [Cài đặt](#cài-đặt)
4. [Hướng dẫn khởi chạy](#hướng-dẫn-khởi-chạy)
5. [Cấu trúc dự án](#cấu-trúc-dự-án)
6. [Ghi chú](#ghi-chú)

---

## **Tính năng chính**
- Menu chính với các nút:
  - Bắt đầu trò chơi
  - Cài đặt
  - Thoát
- Chọn độ khó: Dễ, Vừa, Khó (mỗi độ khó có tốc độ zombie khác nhau).
- Hoạt ảnh mượt mà cho zombie và boss (đi, tấn công, chết).
- Hiển thị điểm số, số mạng còn lại, cấp độ hiện tại.
- Nhạc nền và âm thanh hiệu ứng khi bắn đạn.
- Zombie vượt qua căn cứ sẽ làm mất mạng; trò chơi kết thúc khi hết mạng.
- Boss với lượng máu cố định và hoạt ảnh riêng biệt.

---

## **Cách chơi**
- **Di chuyển**: Sử dụng phím **mũi tên** (lên/xuống) để điều chỉnh vị trí nhân vật.
- **Bắn đạn**: Nhấn phím **Space**.
- **Mục tiêu**:
  - Tiêu diệt zombie trước khi chúng vượt qua căn cứ.
  - Đánh bại boss để đạt điểm số cao.
- **Lưu ý**: Trò chơi kết thúc nếu bạn để hết mạng.

---

## **Cài đặt**

### **Yêu cầu**
- Python 3.10+
- Thư viện:
  - `pygame`

### **Hướng dẫn cài đặt**
1. Cài đặt Python từ [python.org](https://www.python.org/).
2. Cài đặt thư viện `pygame` bằng lệnh:
   ```bash
   pip install pygame

   
## **Cấu Trúc Dự Án**
Soldier-vs-Zombie/
│
├── main.py                # Mã nguồn chính của trò chơi
├── README.md              # Hướng dẫn và thông tin về dự án
├── requirements.txt       # Danh sách thư viện cần cài đặt (nếu có)
└── assets/                # Thư mục chứa hình ảnh và âm thanh
    ├── images/
    │   ├── menu_background.jpg
    │   ├── background_easy.jpg
    │   ├── ...
    ├── sounds/
    │   ├── background.wav
    │   ├── laser.wav
