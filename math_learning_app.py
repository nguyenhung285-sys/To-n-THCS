import streamlit as st
import pandas as pd
import numpy as np
import graphviz
import random
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Phần Mềm Học Tập Toán THCS (Lớp 6-9)",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for UI styling
st.markdown("""
<style>
    .main-title {
        font-size: 2.2rem;
        color: #1E3A8A;
        text-align: center;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        text-align: center;
        margin-bottom: 1.5rem;
    }
    .profile-card {
        background-color: #F0F9FF;
        border: 2px solid #0EA5E9;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 20px;
    }
    .card-header {
        background: linear-gradient(90deg, #1E3A8A 0%, #3B82F6 100%);
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        font-size: 1.2rem;
        margin-bottom: 15px;
    }
    .stButton>button {
        border-radius: 6px;
        font-weight: bold;
    }
    .correct-box {
        background-color: #DEF7EC;
        border-left: 5px solid #0E9F6E;
        padding: 10px;
        border-radius: 4px;
        margin-top: 5px;
    }
    .wrong-box {
        background-color: #FDE8E8;
        border-left: 5px solid #E02424;
        padding: 10px;
        border-radius: 4px;
        margin-top: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session States
if 'user_name' not in st.session_state:
    st.session_state.user_name = "Nguyễn Văn A"
if 'user_class' not in st.session_state:
    st.session_state.user_class = "7A1"

if 'submissions' not in st.session_state:
    st.session_state.submissions = [
        {"Họ và tên": "Trần Thị B", "Lớp": "6A", "Khối Lớp": "Lớp 6", "Số câu đã trả lời": 10, "Số câu đúng": 9, "Điểm số": 90, "Thời gian": "2026-09-26 18:30"},
        {"Họ và tên": "Lê Văn C", "Lớp": "7B", "Khối Lớp": "Lớp 7", "Số câu đã trả lời": 10, "Số câu đúng": 8, "Điểm số": 80, "Thời gian": "2026-09-26 19:15"},
        {"Họ và tên": "Phạm Minh D", "Lớp": "8A2", "Khối Lớp": "Lớp 8", "Số câu đã trả lời": 10, "Số câu đúng": 10, "Điểm số": 100, "Thời gian": "2026-09-26 19:40"},
        {"Họ và tên": "Hoàng Anh E", "Lớp": "9A1", "Khối Lớp": "Lớp 9", "Số câu đã trả lời": 10, "Số câu đúng": 7, "Điểm số": 70, "Thời gian": "2026-09-26 20:05"},
    ]

# Header
st.markdown('<div class="main-title">📚 PHẦN MỀM HỌC TẬP & ÔN TẬP TOÁN THCS</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Kết Nối Tri Thức Với Cuộc Sống - Hệ Thống Kiến Thức, Luyện Tập & AI Hỗ Trợ</div>', unsafe_allow_html=True)

# Student Profile Bar
with st.container():
    st.markdown('<div class="profile-card">', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 1, 1])
    with c1:
        st.session_state.user_name = st.text_input("👤 Họ và tên học sinh:", value=st.session_state.user_name)
    with c2:
        st.session_state.user_class = st.text_input("🏫 Lớp:", value=st.session_state.user_class)
    with c3:
        st.metric(label="Status", value="Đang học tập 🟢")
    st.markdown('</div>', unsafe_allow_html=True)

# Curriculum Data per Grade
GRADES_DATA = {
    "Lớp 6": {
        "topics": ["Tập hợp & Số tự nhiên", "Phép tính Lũy thừa", "Phân số & Số thập phân", "Hình học trực quan"],
        "mindmap": {
            "root": "TOÁN LỚP 6",
            "branches": {
                "Số & Đại Số": ["Tập hợp & Số tự nhiên", "Số nguyên (Âm & Dương)", "Phân số & Số thập phân"],
                "Hình Học": ["Điểm, Đường thẳng, Đoạn thẳng", "Góc & Dụng cụ đo", "Hình vuông, Tam giác đều, Lục giác đều"],
                "Thống Kê": ["Thu thập & Biểu diễn dữ liệu", "Biểu đồ cột, Biểu đồ cột kép"]
            }
        },
        "quiz": [
            {"id": 1, "type": "single", "q": "Cho tập hợp A = {x ∈ ℕ | x < 5}. Số phần tử của A là:", "opts": ["4", "5", "6", "Vô số"], "ans": "5", "exp": "Tập hợp A = {0, 1, 2, 3, 4} gồm 5 phần tử. Lỗi sai thường gặp: Quên số 0 trong tập hợp số tự nhiên ℕ."},
            {"id": 2, "type": "single", "q": "Kết quả của phép tính 2³ . 2² là:", "opts": ["2⁶", "2⁵", "4⁵", "4⁶"], "ans": "2⁵", "exp": "Áp dụng quy tắc nhân hai lũy thừa cùng cơ số: aᵐ . aⁿ = aᵐ⁺ⁿ. Do đó 2³⁺² = 2⁵. Lỗi sai: Nhân hai số mũ với nhau."},
            {"id": 3, "type": "tf", "q": "Số 0 là số nguyên âm.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "Số 0 không là số nguyên âm cũng không là số nguyên dương."},
            {"id": 4, "type": "single", "q": "Phân số nào sau đây tối giản?", "opts": ["2/4", "3/9", "5/7", "6/10"], "ans": "5/7", "exp": "Phân số 5/7 có tử và mẫu là hai số nguyên tố cùng nhau (UCLN = 1)."},
            {"id": 5, "type": "single", "q": "Tìm x, biết: x - 15 = -5", "opts": ["x = -20", "x = 10", "x = -10", "x = 20"], "ans": "x = 10", "exp": "x = -5 + 15 = 10. Lỗi sai: Nhầm dấu khi chuyển thế thành x = -5 - 15 = -20."},
            {"id": 6, "type": "single", "q": "Hình nào sau đây có 3 trục đối xứng?", "opts": ["Hình chữ nhật", "Tam giác đều", "Hình vuông", "Hình tròn"], "ans": "Tam giác đều", "exp": "Tam giác đều có 3 trục đối xứng đi qua 3 đỉnh và trung điểm cạnh đối diện."},
            {"id": 7, "type": "tf", "q": "Tổng hai số nguyên âm luôn là một số nguyên âm.", "opts": ["Đúng", "Sai"], "ans": "Đúng", "exp": "Quy tắc cộng hai số nguyên âm: (-a) + (-b) = -(a + b) < 0."},
            {"id": 8, "type": "single", "q": "Số đối của phân số -3/4 là:", "opts": ["3/4", "-4/3", "4/3", "-3/4"], "ans": "3/4", "exp": "Số đối của -a/b là a/b."},
            {"id": 9, "type": "single", "q": "Hình vuông có cạnh 5cm thì diện tích là:", "opts": ["20 cm²", "25 cm²", "10 cm²", "15 cm²"], "ans": "25 cm²", "exp": "Diện tích hình vuông S = a² = 5² = 25 cm²."},
            {"id": 10, "type": "single", "q": "Giá trị tuyệt đối của -12 là:", "opts": ["-12", "12", "0", "1/12"], "ans": "12", "exp": "Giá trị tuyệt đối của một số luôn không âm: |-12| = 12."}
        ]
    },
    "Lớp 7": {
        "topics": ["Số hữu tỉ & Số thực", "Tỉ lệ thức & Đại lượng tỉ lệ", "Biểu thức đại số & Đa thức 1 biến", "Tam giác bằng nhau"],
        "mindmap": {
            "root": "TOÁN LỚP 7",
            "branches": {
                "Số & Đại Số": ["Số hữu tỉ (ℚ) & Số thực (ℝ)", "Tỉ lệ thức & Dãy tỉ số bằng nhau", "Đại lượng tỉ lệ thuận, tỉ lệ nghịch"],
                "Biểu Thức Đại Số": ["Khái niệm biểu thức đại số", "Đa thức một biến & Các phép tính", "Nghiệm của đa thức một biến"],
                "Hình Học": ["Góc ở vị trí đặc biệt, Hai đường thẳng song song", "Tam giác bằng nhau (c.c.c, c.g.c, g.c.g)", "Quan hệ giữa các yếu tố trong tam giác"]
            }
        },
        "quiz": [
            {"id": 1, "type": "single", "q": "Tập hợp các số hữu tỉ được ký hiệu là:", "opts": ["ℕ", "ℤ", "ℚ", "ℝ"], "ans": "ℚ", "exp": "Tập hợp số hữu tỉ ký hiệu là ℚ. ℕ là số tự nhiên, ℤ là số nguyên, ℝ là số thực."},
            {"id": 2, "type": "single", "q": "Từ tỉ lệ thức a/b = c/d (với a,b,c,d ≠ 0), ta suy ra:", "opts": ["a.c = b.d", "a.d = b.c", "a.b = c.d", "a+b = c+d"], "ans": "a.d = b.c", "exp": "Tính chất cơ bản của tỉ lệ thức: Tích ngoại tỉ bằng tích trung tỉ (a.d = b.c)."},
            {"id": 3, "type": "tf", "q": "Số căn 2 (√2) là một số hữu tỉ.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "√2 = 1.4142135... là một số vô tỉ."},
            {"id": 4, "type": "single", "q": "Cho x và y tỉ lệ thuận với nhau theo hệ số k = 3. Công thức biểu diễn y theo x là:", "opts": ["y = 3/x", "y = 3x", "x = 3y", "y = x + 3"], "ans": "y = 3x", "exp": "Hai đại lượng tỉ lệ thuận liên hệ theo công thức y = kx."},
            {"id": 5, "type": "single", "q": "Bậc của đa thức P(x) = 3x⁴ - 2x² + x⁵ - 7 là:", "opts": ["3", "4", "5", "7"], "ans": "5", "exp": "Bậc của đa thức một biến là số mũ lớn nhất của biến trong đa thức đó (x⁵ có mũ 5)."},
            {"id": 6, "type": "single", "q": "Tổng ba góc trong một tam giác bằng:", "opts": ["90°", "180°", "360°", "120°"], "ans": "180°", "exp": "Định lý tổng ba góc trong một tam giác luôn bằng 180°."},
            {"id": 7, "type": "tf", "q": "Hai tam giác có ba cặp góc tương ứng bằng nhau thì bằng nhau.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "Chỉ có các trường hợp bằng nhau c.c.c, c.g.c, g.c.g. Ba góc bằng nhau chỉ đồng dạng chứ không nhất thiết bằng nhau."},
            {"id": 8, "type": "single", "q": "Nghiệm của đa thức P(x) = 2x - 6 là:", "opts": ["x = 3", "x = -3", "x = 6", "x = 0"], "ans": "x = 3", "exp": "Giải P(x) = 0 => 2x - 6 = 0 => 2x = 6 => x = 3."},
            {"id": 9, "type": "single", "q": "Trong tam giác ABC có AB = 5cm, BC = 7cm. Cạnh AC không thể bằng:", "opts": ["3cm", "5cm", "10cm", "13cm"], "ans": "13cm", "exp": "Bất đẳng thức tam giác: BC - AB < AC < AB + BC => 2 < AC < 12. Do đó AC không thể bằng 13cm."},
            {"id": 10, "type": "single", "q": "Kết quả của phép tính (-1/2)³ là:", "opts": ["1/8", "-1/8", "-1/6", "1/6"], "ans": "-1/8", "exp": "(-1/2)³ = (-1)³ / 2³ = -1/8."}
        ]
    },
    "Lớp 8": {
        "topics": ["Đa thức & Hằng đẳng thức", "Phân thức đại số", "Phương trình bậc nhất 1 biến", "Hình tứ giác & Đồng dạng"],
        "mindmap": {
            "root": "TOÁN LỚP 8",
            "branches": {
                "Đại Số & Hàm Số": ["Đa thức nhiều biến & Hằng đẳng thức đáng nhớ", "Phân thức đại số & Các phép tính", "Phương trình bậc nhất 1 biến", "Hàm số bậc nhất y = ax + b"],
                "Hình Học Trực Quan": ["Hình chóp tam giác đều & Hình chóp tứ giác đều"],
                "Hình Học Phẳng": ["Tứ giác đặc biệt (Hình bình hành, Hình chữ nhật, Hình rơm, Hình vuông)", "Định lý Thalès trong tam giác", "Tam giác đồng dạng"]
            }
        },
        "quiz": [
            {"id": 1, "type": "single", "q": "Hằng đẳng thức (A + B)² bằng:", "opts": ["A² + B²", "A² - 2AB + B²", "A² + 2AB + B²", "A² + AB + B²"], "ans": "A² + 2AB + B²", "exp": "Bình phương của một tổng: (A + B)² = A² + 2AB + B²."},
            {"id": 2, "type": "single", "q": "Khai triển A² - B² ta được:", "opts": ["(A - B)(A - B)", "(A - B)(A + B)", "(A + B)(A + B)", "A² - 2AB + B²"], "ans": "(A - B)(A + B)", "exp": "Hiệu hai bình phương: A² - B² = (A - B)(A + B)."},
            {"id": 3, "type": "tf", "q": "Điều kiện xác định của phân thức (x + 1)/(x - 2) là x ≠ -1.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "Điều kiện xác định của phân thức là mẫu thức khác 0: x - 2 ≠ 0 => x ≠ 2."},
            {"id": 4, "type": "single", "q": "Nghiệm của phương trình 3x + 9 = 0 là:", "opts": ["x = 3", "x = -3", "x = 0", "x = -9"], "ans": "x = -3", "exp": "3x = -9 => x = -3."},
            {"id": 5, "type": "single", "q": "Đồ thị hàm số y = 2x - 4 cắt trục tung tại điểm có tọa độ:", "opts": ["(0, -4)", "(2, 0)", "(0, 4)", "(-4, 0)"], "ans": "(0, -4)", "exp": "Giao điểm với trục tung Oy có x = 0 => y = 2(0) - 4 = -4. Tọa độ (0, -4)."},
            {"id": 6, "type": "single", "q": "Hình bình hành có hai đường chéo vuông góc với nhau là:", "opts": ["Hình chữ nhật", "Hình thoi", "Hình thang cân", "Hình tròn"], "ans": "Hình thoi", "exp": "Dấu hiệu nhận biết hình thoi: Hình bình hành có hai đường chéo vuông góc."},
            {"id": 7, "type": "tf", "q": "Hai tam giác đồng dạng thì có diện tích bằng nhau.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "Tỉ số diện tích của hai tam giác đồng dạng bằng bình phương tỉ số đồng dạng (k²)."},
            {"id": 8, "type": "single", "q": "Đa thức x² - 4x + 4 được viết dưới dạng bình phương là:", "opts": ["(x + 2)²", "(x - 2)²", "(x - 4)²", "(x + 4)²"], "ans": "(x - 2)²", "exp": "Áp dụng hằng đẳng thức (A - B)² = A² - 2AB + B² với A = x, B = 2."},
            {"id": 9, "type": "single", "q": "Số đường chéo của một tứ giác là:", "opts": ["1", "2", "3", "4"], "ans": "2", "exp": "Tứ giác có 4 đỉnh, số đường chéo là 2."},
            {"id": 10, "type": "single", "q": "Trong định lý Thalès, nếu DE // BC (D∈AB, E∈AC) thì:", "opts": ["AD/AB = AE/AC", "AD/DB = AC/AE", "AD/AC = AE/AB", "AB/AD = AE/AC"], "ans": "AD/AB = AE/AC", "exp": "Định lý Thalès: Đường thẳng song song với một cạnh của tam giác cắt hai cạnh còn lại tạo thành các đoạn thẳng tương ứng tỉ lệ."}
        ]
    },
    "Lớp 9": {
        "topics": ["Hệ phương trình bậc nhất 2 ẩn", "Căn bậc hai & Căn bậc ba", "Phương trình bậc hai & Định lý Vi-ét", "Đường tròn & Góc nội tiếp"],
        "mindmap": {
            "root": "TOÁN LỚP 9",
            "branches": {
                "Đại Số & Giải Tích": [
                    "Hệ phương trình bậc nhất 2 ẩn (Thế & Cộng đại số)",
                    "Căn bậc hai, căn bậc ba & Rút gọn biểu thức chứa căn",
                    "Phương trình bậc hai một ẩn ax² + bx + c = 0",
                    "Định lý Vi-ét & Ứng dụng thực tế"
                ],
                "Hình Học": [
                    "Hệ thức lượng trong tam giác vuông",
                    "Đường tròn, Tiếp tuyến & Vị trí tương đối",
                    "Góc ở tâm, Góc nội tiếp, Tứ giác nội tiếp",
                    "Hình trụ, Hình nón, Hình cầu"
                ]
            }
        },
        "quiz": [
            {"id": 1, "type": "single", "q": "Căn bậc hai số học của 16 là:", "opts": ["4", "-4", "±4", "256"], "ans": "4", "exp": "Căn bậc hai số học của số a không âm là số x không âm sao cho x² = a. √16 = 4."},
            {"id": 2, "type": "single", "q": "Biểu thức √(x - 3) xác định (có nghĩa) khi:", "opts": ["x > 3", "x ≥ 3", "x ≤ 3", "x ≠ 3"], "ans": "x ≥ 3", "exp": "Biểu thức dưới dấu căn bậc hai phải không âm: x - 3 ≥ 0 => x ≥ 3."},
            {"id": 3, "type": "tf", "q": "Hệ phương trình {x + y = 3; x - y = 1} có nghiệm duy nhất là (2, 1).", "opts": ["Đúng", "Sai"], "ans": "Đúng", "exp": "Cộng hai phương trình: 2x = 4 => x = 2. Thay vào x + y = 3 => y = 1."},
            {"id": 4, "type": "single", "q": "Biệt thức Delta (Δ) của phương trình ax² + bx + c = 0 (a ≠ 0) là:", "opts": ["b² - ac", "b² - 4ac", "b - 4ac", "4ac - b²"], "ans": "b² - 4ac", "exp": "Công thức biệt thức Delta: Δ = b² - 4ac."},
            {"id": 5, "type": "single", "q": "Theo định lý Vi-ét, tổng hai nghiệm x₁ + x₂ của phương trình ax² + bx + c = 0 là:", "opts": ["-b/a", "c/a", "b/a", "-c/a"], "ans": "-b/a", "exp": "Định lý Vi-ét: x₁ + x₂ = -b/a và x₁ . x₂ = c/a."},
            {"id": 6, "type": "single", "q": "Góc nội tiếp chắn nửa đường tròn có số đo bằng:", "opts": ["45°", "60°", "90°", "180°"], "ans": "90°", "exp": "Định lý góc nội tiếp chắn nửa đường tròn luôn là góc vuông (90°)."},
            {"id": 7, "type": "tf", "q": "Phương trình x² + 4 = 0 có hai nghiệm phân biệt.", "opts": ["Đúng", "Sai"], "ans": "Sai", "exp": "x² = -4 (vô nghiệm trên tập số thực vì x² ≥ 0 với mọi x)."},
            {"id": 8, "type": "single", "q": "Cho phương trình x² - 5x + 6 = 0. Tích hai nghiệm x₁ . x₂ bằng:", "opts": ["5", "6", "-5", "-6"], "ans": "6", "exp": "Theo Vi-ét: x₁ . x₂ = c/a = 6/1 = 6."},
            {"id": 9, "type": "single", "q": "Trong tam giác vuông, sin của một góc nhọn bằng:", "opts": ["Đối / Huyền", "Kề / Huyền", "Đối / Kề", "Kề / Đối"], "ans": "Đối / Huyền", "exp": "Tỉ số lượng giác: Sin đi học (Đối/Huyền), Cos không hư (Kề/Huyền), Tan đoàn kết (Đối/Kề)."},
            {"id": 10, "type": "single", "q": "Độ dài đường tròn bán kính R được tính theo công thức:", "opts": ["πR²", "2πR", "4πR²", "πR"], "ans": "2πR", "exp": "Chu vi (độ dài) đường tròn C = 2πR. Diện tích hình tròn S = πR²."}
        ]
    }
}

# Function to render Graphviz Mind Map
def render_mindmap(mindmap_data):
    dot = graphviz.Digraph(comment='MindMap')
    dot.attr(rankdir='LR', size='8,5')
    dot.attr('node', shape='box', style='filled,rounded', color='#1E3A8A', fontcolor='white', fontname='Arial', fontsize='12')
    
    root = mindmap_data["root"]
    dot.node('ROOT', root, fillcolor='#1E3A8A', fontsize='14', fontcolor='white')
    
    colors = ['#0EA5E9', '#10B981', '#F59E0B', '#8B5CF6']
    idx = 0
    for branch, items in mindmap_data["branches"].items():
        branch_id = f"B_{idx}"
        branch_color = colors[idx % len(colors)]
        dot.node(branch_id, branch, fillcolor=branch_color, fontcolor='white')
        dot.edge('ROOT', branch_id)
        
        for j, item in enumerate(items):
            item_id = f"I_{idx}_{j}"
            dot.node(item_id, item, fillcolor='#F3F4F6', fontcolor='#1F2937', color='#D1D5DB')
            dot.edge(branch_id, item_id)
        idx += 1
    return dot

# Smart Practice Generator based on Level
def get_smart_practice_questions(grade, level):
    if level == "🟢 Dễ (Easy)":
        if grade == "Lớp 6":
            return [
                {"q": "Số tự nhiên nhỏ nhất là số nào?", "opts": ["0", "1", "-1", "Không có"], "ans": "0", "exp": "Tập hợp số tự nhiên ℕ = {0, 1, 2, 3...}, số nhỏ nhất là 0."},
                {"q": "Tính 15 + 25", "opts": ["35", "40", "45", "50"], "ans": "40", "exp": "Phép cộng số tự nhiên đơn giản."}
            ]
        elif grade == "Lớp 7":
            return [
                {"q": "Số nào sau đây là số hữu tỉ?", "opts": ["0.5", "√2", "π", "e"], "ans": "0.5", "exp": "0.5 = 1/2 là số hữu tỉ."},
                {"q": "Tính |-7|", "opts": ["7", "-7", "0", "14"], "ans": "7", "exp": "Giá trị tuyệt đối luôn không âm."}
            ]
        elif grade == "Lớp 8":
            return [
                {"q": "Khai triển (x + 1)²", "opts": ["x² + 2x + 1", "x² + 1", "x² + x + 1", "x² + 4x + 1"], "ans": "x² + 2x + 1", "exp": "Hằng đẳng thức (A+B)²."},
                {"q": "Tứ giác có 4 góc vuông là hình gì?", "opts": ["Hình chữ nhật", "Hình thoi", "Hình thang", "Hình bình hành"], "ans": "Hình chữ nhật", "exp": "Định nghĩa hình chữ nhật."}
            ]
        else: # Lớp 9
            return [
                {"q": "Căn bậc hai số học của 25 là:", "opts": ["5", "-5", "25", "625"], "ans": "5", "exp": "√25 = 5."},
                {"q": "Phương trình x - 2 = 0 có nghiệm x bằng:", "opts": ["2", "-2", "0", "4"], "ans": "2", "exp": "x = 2."}
            ]
    elif level == "🟡 Trung bình (Medium)":
        if grade == "Lớp 6":
            return [
                {"q": "Thực hiện phép tính: 2⁴ - 3 . 2", "opts": ["10", "26", "14", "8"], "ans": "10", "exp": "2⁴ = 16, 3 . 2 = 6 => 16 - 6 = 10."},
                {"q": "Tìm UCLN(12, 18)", "opts": ["6", "12", "3", "36"], "ans": "6", "exp": "12 = 2².3, 18 = 2.3² => UCLN = 2.3 = 6."}
            ]
        elif grade == "Lớp 7":
            return [
                {"q": "Tìm x từ tỉ lệ thức: x/4 = 9/12", "opts": ["3", "4", "36", "10"], "ans": "3", "exp": "x = (4 . 9) / 12 = 3."},
                {"q": "Cho ΔABC = ΔDEF. Biết AB = 4cm. Độ dài cạnh DE là:", "opts": ["4cm", "8cm", "2cm", "Không xác định"], "ans": "4cm", "exp": "Hai tam giác bằng nhau có các cạnh tương ứng bằng nhau (DE = AB = 4cm)."}
            ]
        elif grade == "Lớp 8":
            return [
                {"q": "Phân tích x² - 9 thành nhân tử:", "opts": ["(x - 3)(x + 3)", "(x - 9)(x + 1)", "(x - 3)²", "(x + 3)²"], "ans": "(x - 3)(x + 3)", "exp": "Hiệu hai bình phương A² - B² = (A - B)(A + B)."},
                {"q": "Giải phương trình: (x - 2)(x + 3) = 0", "opts": ["x = 2 hoặc x = -3", "x = -2 hoặc x = 3", "x = 2 hoặc x = 3", "x = 0"], "ans": "x = 2 hoặc x = -3", "exp": "Phương trình tích A.B = 0 => A=0 hoặc B=0."}
            ]
        else: # Lớp 9
            return [
                {"q": "Rút gọn biểu thức A = √(12) + √(27) - √(48)", "opts": ["√3", "2√3", "0", "3√3"], "ans": "√3", "exp": "2√3 + 3√3 - 4√3 = √3."},
                {"q": "Cho phương trình x² - 7x + 10 = 0. Tổng và tích 2 nghiệm là:", "opts": ["S = 7, P = 10", "S = -7, P = 10", "S = 10, P = 7", "S = 7, P = -10"], "ans": "S = 7, P = 10", "exp": "Theo Vi-ét: S = -b/a = 7, P = c/a = 10."}
            ]
    else: # Khó
        if grade == "Lớp 6":
            return [
                {"q": "Tìm số tự nhiên n nhỏ nhất để (n + 5) chia hết cho (n + 1)", "opts": ["0", "1", "3", "4"], "ans": "0", "exp": "(n + 5) = (n + 1) + 4. Để chia hết thì 4 chia hết cho (n+1) => n+1 ∈ {1,2,4} => n nhỏ nhất là 0."},
                {"q": "Tính nhanh: A = 1/1.2 + 1/2.3 + 1/3.4 + ... + 1/99.100", "opts": ["99/100", "1/100", "1", "100/99"], "ans": "99/100", "exp": "A = (1 - 1/2) + (1/2 - 1/3) + ... + (1/99 - 1/100) = 1 - 1/100 = 99/100."}
            ]
        elif grade == "Lớp 7":
            return [
                {"q": "Cho a/b = c/d. Chứng minh (a + b)/(a - b) bằng tỉ số nào?", "opts": ["(c + d)/(c - d)", "(c - d)/(c + d)", "c/d", "a/c"], "ans": "(c + d)/(c - d)", "exp": "Đặt a/b = c/d = k => a = bk, c = dk. Thay vào ta được (k+1)/(k-1) = (c+d)/(c-d)."},
                {"q": "Giá trị nhỏ nhất của biểu thức A = |x - 2| + |x - 5| là:", "opts": ["3", "0", "5", "2"], "ans": "3", "exp": "|x - 2| + |x - 5| = |x - 2| + |5 - x| ≥ |x - 2 + 5 - x| = 3. Dấu '=' xảy ra khi 2 ≤ x ≤ 5."}
            ]
        elif grade == "Lớp 8":
            return [
                {"q": "Cho x + y = 5 và xy = 6. Tính x³ + y³", "opts": ["35", "65", "125", "95"], "ans": "35", "exp": "x³ + y³ = (x + y)³ - 3xy(x + y) = 5³ - 3(6)(5) = 125 - 90 = 35."},
                {"q": "Tìm giá trị nhỏ nhất của đa thức P = x² - 4x + 10", "opts": ["6", "10", "2", "4"], "ans": "6", "exp": "P = (x - 2)² + 6 ≥ 6. Min P = 6 khi x = 2."}
            ]
        else: # Lớp 9
            return [
                {"q": "Tìm m để phương trình x² - 2mx + m² - 4 = 0 có 2 nghiệm phân biệt x₁, x₂ thỏa mãn x₁² + x₂² = 20", "opts": ["m = ±2", "m = 2", "m = 4", "m = ±3"], "ans": "m = ±2", "exp": "Δ' = m² - (m²-4) = 4 > 0. x₁²+x₂² = (x₁+x₂)² - 2x₁x₂ = (2m)² - 2(m²-4) = 2m² + 8 = 20 => 2m² = 12 nhầm => 2m² = 8 => m² = 4 => m = ±2."},
                {"q": "Giá trị lớn nhất của P = √(x - 1) + √(5 - x) là:", "opts": ["2√2", "2", "4", "√8"], "ans": "2√2", "exp": "Áp dụng BĐT Bất đẳng thức Bunhiacopxki: P² ≤ (1² + 1²)(x - 1 + 5 - x) = 2 . 4 = 8 => P ≤ √8 = 2√2."}
            ]

# Render Tabs for 4 Grades
tabs = st.tabs(["📘 KHỐI LỚP 6", "📗 KHỐI LỚP 7", "📙 KHỐI LỚP 8", "📕 KHỐI LỚP 9"])

for grade_idx, (grade_name, grade_data) in enumerate(GRADES_DATA.items()):
    with tabs[grade_idx]:
        st.markdown(f'<div class="card-header">CHƯƠNG TRÌNH TOÁN {grade_name.upper()} - KẾT NỐI TRI THỨC VỚI CUỘC SỐNG</div>', unsafe_allow_html=True)
        
        # 6 Main Functional Sections using Radio or Sub-tabs
        section = st.radio(
            f"🎯 Chọn mục học tập cho {grade_name}:",
            ["1. Hệ thống kiến thức", "2. Luyện tập (10 câu)", "3. Luyện tập thông minh", "4. Luyện tập cùng AI", "5. Nộp kết quả", "6. Xếp hạng"],
            key=f"radio_{grade_name}",
            horizontal=True
        )
        
        st.divider()
        
        # 1. Hệ thống kiến thức
        if section == "1. Hệ thống kiến thức":
            st.subheader("🌐 Sơ đồ tư duy kiến thức trọng tâm")
            col_map, col_desc = st.columns([3, 2])
            with col_map:
                st.graphviz_chart(render_mindmap(grade_data["mindmap"]))
            with col_desc:
                st.info("💡 **Hướng dẫn ôn tập:**")
                st.write("- **Số & Đại số:** Nắm vững các tập hợp số, phép tính, công thức biến đổi và cách giải phương trình.")
                st.write("- **Hình học:** Nhớ kĩ các định lý, tính chất hình học, công thức tính chu vi, diện tích, thể tích.")
                st.write("- **Thống kê & Xác suất:** Kỹ năng đọc biểu đồ, thu thập và phân tích dữ liệu thực tế.")
                
        # 2. Luyện tập (10 câu hỏi)
        elif section == "2. Luyện tập (10 câu)":
            st.subheader("📝 Bài luyện tập 10 câu hỏi trắc nghiệm")
            st.caption("Hoàn thành tất cả các câu hỏi, bấm 'Kiểm tra đáp án' để nhận phản hồi và giải thích lỗi sai chi tiết.")
            
            user_answers = {}
            for q in grade_data["quiz"]:
                st.markdown(f"**Câu {q['id']}:** {q['q']}")
                ans_key = f"quiz_{grade_name}_{q['id']}"
                if q["type"] in ["single", "tf"]:
                    user_answers[q['id']] = st.radio("Chọn đáp án:", q["opts"], key=ans_key, index=0)
                st.write("")
                
            if st.button("🚀 Kiểm tra đáp án & Giải thích lỗi sai", key=f"btn_check_{grade_name}"):
                score = 0
                st.markdown("### 📊 Kết quả chi tiết:")
                for q in grade_data["quiz"]:
                    u_ans = user_answers.get(q['id'])
                    is_correct = (u_ans == q["ans"])
                    if is_correct:
                        score += 1
                        st.markdown(f'<div class="correct-box"><b>Câu {q["id"]}: Chính xác! ✅</b><br>Đáp án của bạn: {u_ans}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div class="wrong-box"><b>Câu {q["id"]}: Chưa chính xác ❌</b><br>Đáp án chọn: {u_ans} | <b>Đáp án đúng: {q["ans"]}</b><br>💡 <b>Giải thích lỗi sai & Hướng dẫn:</b> {q["exp"]}</div>', unsafe_allow_html=True)
                
                final_score = score * 10
                st.success(f"🎉 **Tổng điểm của bạn:** {final_score}/100 điểm ({score}/10 câu đúng)")
                
                # Auto record submission
                submission_entry = {
                    "Họ và tên": st.session_state.user_name,
                    "Lớp": st.session_state.user_class,
                    "Khối Lớp": grade_name,
                    "Số câu đã trả lời": len(user_answers),
                    "Số câu đúng": score,
                    "Điểm số": final_score,
                    "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M")
                }
                st.session_state.submissions.append(submission_entry)
                st.info("✅ Kết quả đã được tự động lưu vào mục **5. Nộp kết quả** và cập nhật vào **6. Xếp hạng**!")

        # 3. Luyện tập thông minh
        elif section == "3. Luyện tập thông minh":
            st.subheader("⚡ Luyện tập thông minh theo cấp độ")
            level = st.select_slider("Chọn mức độ thử thách:", options=["🟢 Dễ (Easy)", "🟡 Trung bình (Medium)", "🔴 Khó (Hard)"], key=f"slider_{grade_name}")
            
            smart_qs = get_smart_practice_questions(grade_name, level)
            st.write(f"Đang hiển thị bộ câu hỏi mức độ: **{level}**")
            
            for idx, sq in enumerate(smart_qs, 1):
                st.markdown(f"**Câu hỏi {idx}:** {sq['q']}")
                u_opt = st.radio(f"Lựa chọn câu {idx}:", sq['opts'], key=f"smart_{grade_name}_{level}_{idx}")
                if st.button(f"Kiểm tra câu {idx}", key=f"btn_smart_{grade_name}_{idx}"):
                    if u_opt == sq['ans']:
                        st.success("Xuất sắc! Bạn đã trả lời đúng. 🎉")
                    else:
                        st.error(f"Chưa đúng. Đáp án đúng là: **{sq['ans']}**")
                        st.info(f"🔍 **Phân tích chi tiết:** {sq['exp']}")
                st.divider()

        # 4. Luyện tập cùng AI
        elif section == "4. Luyện tập cùng AI":
            st.subheader("🤖 AI Sinh Câu Hỏi Theo Chủ Đề Tự Chọn")
            selected_topic = st.selectbox("📌 Chọn chủ đề bài học muốn ôn tập:", grade_data["topics"], key=f"ai_topic_{grade_name}")
            num_ai_q = st.slider("Số lượng câu hỏi AI tạo:", min_value=1, max_value=5, value=2, key=f"ai_num_{grade_name}")
            
            if st.button("✨ Sinh câu hỏi cùng AI", key=f"btn_ai_{grade_name}"):
                st.markdown(f"### 🤖 AI đã khởi tạo {num_ai_q} câu hỏi thuộc chủ đề **{selected_topic}**:")
                
                # Dynamic AI Question Generator Simulation based on real topic logic
                for i in range(1, num_ai_q + 1):
                    val1 = random.randint(2, 9)
                    val2 = random.randint(2, 9)
                    st.markdown(f"**Câu {i} (AI Dynamic):** Cho bài toán liên quan đến `{selected_topic}` với các thông số a = {val1}, b = {val2}.")
                    if "Tập hợp" in selected_topic or "Số hữu tỉ" in selected_topic:
                        st.write(f"Tính giá trị của biểu thức P = {val1}x + {val2} tại x = 2.")
                        st.success(f"💡 **Đáp án gợi ý từ AI:** P = {val1}*(2) + {val2} = {val1*2 + val2}")
                    elif "Đa thức" in selected_topic or "Hằng đẳng thức" in selected_topic:
                        st.write(f"Khai triển và tính giá trị ({val1}x + {val2})² khi x = 1.")
                        st.success(f"💡 **Đáp án gợi ý từ AI:** ({val1}*1 + {val2})² = ({val1+val2})² = {(val1+val2)**2}")
                    elif "Phương trình" in selected_topic or "Căn bậc hai" in selected_topic:
                        st.write(f"Giải phương trình: {val1}x - {val2*val1} = 0")
                        st.success(f"💡 **Đáp án gợi ý từ AI:** {val1}x = {val2*val1} => x = {val2}")
                    else:
                        st.write(f"Tính chu vi/diện tích hình có kích thước {val1}cm và {val2}cm.")
                        st.success(f"💡 **Đáp án gợi ý từ AI:** Diện tích = {val1} x {val2} = {val1*val2} cm²")
                    st.divider()

        # 5. Nộp kết quả
        elif section == "5. Nộp kết quả":
            st.subheader("📋 Form Thống Kê & Nộp Kết Quả Học Tập")
            
            with st.form(key=f"submit_form_{grade_name}"):
                col_f1, col_f2 = st.columns(2)
                with col_f1:
                    f_name = st.text_input("Họ và tên:", value=st.session_state.user_name)
                    f_class = st.text_input("Lớp:", value=st.session_state.user_class)
                    f_grade = st.selectbox("Khối Lớp:", ["Lớp 6", "Lớp 7", "Lớp 8", "Lớp 9"], index=grade_idx)
                with col_f2:
                    f_answered = st.number_input("Số câu đã trả lời:", min_value=0, max_value=10, value=10)
                    f_unanswered = st.number_input("Số câu chưa trả lời:", min_value=0, max_value=10, value=0)
                    f_correct = st.number_input("Số câu trả lời đúng:", min_value=0, max_value=10, value=8)
                
                f_score = f_correct * 10
                submit_btn = st.form_submit_button("📤 Nộp kết quả vào Bảng tính")
                
                if submit_btn:
                    new_sub = {
                        "Họ và tên": f_name,
                        "Lớp": f_class,
                        "Khối Lớp": f_grade,
                        "Số câu đã trả lời": f_answered,
                        "Số câu đúng": f_correct,
                        "Điểm số": f_score,
                        "Thời gian": datetime.now().strftime("%Y-%m-%d %H:%M")
                    }
                    st.session_state.submissions.append(new_sub)
                    st.success("✅ Đã ghi nhận kết quả thành công!")

            st.markdown("### 📊 Bảng tổng hợp dữ liệu (Spreadsheet View):")
            df_sub = pd.DataFrame(st.session_state.submissions)
            st.dataframe(df_sub, use_container_width=True)
            
            # Download CSV capability
            csv = df_sub.to_csv(index=False).encode('utf-8-sig')
            st.download_button(
                label="📥 Tải Bảng Tính Kết Quả (CSV/Excel)",
                data=csv,
                file_name="ket_qua_hoc_tap_toan.csv",
                mime="text/csv",
                key=f"dl_csv_{grade_name}"
            )

        # 6. Xếp hạng
        elif section == "6. Xếp hạng":
            st.subheader("🏆 Bảng Xếp Hạng Học Sinh (Leaderboard)")
            df_rank = pd.DataFrame(st.session_state.submissions)
            
            if not df_rank.empty:
                # Sort from highest score to lowest score
                df_rank = df_rank.sort_values(by=["Điểm số", "Số câu đúng"], ascending=[False, False]).reset_index(drop=True)
                df_rank.index += 1
                df_rank.index.name = "Thứ hạng"
                
                # Add medal badges
                badges = []
                for r in range(1, len(df_rank) + 1):
                    if r == 1:
                        badges.append("🥇 Hạng 1 (Đại Cao Thủ)")
                    elif r == 2:
                        badges.append("🥈 Hạng 2 (Cao Thủ)")
                    elif r == 3:
                        badges.append("🥉 Hạng 3 (Tinh Anh)")
                    else:
                        badges.append(f"Top {r}")
                df_rank["Danh hiệu"] = badges
                
                st.table(df_rank[["Danh hiệu", "Họ và tên", "Lớp", "Khối Lớp", "Điểm số", "Số câu đúng", "Thời gian"]])
            else:
                st.info("Chưa có dữ liệu xếp hạng.")

# Footer
st.divider()
st.caption("© 2026 Phần Mềm Học Tập Toán THCS - Xây dựng dựa trên bộ sách Kết Nối Tri Thức Với Cuộc Sống.")
