import streamlit as st

st.set_page_config(
    page_title="Giới thiệu",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Header
st.markdown('<div class="intro-header"><h1>📘 Giới thiệu hệ thống Tra cứu Luật</h1></div>', unsafe_allow_html=True)

# Introduction
st.markdown("""
<div class="feature-box">
<h3>🎯 Mục tiêu hệ thống</h3>
<p>Hệ thống Tra cứu Luật được xây dựng nhằm hỗ trợ người dùng tra cứu thông tin pháp luật một cách nhanh chóng, chính xác và dễ dàng. Hệ thống cung cấp các tính năng:</p>
<ul>
<li>🔍 <strong>Tra cứu văn bản:</strong> Tìm kiếm các điều, khoản, chương trong văn bản pháp luật</li>
<li>🔑 <strong>Tìm kiếm từ khóa:</strong> Tìm kiếm chính xác theo từ khóa trong văn bản</li>
<li>🧠 <strong>Tìm kiếm ngữ nghĩa:</strong> Hiểu ý nghĩa câu hỏi và tìm kết quả liên quan</li>
<li>❓ <strong>FAQ:</strong> Hỏi đáp về các vấn đề pháp luật thường gặp</li>
<li>💡 <strong>Gợi ý tự động:</strong> Đề xuất các từ khóa và câu hỏi liên quan</li>
</ul>
</div>
""", unsafe_allow_html=True)



st.markdown("---")



# Architecture section
st.subheader("🏗️ Kiến trúc hệ thống")

st.markdown("""
<div class="feature-box">
<h3>Quy trình hoạt động</h3>
<ol>
<li><strong>Người dùng nhập truy vấn:</strong> Từ khóa hoặc câu hỏi tự nhiên</li>
<li><strong>Hệ thống phân tích:</strong> Xác định phương thức tìm kiếm (từ khóa/ngữ nghĩa/tự động)</li>
<li><strong>Tìm kiếm:</strong> 
   <ul>
   <li>Keyword Search: Tìm chính xác từ khóa trong văn bản</li>
   <li>Semantic Search: Chuyển đổi câu hỏi thành vector và tìm các văn bản tương tự</li>
   </ul>
</li>
<li><strong>Xếp hạng kết quả:</strong> Sắp xếp theo độ liên quan</li>
<li><strong>Hiển thị:</strong> Trả về kết quả với preview và tùy chọn xem chi tiết</li>
</ol>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Future development
st.subheader("🚀 Hướng phát triển")

col_future1, col_future2 = st.columns(2)

with col_future1:
    st.markdown("""
    <div class="feature-box">
    <h3>Ngắn hạn</h3>
    <ul>
    <li>Mở rộng cơ sở dữ liệu văn bản</li>
    <li>Cải thiện độ chính xác tìm kiếm</li>
    <li>Thêm tính năng lưu lịch sử tìm kiếm</li>
    <li>Tối ưu hóa giao diện người dùng</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col_future2:
    st.markdown("""
    <div class="feature-box">
    <h3>Dài hạn</h3>
    <ul>
    <li>Hỗ trợ đa ngôn ngữ</li>
    <li>Tích hợp chatbot pháp luật</li>
    <li>Phân tích và so sánh văn bản</li>
    <li>API cho ứng dụng khác</li>
    <li>Mobile app</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Contact/Info
st.info("""
💡 **Lưu ý:** Đây là hệ thống demo cho mục đích học tập và nghiên cứu. 
Để có thông tin pháp luật chính thức, vui lòng tham khảo các nguồn chính thức từ cơ quan nhà nước có thẩm quyền.
""")
