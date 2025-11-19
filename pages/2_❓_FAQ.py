import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="FAQ",
    page_icon="❓",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Header
# st.markdown('<div class="faq-header"><h1>❓ FAQ – Hỏi đáp pháp luật</h1></div>', unsafe_allow_html=True)
st.title("❓ FAQ – Hỏi đáp pháp luật")

# Mock FAQ data (replace with actual CSV reading if file exists)
try:
    faq_df = pd.read_csv("data/faq.csv")
except:
    # Create mock data if CSV doesn't exist
    faq_data = {
        'question': [
            'Điều kiện để được cấp sổ đỏ là gì?',
            'Tôi có được bồi thường khi Nhà nước thu hồi đất không?',
            'Thủ tục cấp Giấy chứng nhận quyền sử dụng đất mất bao lâu?',
            'Khi nào cần làm thủ tục chuyển nhượng quyền sử dụng đất?',
            'Chi phí cấp sổ đỏ là bao nhiêu?',
            'Có thể cấp sổ đỏ cho đất không có giấy tờ không?',
            'Quyền sử dụng đất có được thừa kế không?',
            'Thời hạn sử dụng đất là bao lâu?'
        ],
        'answer': [
            'Để được cấp sổ đỏ, bạn cần đáp ứng các điều kiện: có đủ giấy tờ về quyền sử dụng đất, đất không có tranh chấp, quyền sử dụng đất không bị kê biên, và đang sử dụng đất ổn định (theo Điều 75).',
            'Có, khi Nhà nước thu hồi đất vì mục đích quốc phòng, an ninh, phát triển kinh tế - xã hội, bạn sẽ được bồi thường về đất, tài sản gắn liền với đất và được hỗ trợ khi thu hồi đất (theo Điều 50).',
            'Thời gian xử lý hồ sơ cấp Giấy chứng nhận quyền sử dụng đất thường từ 30-60 ngày làm việc kể từ ngày nhận đủ hồ sơ hợp lệ, tùy thuộc vào từng địa phương.',
            'Bạn cần làm thủ tục chuyển nhượng quyền sử dụng đất khi muốn chuyển quyền sử dụng đất cho người khác. Thủ tục bao gồm: hợp đồng chuyển nhượng, nộp hồ sơ tại cơ quan có thẩm quyền và đóng các loại phí, lệ phí theo quy định.',
            'Chi phí cấp sổ đỏ bao gồm: lệ phí cấp giấy chứng nhận, phí thẩm định hồ sơ, phí đo đạc địa chính (nếu chưa có). Tổng chi phí thường từ 500.000 - 2.000.000 VNĐ tùy thuộc vào diện tích và loại đất.',
            'Có thể, nhưng cần có đủ điều kiện theo quy định. Đối với đất không có giấy tờ, bạn cần chứng minh việc sử dụng đất ổn định, không có tranh chấp và phù hợp với quy hoạch sử dụng đất.',
            'Có, quyền sử dụng đất có thể được thừa kế theo quy định của pháp luật về thừa kế. Người thừa kế sẽ được cấp Giấy chứng nhận quyền sử dụng đất sau khi hoàn tất thủ tục thừa kế.',
            'Thời hạn sử dụng đất tùy thuộc vào loại đất: đất ở có thời hạn lâu dài, đất nông nghiệp thường có thời hạn 50 năm, đất thương mại dịch vụ có thời hạn 50-70 năm. Sau khi hết hạn, có thể được gia hạn nếu đáp ứng điều kiện.'
        ],
        'category': [
            'Cấp sổ đỏ',
            'Thu hồi đất',
            'Cấp sổ đỏ',
            'Chuyển nhượng',
            'Chi phí',
            'Cấp sổ đỏ',
            'Thừa kế',
            'Thời hạn'
        ]
    }
    faq_df = pd.DataFrame(faq_data)
st.dataframe(faq_df)

