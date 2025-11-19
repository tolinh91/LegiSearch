# 📁 Thư mục Dữ liệu

Thư mục này chứa các file dữ liệu cho hệ thống Tra cứu Luật.

## Cấu trúc

```
data/
├── faq.csv              # File FAQ (Câu hỏi thường gặp)
├── laws/                # Thư mục chứa văn bản pháp luật
│   ├── luat_dat_dai.json
│   ├── luat_nha_o.json
│   └── ...
└── README.md            # File này
```

## File FAQ (faq.csv)

File CSV chứa các câu hỏi thường gặp với cấu trúc:

```csv
question,answer,category
"Điều kiện để được cấp sổ đỏ là gì?","Để được cấp sổ đỏ, bạn cần đáp ứng các điều kiện...","Cấp sổ đỏ"
"Tôi có được bồi thường khi Nhà nước thu hồi đất không?","Có, khi Nhà nước thu hồi đất...","Thu hồi đất"
```

### Các cột:
- **question**: Câu hỏi
- **answer**: Câu trả lời
- **category**: Danh mục (tùy chọn)

## File Văn bản Pháp luật

Các file văn bản pháp luật có thể được lưu dưới dạng JSON với cấu trúc:

```json
{
  "law_name": "Luật Đất đai",
  "law_number": "45/2013/QH13",
  "articles": [
    {
      "article": "75",
      "title": "Điều kiện cấp Giấy chứng nhận quyền sử dụng đất",
      "chapter": "Chương V",
      "content": "Giấy chứng nhận quyền sử dụng đất được cấp cho người sử dụng đất khi đáp ứng đủ các điều kiện sau đây:\n\n1. Có đủ giấy tờ về quyền sử dụng đất theo quy định;\n2. Đất không có tranh chấp;\n3. Quyền sử dụng đất không bị kê biên để bảo đảm thi hành án;\n4. Đang sử dụng đất ổn định.",
      "preview": "Giấy chứng nhận quyền sử dụng đất được cấp cho người sử dụng đất khi đáp ứng đủ các điều kiện theo quy định của pháp luật..."
    }
  ]
}
```

## Lưu ý

- Đảm bảo file `faq.csv` có encoding UTF-8 để hiển thị đúng tiếng Việt
- Các file JSON nên được format đúng cấu trúc
- Dữ liệu mẫu có thể được thay thế bằng dữ liệu thực tế

