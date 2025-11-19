# ⚖️ Hệ thống Tra cứu Luật - Legal Lookup System

Hệ thống tra cứu văn bản pháp luật thông minh với khả năng tìm kiếm từ khóa và tìm kiếm ngữ nghĩa (semantic search), được xây dựng bằng Streamlit.

## 📋 Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng](#tính-năng)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt](#cài-đặt)
- [Cấu trúc dự án](#cấu-trúc-dự-án)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
- [Cấu hình](#cấu-hình)
- [Phát triển](#phát-triển)
- [Đóng góp](#đóng-góp)
- [Giấy phép](#giấy-phép)

## 🎯 Giới thiệu

Hệ thống Tra cứu Luật là một ứng dụng web cho phép người dùng tra cứu thông tin pháp luật một cách nhanh chóng và chính xác. Hệ thống hỗ trợ:

- **Tìm kiếm từ khóa**: Tìm kiếm chính xác các từ khóa trong văn bản pháp luật
- **Tìm kiếm ngữ nghĩa**: Sử dụng AI để hiểu ý nghĩa câu hỏi và tìm kết quả liên quan
- **Chế độ tự động**: Hệ thống tự động chọn phương thức tìm kiếm phù hợp
- **FAQ**: Hỏi đáp về các vấn đề pháp luật thường gặp

## ✨ Tính năng

### 🔍 Tra cứu văn bản
- Tìm kiếm các điều, khoản, chương trong văn bản pháp luật
- Hỗ trợ tìm kiếm bằng từ khóa hoặc câu hỏi tự nhiên
- Hiển thị độ liên quan của kết quả (relevance score)
- Xem chi tiết nội dung đầy đủ của điều luật
- Điều hướng giữa các điều luật (Điều trước/Điều tiếp theo)

### ❓ FAQ - Hỏi đáp pháp luật
- Danh sách câu hỏi thường gặp về pháp luật
- Tìm kiếm trong FAQ
- Phân loại theo danh mục
- Hiển thị câu trả lời chi tiết

### 📘 Giới thiệu hệ thống
- Thông tin về mục tiêu và phạm vi hệ thống
- Công nghệ sử dụng
- Kiến trúc hệ thống
- Hướng phát triển

### ⚙️ Cài đặt
- Tùy chỉnh chế độ tìm kiếm mặc định
- Cấu hình số kết quả hiển thị
- Bật/tắt các tính năng (gợi ý tự động, hiển thị điểm liên quan)
- Cài đặt quyền riêng tư

## 💻 Yêu cầu hệ thống

- Python 3.8 trở lên
- pip (Python package manager)
- 4GB RAM trở lên (khuyến nghị)
- Kết nối Internet (để tải các thư viện và mô hình)

## 🚀 Cài đặt

### 1. Clone repository

```bash
git clone <repository-url>
cd LegiSearch
```

### 2. Tạo môi trường ảo (khuyến nghị)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Chuẩn bị dữ liệu

Tạo thư mục `data` và thêm các file dữ liệu cần thiết:

```
data/
  ├── faq.csv          # File FAQ (question, answer, category)
  ├── laws/            # Thư mục chứa văn bản pháp luật
  └── ...
```

**Cấu trúc file FAQ (faq.csv):**
```csv
question,answer,category
"Điều kiện để được cấp sổ đỏ là gì?","Để được cấp sổ đỏ...","Cấp sổ đỏ"
```

### 5. Chạy ứng dụng

```bash
streamlit run app.py
```

Ứng dụng sẽ tự động mở trong trình duyệt tại địa chỉ: `http://localhost:8501`

## 📁 Cấu trúc dự án

```
streamlt/
├── app.py                          # File chính của ứng dụng
├── requirements.txt                # Danh sách các thư viện cần thiết
├── README.md                       # File hướng dẫn này
│
├── pages/                          # Các trang của ứng dụng
│   ├── 1_🔍_Tra_cuu_van_ban.py    # Trang tra cứu văn bản
│   ├── 2_❓_FAQ.py                 # Trang FAQ
│   ├── 3_📘_Gioi_thieu.py         # Trang giới thiệu
│   └── 4_⚙️_Cai_dat.py            # Trang cài đặt
│
├── libs/                           # Thư viện hỗ trợ
│   ├── search.py                   # Hàm tìm kiếm (keyword, semantic)
│   ├── classifier.py               # Phân loại truy vấn
│   └── utils.py                    # Các hàm tiện ích
│
├── models/                         # Thư mục chứa mô hình ML
│   └── (các file mô hình sẽ được lưu ở đây)
│
└── data/                           # Thư mục dữ liệu
    ├── faq.csv                     # File FAQ
    └── laws/                       # Văn bản pháp luật
```

## 📖 Hướng dẫn sử dụng

### Tra cứu văn bản

1. Truy cập trang **"🔍 Tra cứu văn bản"** từ menu bên trái
2. Nhập từ khóa hoặc câu hỏi vào ô tìm kiếm
   - Ví dụ: "Điều kiện cấp sổ đỏ"
   - Ví dụ: "Tôi có được bồi thường khi thu hồi đất không?"
3. Chọn phương thức tìm kiếm:
   - **🔑 Tìm kiếm từ khóa**: Tìm chính xác các từ khóa
   - **🧠 Tìm kiếm ngữ nghĩa**: Hiểu ý nghĩa và tìm kết quả liên quan
   - **⚡ Tự động**: Hệ thống tự động chọn phương thức
4. Nhấn nút **"🔍 Tìm kiếm"** hoặc nhấn Enter
5. Xem kết quả và nhấn **"Xem chi tiết"** để xem nội dung đầy đủ

### FAQ

1. Truy cập trang **"❓ FAQ"**
2. Sử dụng ô tìm kiếm để tìm câu hỏi (nếu có)
3. Nhấn vào câu hỏi để xem câu trả lời

### Cài đặt

1. Truy cập trang **"⚙️ Cài đặt"**
2. Tùy chỉnh các cài đặt theo nhu cầu
3. Nhấn **"💾 Lưu cài đặt"** để lưu

## ⚙️ Cấu hình

### Cấu hình tìm kiếm

Trong file `libs/search.py`, bạn có thể cấu hình:

- Số lượng kết quả tối đa
- Ngưỡng độ liên quan tối thiểu
- Mô hình semantic search sử dụng

### Cấu hình dữ liệu

- Đặt file FAQ tại `data/faq.csv`
- Đặt các file văn bản pháp luật trong `data/laws/`

## 🔧 Phát triển

### Thêm tính năng tìm kiếm

1. Mở file `libs/search.py`
2. Implement các hàm:
   - `keyword_search(query)`: Tìm kiếm từ khóa
   - `semantic_search(query)`: Tìm kiếm ngữ nghĩa

**Ví dụ:**

```python
def keyword_search(query):
    """
    Tìm kiếm từ khóa trong văn bản pháp luật
    
    Args:
        query: Từ khóa tìm kiếm
        
    Returns:
        List các kết quả với format:
        [{
            'article': 'Điều 75',
            'title': 'Tiêu đề',
            'preview': 'Mô tả ngắn...',
            'content': 'Nội dung đầy đủ...',
            'chapter': 'Chương V',
            'relevance': 95
        }]
    """
    # Implement your search logic here
    pass
```

### Thêm phân loại truy vấn

1. Mở file `libs/classifier.py`
2. Implement hàm `classify_query(query)`:

```python
def classify_query(query):
    """
    Phân loại truy vấn là keyword hay semantic
    
    Args:
        query: Câu hỏi/từ khóa
        
    Returns:
        'keyword' hoặc 'semantic'
    """
    # Implement your classification logic here
    pass
```

### Kích hoạt tính năng

Sau khi implement các hàm, bỏ comment trong file `pages/1_🔍_Tra_cuu_van_ban.py`:

```python
from libs.search import keyword_search, semantic_search
from libs.classifier import classify_query
```

## 🧪 Testing

Để test ứng dụng:

```bash
# Chạy ứng dụng
streamlit run app.py

# Test các tính năng:
# 1. Test tìm kiếm từ khóa
# 2. Test tìm kiếm ngữ nghĩa
# 3. Test chế độ tự động
# 4. Test FAQ
```

## 📝 Ghi chú

- Đây là hệ thống demo cho mục đích học tập và nghiên cứu
- Để có thông tin pháp luật chính thức, vui lòng tham khảo các nguồn chính thức từ cơ quan nhà nước có thẩm quyền
- Dữ liệu mẫu được cung cấp để demo, cần thay thế bằng dữ liệu thực tế

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 Giấy phép

Dự án này được phát hành dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 👥 Tác giả

- **Nhóm phát triển** - [Tên nhóm/người phát triển]



