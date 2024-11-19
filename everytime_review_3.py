# everytime_reveiw.py 파일
# 에브리타임 강의평 관련 파일

# 라이브러리
import plotly.express as px
import plotly.graph_objects as go
import os
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # 수정된 부분
import wordcloud
import matplotlib.font_manager as fm
from io import BytesIO
from streamlit_option_menu import option_menu
import ast
import koreanize_matplotlib 
from konlpy.tag import Okt
from gensim import corpora
from gensim.models import LdaModel
from collections import Counter
import re
import io
import base64
import matplotlib.pyplot as plt
# 로깅 설정: 정보성 메시지를 출력
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 모듈
from utils import convert_string_to_list, create_star_rating

# 함수
# ----------------------교과목별 평균 별점을 시각화하는 함수---------------------#
def visualize_ratings(course_name, professor_name, every):
    # 조건에 따른 데이터 필터링
    if course_name == '전체' and professor_name == '전체':
        filtered_df = everytime_final
        title_prefix = "전체 데이터"
    elif course_name == '전체':
        filtered_df = everytime_final[everytime_final['담당교수'] == professor_name]
        title_prefix = f"교수님: {professor_name}"
    elif professor_name == '전체':
        filtered_df = everytime_final[everytime_final['교과목명'] == course_name]
        title_prefix = f"과목: {course_name}"
    else:
        filtered_df = everytime_final[(everytime_final['교과목명'] == course_name) & (everytime_final['담당교수'] == professor_name)]
        title_prefix = f"{course_name}:{professor_name}"

    # 평균 별점 계산
    average_rating = filtered_df['별점'].mean() * 20  # 백분율로 변환 (100% = 5점)
    
    # HTML을 이용하여 별점 표시
    stars_html = create_star_rating(average_rating)
    
    # Streamlit을 사용해 HTML 렌더링
    # st.markdown(f"### {title_prefix} 평균 별점")
    st.markdown("<h4>😆평균 별점</h4>", unsafe_allow_html=True)
    st.markdown(stars_html, unsafe_allow_html=True)

    # 별점 비율 시각화 (Pie Chart)
    rating_counts = filtered_df['별점'].value_counts().sort_index()
    fig_pie = px.pie(values=rating_counts.values, names=rating_counts.index, title='별점별 비율')
    fig_pie.update_traces(
        textinfo='label+percent',
        texttemplate='%{label}점<br>%{percent:.2%}',
        textfont_size=20,
        marker=dict(colors=['#AEC6CF', '#FFB7B2', '#B5EAD7', '#FFDAC1', '#C3B1E1', '#FFDFBA'])
    )
    fig_pie.update_layout(
        title={'text': '<b>별점별 비율</b>', 'x': 0.5, 'xanchor': 'center', 'font': {'size': 24}},
        height=600,
        width=1200,
        showlegend=False
    )

    return fig_pie


# 변수
flag_run=0
image_path_wordcloud_1=0
image_path_wordcloud_0=0
subject_detail=""
subject_type=""
subject_hakjeom=""
subject_hakgwa=""
subject_room=""
review_pos_text=""
review_neg_text=""
flag_review_pos=0
flag_review_neg=0
flag_word_pos=0
flag_word_neg=0

# CSS 스타일 정의
# CSS 스타일 정의
css = """
    <style>    
    .scrollable-container {
        max-height: 250px; /* 스크롤 가능한 영역의 최대 높이 설정 */
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

# 과목명, 교수명 파일 읽기
with open('everytime_sub_pro_3.txt', 'r') as f:
    everytime_sub_pro = eval(f.read())
    sub=everytime_sub_pro[0]
    pro=everytime_sub_pro[1]
print("everytime_review_3.py 파일에서 과목, 교수명 받음 :", sub, pro)

# 데이터 로딩
# everytime=pd.read_csv("Streamlit구현/dataset/에브리타임 강의평, 평균별점, 리뷰개수, 긍부정, LLM키워드(중복 제거X).csv")
# everytime_drop=everytime.drop_duplicates(subset=["교과목명", "담당교수"])
# anu_subject_info=pd.read_csv("Streamlit구현/dataset/벡터DB에 넣을 안동대 교과목정보_final.csv")

everytime_final=pd.read_csv("Streamlit구현/dataset/에타 리뷰 긍부정 세부정보_final.csv")
file_list=os.listdir("Streamlit구현/에타_wordclouds_긍부정처리_최종_final")
word=pd.DataFrame({
    "이미지경로":file_list
})


# 교과목 df에서 해당 과목과 교수님의 정보가 있는지 검사
for x in everytime_final.index:
    if everytime_final.loc[x, "담당교수"]==pro and everytime_final.loc[x, "교과목명"]==sub:
        subject_hakgwa=everytime_final.loc[x, "개설학과"]
        subject_type=everytime_final.loc[x, "이수구분"]
        subject_hakjeom=str(everytime_final.loc[x, "학점"])
        subject_room=everytime_final.loc[x, "강의시간[강의실]"]
        subject_detail=everytime_final.loc[x, "세부정보"]

# 에타 강의평 df에서 해당 과목과 교수님 긍정/부정 리뷰가 있는지 검사
if len(everytime_final[(everytime_final["담당교수"]==pro)&(everytime_final["교과목명"]==sub)][everytime_final["label"]==1]["리뷰"]) >= 1:
    flag_review_pos=1
    review_pos_text=everytime_final[(everytime_final["담당교수"]==pro)&(everytime_final["교과목명"]==sub)][everytime_final["label"]==1]["리뷰"]
else:
    flag_eview_pos=0

if len(everytime_final[(everytime_final["담당교수"]==pro)&(everytime_final["교과목명"]==sub)][everytime_final["label"]==0]["리뷰"]) >= 1:
    flag_review_neg=1
    review_neg_text=everytime_final[(everytime_final["담당교수"]==pro)&(everytime_final["교과목명"]==sub)][everytime_final["label"]==0]["리뷰"]
else:
    flag_review_neg=0
    

# 해당 과목과 교수님 워클 파일이 있는지 검사 (긍정)
# 없다면 처리하는 코드 추가
for x in word["이미지경로"]:
    if sub in x and pro in x and "긍정" in x:
        flag_word_pos=1
        image_path_wordcloud_1="Streamlit구현/에타_wordclouds_긍부정처리_최종_final/"+x
        break

# 해당 과목과 교수님 워클 파일이 있는지 검사 (부정)
# 없다면 처리하는 코드 추가
for x in word["이미지경로"]:
    if sub in x and pro in x and "부정" in x:
        flag_word_neg=1
        image_path_wordcloud_0="Streamlit구현/에타_wordclouds_긍부정처리_최종_final/"+x
        break


# 페이지 설정
st.set_page_config(page_title=pro+"/"+sub, page_icon="🏫", layout="wide")
# HTML과 CSS를 스트림릿에 표시
st.markdown(css, unsafe_allow_html=True)

# 제목
st.title("📚"+sub)
st.markdown(f"""<b style="font-size:24px;">🧸{pro} 교수님</b>""", unsafe_allow_html=True)
# 익스패너
with st.expander("교과목 정보"):
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
            <span>1️⃣<b>학과 </b> </span><span class="highlight-background-red">{subject_hakgwa}</span>
        </div>
        <br>
    """, unsafe_allow_html=True)
    st.markdown(f"""
                    <style>
                        .highlight-background-orange {{
                            background-color: #FFD5B5; /* 배경색 (파스텔 주황) */
                            padding: 10px; /* 텍스트와 배경 사이의 패딩 */
                            border-radius: 5px; /* 모서리 둥글게 */
                            display: inline; /* 배경색이 텍스트에만 적용되도록 */
                        }}
                    </style>
                    <div>
                        <span>2️⃣<b>이수구분 </b> </span><span class="highlight-background-orange">{subject_type}</span>
                    </div>
                    <br>
                """, unsafe_allow_html=True)
    st.markdown(f"""
            <style>
                .highlight-background-yellow {{
                    background-color: #FFEB99; /* 배경색 (파스텔 노랑) */
                    padding: 10px; /* 텍스트와 배경 사이의 패딩 */
                    border-radius: 5px; /* 모서리 둥글게 */
                    display: inline; /* 배경색이 텍스트에만 적용되도록 */
                }}
            </style>
            <div>
                <span>3️⃣<b>학점 </b> </span><span class="highlight-background-yellow">{subject_hakjeom}</span>
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
                <span>4️⃣<b>강의실&시간 </b> </span><span class="highlight-background-green">{subject_room}</span>
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
                    display: inline-block; /* inline-block으로 변경 */
                }}
            </style>
            <div>
                <span>5️⃣<b>강의정보 </b> </span><span class="highlight-background-blue">{subject_detail}</span>
            </div>
            <br>
        """, unsafe_allow_html=True)
    
    
# 줄바꿈
st.markdown("<br>", unsafe_allow_html=True)

# 탭 만들기
tabs = st.tabs(["워드 클라우드🍉", "별점🥝"])

# 워드 클라우드 탭
with tabs[0]:
    # 긍정, 부정 나누기
    title_col1, title_col2 = st.columns([1, 1])

    # 긍정
    with title_col1:
        st.markdown("""
                <style>
                    .custom-title {
                        margin-left: 280px; /* 원하는 공백의 크기 조정 */
                    }.centered-text {
                    font-size: 24px;  /* 글자 크기 조정 */
                    display: flex;
                    justify-content: center;  /* 좌우 가운데 정렬 */
                    align-items: center;  /* 상하 가운데 정렬 */
                    height: 200px;  /* 높이 설정으로 상하 가운데 정렬 */
                    font-weight: bold;  /* 글자 두께 조정 (선택 사항) */
                    }
                </style>
                <h1 class="custom-title">긍정👍</h1>
            """, unsafe_allow_html=True)
            # st.title("장점👍")
        if flag_word_pos==1:
            st.image(image_path_wordcloud_1, use_column_width=True)
        else:
            st.markdown("""
                <p class="centered-text">❌긍정 강의평이 없어요</p>
                """, unsafe_allow_html=True)

        if flag_review_pos==1:
                total_text="""
                <div class="scrollable-container">
                """
                for text in review_pos_text:
                    c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                    c_divider="<div class='divider'></div>" # 구분선 추가
                    total_text+=c_text+c_divider

                st.markdown(f"""<b style="font-size:24px;">🐼긍정 강의평</b>""", unsafe_allow_html=True)
                st.markdown(total_text, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

    # 부정
    with title_col2:
        st.markdown("""
                <style>
                    .custom-title {
                        margin-left: 280px; /* 원하는 공백의 크기 조정 */
                    }
                    .centered-text {
                    font-size: 24px;  /* 글자 크기 조정 */
                    display: flex;
                    justify-content: center;  /* 좌우 가운데 정렬 */
                    align-items: center;  /* 상하 가운데 정렬 */
                    height: 200px;  /* 높이 설정으로 상하 가운데 정렬 */
                    font-weight: bold;  /* 글자 두께 조정 (선택 사항) */
                    }
                </style>
                <h1 class="custom-title">부정👎</h1>
            """, unsafe_allow_html=True)
            # st.title("단점👎")
        if flag_word_neg==1:
            st.image(image_path_wordcloud_0, use_column_width=True)
        else:
            st.markdown("""
                <p class="centered-text">❌부정 강의평이 없어요</p>
                """, unsafe_allow_html=True)


        if flag_review_neg==1:
                total_text="""
                <div class="scrollable-container">
                """
                for text in review_neg_text:
                    c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                    c_divider="<div class='divider'></div>" # 구분선 추가
                    total_text+=c_text+c_divider

                st.markdown(f"""<b style="font-size:24px;">🐰부정 강의평</b>""", unsafe_allow_html=True)
                st.markdown(total_text, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
    
    # 별점 탭
with tabs[1]:
    fig_star = visualize_ratings(sub, pro, everytime_final)
    st.plotly_chart(fig_star)




