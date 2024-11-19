# jumpit_wanted_review_page.py
# 점핏, 원티드 회사 리뷰 관련 파일

# ================================================= 라이브러리 ==============================================
from konlpy.tag import Okt
from gensim import corpora
from gensim.models import LdaModel
from collections import Counter
import re
import streamlit as st
import pandas as pd
from PIL import Image
import io
import base64
import matplotlib.pyplot as plt
# 로깅 설정: 정보성 메시지를 출력
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# ================================================= 함수 ==============================================
def image_to_base64(image_path):
    """이미지 파일을 Base64로 인코딩하여 반환합니다."""
    with open(image_path, "rb") as img_file:
        # 이미지를 Base64로 인코딩
        encoded_string = base64.b64encode(img_file.read()).decode()
    return encoded_string

def display_image_from_base64(base64_string):
    """Base64로 인코딩된 이미지를 Streamlit에서 표시합니다."""
    # Base64 문자열을 HTML로 변환
    image_html = f'''
    <div style="text-align: left; width: 100%; overflow: hidden;">
        <img src="data:image/jpeg;base64,{base64_string}" style="width: 1000px; max-width: 100%; height: auto;">
    </div>
    '''
    st.markdown(image_html, unsafe_allow_html=True)

# ================================================= 전역변수 ==============================================
number_list=["1️⃣", "2️⃣", "3️⃣"] # 숫자 이모지

# ========================================= CSS 스타일 정의 ==============================================
css = """
    <style>    
    .scrollable-container {
        max-height: 120px; /* 스크롤 가능한 영역의 최대 높이 설정 */
        overflow-y: scroll;
        border: 1px solid #ddd;
        gap: 1px; /* 텍스트와 스크롤바 사이의 간격 */
        margin: 0; /* 스크롤 가능한 영역과 다른 요소 사이의 여백 설정 */
        font-size: 10px; /* 텍스트 글씨 크기 조정 */
    }
    .text-item {
        padding: 0px 0; /* 구분선과 텍스트 사이의 여백 설정 */
    }
    .text-item:last-child {
        border-bottom: none; /* 마지막 문장에는 구분선 없음 */
    }
    .divider {
        border-bottom: 1px solid #ddd; /* 구분선 스타일 */
        margin: 15px 0; /* 구분선 위아래 간격 조정 */
    }
    .left-align-img {
        display: block; /* 블록 요소로 만들어서 정렬 설정 */
        margin: 0; /* 기본 여백 제거 */
        width: 100%; /* 이미지의 너비를 컨테이너에 맞게 조정 */
        max-width: 1000px; /* 이미지의 최대 너비 설정 (여기서는 예를 들어 1000px) */
    }
"""

# ========================================= 데이터 로딩 ==============================================
jumpit_wanted_drop=pd.read_csv("dataset/점핏_원티드_리뷰_중복제거_(별점,연봉,한줄요약)_streamlit(final).csv")
df_advantage=pd.read_csv("dataset/점핏_원티드_리뷰_토픽모델링_장점(fianl).csv")
df_disadvantage=pd.read_csv("dataset/점핏_원티드_리뷰_토픽모델링_단점(fianl).csv")
df_word_cloud=pd.read_csv("dataset/회사 워드클라우드.csv")
df_type=pd.read_csv("dataset/회사업종.csv") # 업종

# ========================================= 회사명 선택하는 코드 추가 ==============================================
# 샘플로 딥노이드가 선택되었다는 가정
junmpit_wanted_name=["딥노이드"]


# ========================================= 회사명으로 필터링 ==============================================
df_info_factory=jumpit_wanted_drop[jumpit_wanted_drop["회사명"]==junmpit_wanted_name[0]]
df_advantage_factory=df_advantage[df_advantage["회사명"]==junmpit_wanted_name[0]]
df_disadvantage_factory=df_disadvantage[df_disadvantage["회사명"]==junmpit_wanted_name[0]]
df_word_cloud_factory=df_word_cloud[df_word_cloud["회사명"]=="딥노이드"]  # 현재 워드클라우드가 딥노이드밖에 이렇게 설정함 (바꿔야함)
df_type_factory=df_type[df_type["회사명"]==junmpit_wanted_name[0]]

# ====================================== 워드클라우드 이미지 경로 뽑기==============================================
current_word_cloud_path_advantage=df_word_cloud_factory["워클_장점"].values[0]
current_word_cloud_path_disadvantage=df_word_cloud_factory["워클_단점"].values[0]

# ====================================== 페이지 설정==============================================
st.set_page_config(page_title="{}".format(junmpit_wanted_name[0]), layout="wide")


# ====================================== HTML과 CSS를 스트림릿에 표시 ====================================== 
st.markdown(css, unsafe_allow_html=True)


#======================================  회사명 출력 ====================================== 
st.title("🌟"+df_info_factory["회사명"].values[0]) # 제목

# ====================================== 업종 출력 ====================================== 
st.markdown(f"""
    <style>
        .highlight-background {{
            background-color: #F0A0E6; /* 배경색 (그린) */
            padding: 10px; /* 텍스트와 배경 사이의 패딩 */
            border-radius: 5px; /* 모서리 둥글게 */
            display: inline; /* 배경색이 텍스트에만 적용되도록 */
        }}
    </style>
    <div>
        <span><h3></span><span class="highlight-background">{df_type_factory["업종"].values[0]}</h3></span>
    </div>
    <br>
""", unsafe_allow_html=True)


# ======================================  리뷰 한줄 요약, 평균 별점, 평균 연봉 표시 (바) ====================================== 
with st.expander("회사 요약 정보"):
    st.markdown(f"""
        <style>
            .highlight-background-red {{
                background-color: #FFD7D0; /* 배경색 (파스텔 레드) */
                padding: 10px; /* 텍스트와 배경 사이의 패딩 */
                border-radius: 5px; /* 모서리 둥글게 */
                display: inline; /* 배경색이 텍스트에만 적용되도록 */
            }}
        </style>
        <div>
            <span>❤️<b>리뷰 한줄 요약</b>❤️ </span><span class="highlight-background-red">{df_info_factory["한줄 요약"].values[0]}</span>
        </div>
        <br>
    """, unsafe_allow_html=True)
    st.markdown(f"""
        <style>
            .highlight-background-green {{
                background-color: #B3FFBE; /* 배경색 (파스텔 그린) */
                padding: 10px; /* 텍스트와 배경 사이의 패딩 */
                border-radius: 5px; /* 모서리 둥글게 */
                display: inline; /* 배경색이 텍스트에만 적용되도록 */
            }}
        </style>
        <div>
            <span>💚<b>평균 별점</b>💚 </span><span class="highlight-background-green">{df_info_factory["평균별점"].values[0]} / 5</span>
        </div>
        <br>
    """, unsafe_allow_html=True)

    st.markdown(f"""
        <style>
            .highlight-background-blue {{
                background-color: #CBE7FE; /* 배경색 (파스텔 블루) */
                padding: 10px; /* 텍스트와 배경 사이의 패딩 */
                border-radius: 5px; /* 모서리 둥글게 */
                display: inline; /* 배경색이 텍스트에만 적용되도록 */
            }}
        </style>
        <div>
            <span>💙<b>평균 연봉</b>💙 </span><span class="highlight-background-blue">{df_info_factory["평균연봉"].values[0]}</span>
        </div>
        <br>
    """, unsafe_allow_html=True)

# ====================================== 줄바꿈 ====================================== 
st.markdown("<br>", unsafe_allow_html=True)

# ======================================  탭 만들기 ====================================== 
tabs = st.tabs(["워드 클라우드🍧", "토픽 모델링🍩"])


# ====================================== 워드 클라우드 탭 ====================================== 
with tabs[0]:
    # 열 비율 설정
    title_col1, title_col2 = st.columns([1, 1])

    # 장점
    with title_col1:
        st.markdown("""
            <style>
                .custom-title {
                    margin-left: 280px; /* 원하는 공백의 크기 조정 */
                }
            </style>
            <h1 class="custom-title">장점👍</h1>
        """, unsafe_allow_html=True)
        # st.title("장점👍")
        st.image(current_word_cloud_path_advantage, use_column_width=True)

    # 단점
    with title_col2:
        st.markdown("""
            <style>
                .custom-title {
                    margin-left: 280px; /* 원하는 공백의 크기 조정 */
                }
            </style>
            <h1 class="custom-title">단점👎</h1>
        """, unsafe_allow_html=True)
        # st.title("단점👎")
        st.image(current_word_cloud_path_disadvantage, use_column_width=True)

# ====================================== 토픽 모델링 탭 ====================================== 
with tabs[1]:
    # 열 비율 설정
    title_col1, title_col2 = st.columns([1, 1])

    # 장점
    with title_col1:
        st.markdown("""
            <style>
                .custom-title {
                    margin-left: 280px; /* 원하는 공백의 크기 조정 */
                }
            </style>
            <h1 class="custom-title">장점👍</h1>
        """, unsafe_allow_html=True)
        # 토픽3개 반복함
        for x in range(3):
            # 토픽으로 필터링
            c_df_advantage_factory=df_advantage_factory[df_advantage_factory["토픽(장점)"]==x]
            c_topic_list=c_df_advantage_factory["토픽 {} 단어들".format(x)].values[0]
            print(c_topic_list)
            topic_word=number_list[x]+c_topic_list
            st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

            total_text="""
            <div class="scrollable-container">
            """
            text_list=c_df_advantage_factory["장점"]
            for text in text_list:
                c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                c_divider="<div class='divider'></div>" # 구분선 추가
                total_text+=c_text+c_divider

            st.markdown(total_text, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)

    # 두 번째 열에 제목 추가
    with title_col2:
        st.markdown("""
            <style>
                .custom-title {
                    margin-left: 280px; /* 원하는 공백의 크기 조정 */
                }
            </style>
            <h1 class="custom-title">단점👎</h1>
        """, unsafe_allow_html=True)
        # 토픽3개 반복함
        for x in range(3):
            # 토픽으로 필터링
            c_df_disadvantage_factory=df_disadvantage_factory[df_disadvantage_factory["토픽(단점)"]==x]
            c_topic_list=c_df_disadvantage_factory["토픽 {} 단어들".format(x)].values[0]
            print(c_topic_list)
            topic_word=number_list[x]+c_topic_list
            st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

            total_text="""
            <div class="scrollable-container">
            """
            text_list=c_df_disadvantage_factory["단점"]
            for text in text_list:
                c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                c_divider="<div class='divider'></div>" # 구분선 추가
                total_text+=c_text+c_divider

            st.markdown(total_text, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)


# =========================================  회사와 나의 성향을 분석하는 코드 추가 =============================================
pass