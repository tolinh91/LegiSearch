import streamlit as st

st.set_page_config(
    page_title="Tra cứu Luật",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Header
st.markdown('<h1 class="main-header">⚖️ Hệ thống Tra cứu Luật</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Hệ thống tra cứu văn bản pháp luật thông minh với tìm kiếm từ khóa và ngữ nghĩa</p>', unsafe_allow_html=True)

# Main content
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🔍 Tra cứu văn bản</h3>
        <p>Tìm kiếm các điều, khoản, chương trong văn bản pháp luật bằng từ khóa hoặc câu hỏi tự nhiên.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>❓ FAQ – Hỏi đáp</h3>
        <p>Xem các câu hỏi thường gặp về pháp luật và tìm câu trả lời nhanh chóng.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📘 Giới thiệu hệ thống</h3>
        <p>Tìm hiểu về mục tiêu, phạm vi và công nghệ của hệ thống tra cứu luật.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="feature-card">
        <h3>⚙️ Cài đặt</h3>
        <p>Tùy chỉnh cài đặt tìm kiếm và giao diện theo nhu cầu của bạn.</p>
    </div>
    """, unsafe_allow_html=True)

st.info("💡 **Bắt đầu:** Chọn chức năng từ menu bên trái để bắt đầu tra cứu.")
