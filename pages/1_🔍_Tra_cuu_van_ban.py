import streamlit as st
# from libs.search import keyword_search, semantic_search
# from libs.classifier import classify_query

st.set_page_config(
    page_title="Tra cứu Văn bản",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)



# Initialize session state
if 'search_mode' not in st.session_state:
    st.session_state.search_mode = 'auto'
if 'search_query' not in st.session_state:
    st.session_state.search_query = ''
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'selected_result' not in st.session_state:
    st.session_state.selected_result = None
if 'autocomplete_suggestions' not in st.session_state:
    st.session_state.autocomplete_suggestions = []

# Header
st.markdown('<div class="search-header"><h1>🔍 Tra cứu Văn bản pháp luật</h1></div>', unsafe_allow_html=True)

# Search Section
with st.container():
    st.markdown('<div class="search-container">', unsafe_allow_html=True)
    
    # Search input
    search_query = st.text_input(
        "Nhập từ khóa hoặc câu hỏi",
        value=st.session_state.search_query,
        placeholder="Ví dụ: 'Điều kiện cấp sổ đỏ', 'Tôi có được bồi thường khi thu hồi đất không?'",
        key="search_input",
        label_visibility="visible"
    )
    
    # Search mode selection
    st.markdown("**Chọn phương thức tìm kiếm:**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        keyword_selected = st.button("🔑 Tìm kiếm từ khóa", use_container_width=True, 
                                     type="primary" if st.session_state.search_mode == 'keyword' else "secondary")
        if keyword_selected:
            st.session_state.search_mode = 'keyword'
    
    with col2:
        semantic_selected = st.button("🧠 Tìm kiếm ngữ nghĩa", use_container_width=True,
                                     type="primary" if st.session_state.search_mode == 'semantic' else "secondary")
        if semantic_selected:
            st.session_state.search_mode = 'semantic'
    
    with col3:
        auto_selected = st.button("⚡ Tự động", use_container_width=True,
                                 type="primary" if st.session_state.search_mode == 'auto' else "secondary")
        if auto_selected:
            st.session_state.search_mode = 'auto'
    
    # Search button
    col_search1, col_search2, col_search3 = st.columns([1, 2, 1])
    with col_search2:
        search_button = st.button("🔍 Tìm kiếm", use_container_width=True, type="primary")
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Show current search mode
    mode_labels = {
        'keyword': '🔑 Tìm kiếm từ khóa',
        'semantic': '🧠 Tìm kiếm ngữ nghĩa',
        'auto': '⚡ Tự động (hệ thống quyết định)'
    }
    st.info(f"**Chế độ hiện tại:** {mode_labels[st.session_state.search_mode]}")

# if st.session_state.search_mode:
#     # Phân loại nếu ở chế độ Auto
#     if st.session_state.search_mode == "auto":
#         mode = "Keyword Search" if classify_query(st.session_state.search_query) == "keyword" else "Semantic Search"

#     st.info(f"🔎 Đang dùng chế độ: **{st.session_state.search_mode}**")

#     if st.session_state.search_mode == "keyword":
#         results = keyword_search(st.session_state.search_query)
#     elif st.session_state.search_mode == "semantic":
#         results = semantic_search(st.session_state.search_query)

#     st.subheader(f"📄 Kết quả tìm được: {len(results)}")

#     for i, r in enumerate(results):
#         with st.expander(f"📘 Điều {r['article']} — {r['title']}"):
#             st.write(r["preview"])
#             st.write("---")
#             st.markdown(f"**Nội dung đầy đủ:**\n\n{r['content']}")

# Instructions
with st.expander("ℹ️ Hướng dẫn sử dụng"):
    st.markdown("""
    **Cách sử dụng:**
    1. Nhập từ khóa hoặc câu hỏi vào ô tìm kiếm
    2. Chọn phương thức tìm kiếm:
       - **Tìm kiếm từ khóa**: Tìm chính xác các từ khóa trong văn bản
       - **Tìm kiếm ngữ nghĩa**: Hiểu ý nghĩa câu hỏi và tìm kết quả liên quan
       - **Tự động**: Hệ thống tự động chọn phương thức phù hợp
    3. Nhấn "Tìm kiếm" hoặc Enter
    4. Xem kết quả và nhấn "Xem chi tiết" để xem nội dung đầy đủ
    """)