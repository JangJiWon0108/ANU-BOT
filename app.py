# import streamlit as st

# # 현재 페이지 콘텐츠
# st.title("현재 페이지")

# # 새로운 페이지 URL (여기서는 예시로 'https://example.com' 사용)
# new_page_url = "https://example.com"

# # 버튼을 클릭할 때 새 탭에서 열도록 하는 HTML 및 JavaScript
# st.markdown(
#     f"""
#     <a href="{new_page_url}" target="_blank">
#         <button style="padding: 10px 20px; font-size: 16px;">새 페이지 열기</button>
#     </a>
#     """,
#     unsafe_allow_html=True
# )

import streamlit as st
import subprocess

def run_other_app():
    subprocess.Popen(["streamlit", "run", "anu_bot.py"])

st.title("현재 페이지")

a=4

if a==4:
    if st.button("다른 앱 실행"):
        run_other_app()
        st.write("다른 앱을 실행했습니다.")