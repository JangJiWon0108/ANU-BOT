# jumpit_wanted_review.py
# 점핏, 원티드 회사 리뷰 관련 파일

# 라이브러리
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
import os
import json
import streamlit.components.v1 as components
# 로깅 설정: 정보성 메시지를 출력
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# 변수
current_word_cloud_path_advantage=""
current_word_cloud_path_disadvantage=""
current_word_cloud_path_want=""
c_type=""

# 6각형 관련 세션 스테이트 초기화
if "user_scores" not in st.session_state:
    st.session_state.user_scores = None

# 함수
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

# 변수
number_list=["1️⃣", "2️⃣", "3️⃣"] # 숫자 이모지

# CSS 스타일 정의
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

# 데이터 로딩
# jumpit_wanted_drop=pd.read_csv("C:/최종 프로젝트/데이터셋/점핏_원티드_리뷰_중복제거_(별점,연봉,한줄요약)_streamlit(final).csv")
# df_advantage=pd.read_csv("C:/최종 프로젝트/회사 리뷰 관련/딥노이드_장점.csv")
# df_disadvantage=pd.read_csv("C:/최종 프로젝트/회사 리뷰 관련/딥노이드_단점.csv")
# df_word_cloud=pd.read_csv("C:/최종 프로젝트/회사 리뷰 관련/회사 워드클라우드.csv")
# df_type=pd.read_csv("C:/최종 프로젝트/회사 리뷰 관련/회사업종.csv")

jumpit_wanted_drop=pd.read_csv("Streamlit구현/dataset/점핏_원티드_리뷰_중복제거_(별점,연봉,한줄요약)_streamlit(final).csv")
df_advantage=pd.read_csv("Streamlit구현/dataset/점핏_원티드_리뷰_토픽모델링_장점(fianl).csv")
df_disadvantage=pd.read_csv("Streamlit구현/dataset/점핏_원티드_리뷰_토픽모델링_단점(fianl).csv")
df_type=pd.read_csv("Streamlit구현/dataset/회사업종.csv") # 업종
file_list=os.listdir("Streamlit구현/회사 워드클라우드 결과")
df_factory_wordcloud=pd.DataFrame({
    "이미지경로":file_list
})
df_6=pd.read_csv("Streamlit구현/dataset/회사리뷰 육각형 최종.csv")
file_list_want=os.listdir("C:/최종 프로젝트/Streamlit구현/회사 워드클라우드 결과_바라는점")
df_factory_wordcloud_want=pd.DataFrame({
    "이미지경로":file_list_want
})

# 파일에서 회사명 읽기
with open('junmpit_wanted_name.txt', 'r') as f:
    junmpit_wanted_name = eval(f.read())
print("jumpit_wanted_review.py 파일에서 회사명 받음 :", junmpit_wanted_name, type(junmpit_wanted_name))


# 회사명으로 필터링
try: 
    df_info_factory=jumpit_wanted_drop[jumpit_wanted_drop["회사명"]==junmpit_wanted_name[0]]
    df_advantage_factory=df_advantage[df_advantage["회사명"]==junmpit_wanted_name[0]]
    df_disadvantage_factory=df_disadvantage[df_disadvantage["회사명"]==junmpit_wanted_name[0]]
    df_type_factory=df_type[df_type["회사명"]==junmpit_wanted_name[0]]
    current_factory_name=junmpit_wanted_name[0]
except:
    print("회사이름 존재하지 않음!")

# 워드클라우드 파일 뽑기
for x in df_factory_wordcloud["이미지경로"]:
    if current_factory_name in x and "장점" in x:
        current_word_cloud_path_advantage="Streamlit구현/회사 워드클라우드 결과/"+x
for x in df_factory_wordcloud["이미지경로"]:
    if current_factory_name in x and "단점" in x:
        current_word_cloud_path_disadvantage="Streamlit구현/회사 워드클라우드 결과/"+x
for x in df_factory_wordcloud_want["이미지경로"]:
    if current_factory_name in x and "바라는 점" in x:
        current_word_cloud_path_want="Streamlit구현/회사 워드클라우드 결과_바라는점/"+x

        

# 페이지 설정
st.set_page_config(page_icon="🏬", page_title="{}".format(junmpit_wanted_name[0]), layout="wide")

# HTML과 CSS를 스트림릿에 표시
st.markdown(css, unsafe_allow_html=True)

# 회사명
st.title("🌟"+df_info_factory["회사명"].values[0]) # 제목

# 업종
c_type=df_type_factory["업종"].values[0]
if c_type!="No":
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

# 리뷰 한줄 요약, 평균 별점, 평균 연봉 (바)
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

# 줄바꿈
st.markdown("<br>", unsafe_allow_html=True)

# 탭 만들기
tabs = st.tabs(["워드 클라우드🍧", "토픽 모델링🍩", "나와의 궁합👻"])

# 워드 클라우드 탭
with tabs[0]:
    # # 열 비율 설정
    # title_col1, title_col2 = st.columns([1, 1])

    # # 장점
    # with title_col1:
    #     st.markdown("""
    #         <style>
    #             .custom-title {
    #                 margin-left: 280px; /* 원하는 공백의 크기 조정 */
    #             }
    #         </style>
    #         <h1 class="custom-title">장점👍</h1>
    #     """, unsafe_allow_html=True)
    #     # st.title("장점👍")
    #     st.image(current_word_cloud_path_advantage, use_column_width=True)

    # # 단점
    # with title_col2:
    #     st.markdown("""
    #         <style>
    #             .custom-title {
    #                 margin-left: 280px; /* 원하는 공백의 크기 조정 */
    #             }
    #         </style>
    #         <h1 class="custom-title">단점👎</h1>
    #     """, unsafe_allow_html=True)
    #     # st.title("단점👎")
    #     st.image(current_word_cloud_path_disadvantage, use_column_width=True)

            col1, col2 = st.columns(2)
            with col1:
                with st.expander("", expanded = True):
                    st.markdown("""
                                <style>
                                .centered-header {
                                text-align: center;
                                margin-bottom: 20px; /* 하단 여백 추가 */
                                font-size: 40px; /* 글씨 크기 조정 */
                                font-weight: bold; /* 글씨를 진하게 */
                                }
                                </style>
                                <h3 class="centered-header">장점👍</h3>
                                """, unsafe_allow_html=True)
                    
                    if current_word_cloud_path_advantage!="":
                        st.image(current_word_cloud_path_advantage, use_column_width=True)
                    else:
                        st.write("워드클라우드 이미지가 없어요🥹")
                    # display_image(pros_wordcloud_path)
                    
            with col2:
                with st.expander("", expanded = True):
                    st.markdown("""
                                <style>
                                .centered-header {
                                text-align: center;
                                margin-bottom: 20px; /* 하단 여백 추가 */
                                font-size: 40px; /* 글씨 크기 조정 */
                                font-weight: bold; /* 글씨를 진하게 */
                                }
                                </style>
                                <h3 class="centered-header">단점👎</h3>
                                """, unsafe_allow_html=True)
                    
                    if current_word_cloud_path_disadvantage!="":
                        st.image(current_word_cloud_path_disadvantage, use_column_width=True)
                    else:
                        st.write("워드클라우드 이미지가 없어요🥹")
                    # display_image(cons_wordcloud_path)

            col3, col4, col5= st.columns([0.5, 1, 0.5])
            with col4:   
                with st.expander("", expanded = True):
                    st.markdown("""
                                <style>
                                .centered-header {
                                text-align: center;
                                margin-bottom: 20px; /* 하단 여백 추가 */
                                font-size: 40px; /* 글씨 크기 조정 */
                                font-weight: bold; /* 글씨를 진하게 */
                                }
                                </style>
                                <h3 class="centered-header">바라는 점🙏</h3>
                                """, unsafe_allow_html=True)
                    if current_word_cloud_path_want!="":
                        st.image(current_word_cloud_path_want, use_column_width=True)
                    else:
                        st.write("워드클라우드 이미지가 없어요🥹")
                    # display_image(want_wordcloud_path)

# 토픽 모델링 탭
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
            if not c_df_advantage_factory.empty:
                        c_topic_list = c_df_advantage_factory["토픽 {} 단어들".format(x)].values[0]
                        topic_word = number_list[x] + c_topic_list
                        st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

                        total_text = """
                        <div class="scrollable-container">
                        """
                        text_list = c_df_advantage_factory["장점"]
                        for text in text_list:
                            c_text = "<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                            c_divider = "<div class='divider'></div>"
                            total_text += c_text + c_divider

                        st.markdown(total_text, unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
            else:
                        st.write("토픽 모델링을 위한 리뷰 개수가 부족합니다🥹")
            # c_topic_list=c_df_advantage_factory["토픽 {} 단어들".format(x)].values[0]
            # print(c_topic_list)
            # topic_word=number_list[x]+c_topic_list
            # st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

            # total_text="""
            # <div class="scrollable-container">
            # """
            # text_list=c_df_advantage_factory["장점"]
            # for text in text_list:
            #     c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
            #     c_divider="<div class='divider'></div>" # 구분선 추가
            #     total_text+=c_text+c_divider

            # st.markdown(total_text, unsafe_allow_html=True)
            # st.markdown("<br>", unsafe_allow_html=True)

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
            if not c_df_disadvantage_factory.empty:
                        c_topic_list = c_df_disadvantage_factory["토픽 {} 단어들".format(x)].values[0]
                        topic_word = number_list[x] + c_topic_list
                        st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

                        total_text = """
                        <div class='scrollable-container'>
                        """
                        text_list = c_df_disadvantage_factory["단점"]
                        for text in text_list:
                            c_text = "<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
                            c_divider = "<div class='divider'></div>"
                            total_text += c_text + c_divider

                        st.markdown(total_text, unsafe_allow_html=True)
                        st.markdown("<br>", unsafe_allow_html=True)
            else:
                        st.write("토픽 모델링을 위한 리뷰 개수가 부족합니다🥹")
            # c_topic_list=c_df_disadvantage_factory["토픽 {} 단어들".format(x)].values[0]
            # print(c_topic_list)
            # topic_word=number_list[x]+c_topic_list
            # st.markdown("<h5>{}</h5>".format(topic_word), unsafe_allow_html=True)

            # total_text="""
            # <div class="scrollable-container">
            # """
            # text_list=c_df_disadvantage_factory["단점"]
            # for text in text_list:
            #     c_text="<p class='text-item' style='font-size: 15px;'>{}</p>".format(text)
            #     c_divider="<div class='divider'></div>" # 구분선 추가
            #     total_text+=c_text+c_divider

            # st.markdown(total_text, unsafe_allow_html=True)
            # st.markdown("<br>", unsafe_allow_html=True)

    # 나와의 궁합
    with tabs[2]:
                if len(df_6[df_6["회사명"] == current_factory_name])==0:
                    st.markdown("<br>", unsafe_allow_html=True)
                    st.write("나만의 궁합 분석을 위한 리뷰 개수가 부족합니다🥹")
                else:
                    with st.expander("나의 성향 점수 입력👇", expanded=True):
                        st.subheader("자신이 중요하게 생각할수록 높은 점수를 체크해 주세요😁")

                        user_scores = {}
                        criteria = ["복지", "워라밸", "자율", "성장성", "안정성", "연봉"]
                        num_list=["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]

                        for x in range(len(criteria)):
                            st.write(f"<div style='text-align: left; font-size: 18px; font-weight: bold;'>{num_list[x]}{criteria[x]}</div>", unsafe_allow_html=True)
                            user_scores[criteria[x]] = st.radio(
                                label="",  # 라벨을 빈 문자열로 설정
                                options=[1, 2, 3, 4, 5],
                                index=2,  # 기본값으로 3을 선택
                                format_func=lambda x: f"{x}",
                                key=criteria[x],  # 항목별로 고유 키 설정
                                label_visibility="collapsed",  # 라벨 숨기기
                                
                            )
                            st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

                        if st.button("OK"):
                            st.session_state.user_scores = user_scores

                    # 사용자 점수와 회사 점수 비교를 위한 차트 렌더링
                    if st.session_state.user_scores:
                        # 선택된 회사의 데이터 가져오기
                        company_scores = df_6[df_6["회사명"] == current_factory_name].iloc[0].to_dict()

                        # 소수점 자리수 조정
                        company_scores = {k: round(v, 1) if isinstance(v, float) else v for k, v in company_scores.items()}

                        # 사용자 점수와 회사 점수 비교를 위한 데이터 준비
                        def prepare_chart_data(user_scores, company_scores):
                            categories = list(user_scores.keys())
                            user_data = list(user_scores.values())
                            company_data = [company_scores[cat] for cat in categories]
                            return categories, user_data, company_data

                        categories, user_data, company_data = prepare_chart_data(st.session_state.user_scores, company_scores)

                        # 성향 매칭 비율 계산
                        def calculate_matching_percentage(user_scores, company_scores):
                            total_difference = sum(abs(user_scores[cat] - company_scores[cat]) for cat in user_scores)
                            max_difference = len(user_scores) * 4  # 최대 차이는 (5 - 1) * 항목 수
                            matching_percentage = (1 - (total_difference / max_difference)) * 100
                            return round(matching_percentage, 2)

                        matching_percentage = calculate_matching_percentage(st.session_state.user_scores, company_scores)

                        # # Highcharts 레이더 차트 생성
                        # def generate_highcharts_html(categories, user_data, company_data):
                        #     # 유저 데이터와 회사 데이터를 각각 소수점 첫째 자리로 반올림
                        #     user_data = [round(score, 1) for score in user_data]
                        #     company_data = [round(score, 1) for score in company_data]
                            
                        #     # JSON으로 변환
                        #     categories_json = json.dumps(categories)
                        #     user_data_json = json.dumps(user_data)
                        #     company_data_json = json.dumps(company_data)

                        #     html_code = f"""
                        #     <!DOCTYPE html>
                        #     <html>
                        #     <head>
                        #         <title>Highcharts Radar Chart Example</title>
                        #         <script src="https://code.highcharts.com/highcharts.js"></script>
                        #         <script src="https://code.highcharts.com/highcharts-more.js"></script>
                        #         <script src="https://code.highcharts.com/modules/exporting.js"></script>
                        #         <script src="https://code.highcharts.com/modules/export-data.js"></script>
                        #         <script src="https://code.highcharts.com/modules/accessibility.js"></script>
                        #     </head>
                        #     <body>
                        #     <div id="container" style="width: 600px; height: 400px;"></div>
                        #     <script>
                        #     document.addEventListener('DOMContentLoaded', function () {{
                        #         Highcharts.chart('container', {{
                        #             chart: {{
                        #                 polar: true,
                        #                 type: 'line'
                        #             }},
                        #             title: {{
                        #                 text: '👍성향 매치 비율 : {matching_percentage}%',
                        #                 x: -60,
                        #                 style: {{
                        #                     fontSize: '35px',  // 폰트 크기 지정
                        #                     fontWeight: 'bold', // 폰트 두께 지정 (옵션)
                        #                     color: '#333333'    // 폰트 색상 지정 (옵션)
                        #                 }}
                        #             }},
                        #             pane: {{
                        #                 size: '80%'
                        #             }},
                        #             xAxis: {{
                        #                 categories: {categories_json},
                        #                 tickmarkPlacement: 'on',
                        #                 lineWidth: 0
                        #             }},
                        #             yAxis: {{
                        #                 gridLineInterpolation: 'polygon',
                        #                 lineWidth: 0,
                        #                 min: 0,
                        #                 max: 5,
                        #                 tickInterval: 1
                        #             }},
                        #             tooltip: {{
                        #                 shared: true,
                        #                 pointFormat: '<span style="color:{{series.color}}">{{series.name}}: <b>{{point.y:,.2f}}</b><br/>'
                        #             }},
                        #             series: [{{
                        #                 name: '나의 성향',
                        #                 data: {user_data_json},
                        #                 pointPlacement: 'on'
                        #             }}, {{
                        #                 name: '{current_factory_name} 성향',
                        #                 data: {company_data_json},
                        #                 pointPlacement: 'on',
                        #                 color: 'red'
                        #             }}],
                        #             responsive: {{
                        #                 rules: [{{
                        #                     condition: {{
                        #                         maxWidth: 500
                        #                     }},
                        #                     chartOptions: {{
                        #                         legend: {{
                        #                             align: 'center',
                        #                             verticalAlign: 'bottom',
                        #                             layout: 'horizontal'
                        #                         }},
                        #                         pane: {{
                        #                             size: '70%'
                        #                         }}
                        #                     }}
                        #                 }}]
                        #             }}
                        #         }});
                        #     }});
                        #     </script>
                        #     </body>
                        #     </html>
                        #     """
                        #     return html_code

                        def generate_highcharts_html(categories, user_data, company_data):
                            # 유저 데이터와 회사 데이터를 각각 소수점 첫째 자리로 반올림
                            user_data = [round(score, 1) for score in user_data]
                            company_data = [round(score, 1) for score in company_data]

                            # JSON으로 변환
                            categories_json = json.dumps(categories)
                            user_data_json = json.dumps(user_data)
                            company_data_json = json.dumps(company_data)

                            html_code = f"""
                            <!DOCTYPE html>
                            <html>
                            <head>
                                <title>Highcharts Radar Chart Example</title>
                                <script src="https://code.highcharts.com/highcharts.js"></script>
                                <script src="https://code.highcharts.com/highcharts-more.js"></script>
                                <script src="https://code.highcharts.com/modules/exporting.js"></script>
                                <script src="https://code.highcharts.com/modules/export-data.js"></script>
                                <script src="https://code.highcharts.com/modules/accessibility.js"></script>
                                <style>
                                    .title-container {{
                                        display: flex;
                                        align-items: center;
                                        justify-content: center;
                                        font-size: 25px;
                                        font-weight: bold;
                                        color: #333333;
                                        margin-bottom: 20px;
                                        margin-right: 100px; /* 전체를 왼쪽으로 이동 */
                                    }}
                                    .circle-text {{
                                        display: flex;
                                        justify-content: center;
                                        align-items: center;
                                        width: 80px;
                                        height: 80px;
                                        background-color: pink;
                                        border-radius: 50%;
                                        font-size: 23px;
                                        font-weight: bold;
                                        color: #333333;
                                        margin-left: 12px;
                                    }}
                                    #container {{
                                        width: 600px;  /* 차트 너비를 100%로 설정하여 화면에 맞게 조정 */
                                        height: 400px; /* 차트 높이를 더 크게 조정 */
                                    }}
                                </style>
                            </head>
                            <body>
                            <div class="title-container">
                                👍성향 매치 비율
                                <div class="circle-text">{matching_percentage}%</div>
                            </div>
                            <div id="container"></div>
                            <script>
                            document.addEventListener('DOMContentLoaded', function () {{
                                Highcharts.chart('container', {{
                                    chart: {{
                                        polar: true,
                                        type: 'line',
                                        marginBottom: 100, /* 차트의 아래쪽 여백을 추가 */
                                    }},
                                    title: {{
                                        text: '',
                                        x: -60,
                                    }},
                                    pane: {{
                                        size: '80%'
                                    }},
                                    xAxis: {{
                                        categories: {categories_json},
                                        tickmarkPlacement: 'on',
                                        lineWidth: 0
                                    }},
                                    yAxis: {{
                                        gridLineInterpolation: 'polygon',
                                        lineWidth: 0,
                                        min: 0,
                                        max: 5,
                                        tickInterval: 1
                                    }},
                                    tooltip: {{
                                        shared: true,
                                        pointFormat: '<span style="color:{{series.color}}">{{series.name}}: <b>{{point.y:,.2f}}</b><br/>'
                                    }},
                                    series: [{{
                                        name: '나의 성향',
                                        data: {user_data_json},
                                        pointPlacement: 'on'
                                    }}, {{
                                        name: '{current_factory_name} 성향',
                                        data: {company_data_json},
                                        pointPlacement: 'on',
                                        color: 'red'
                                    }}],
                                    responsive: {{
                                        rules: [{{
                                            condition: {{
                                                maxWidth: 500
                                            }},
                                            chartOptions: {{
                                                legend: {{
                                                    align: 'center',
                                                    verticalAlign: 'bottom',
                                                    layout: 'horizontal'
                                                }},
                                                pane: {{
                                                    size: '70%'
                                                }}
                                            }}
                                        }}]
                                    }}
                                }});
                            }});
                            </script>
                            </body>
                            </html>
                            """
                            return html_code
                        # Generate and display the chart
                        html_code = generate_highcharts_html(categories, user_data, company_data)
                        components.html(html_code, height=500, width=700)

# =========================================  =============================================
