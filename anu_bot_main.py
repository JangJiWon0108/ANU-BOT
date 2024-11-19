# anu_bot_main.py
# Streamlit 에 최종 챗봇 구현하는 파일(메인)

# =============================================== 라이브러리 ====================================================
from dotenv import load_dotenv
import pandas as pd
from langchain_community.vectorstores import FAISS
from langchain_upstage import UpstageEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.callbacks.manager import CallbackManager
from langchain_core.prompts import PromptTemplate
from operator import itemgetter
import uuid
import streamlit as st
from streamlit_option_menu import option_menu
from langchain.schema import ChatMessage, HumanMessage
import time
import subprocess
import json
import emoji
import sys
import numpy as np

# =============================================== 모듈 ====================================================
import llm_model
import embedding_model
import vector_DB
import question_retriever_routing
import retriever
import chain
import sidebar_info
import emoji_moving
import anu_bot_info
import anu_bot_subject
import anu_bot_hire

# =============================================== 함수 ====================================================
# 다른 .py 파일 실행 (회사 리뷰)
def run_jumpit_wanted_review_page():
    time.sleep(1)
    subprocess.Popen(["streamlit", "run", "Streamlit구현/jumpit_wanted_review.py"])

# 다른 .py 파일 실행 (에타 강의평 1)
def run_everytime_review_page_1():
    time.sleep(1)
    subprocess.Popen(["streamlit", "run", "Streamlit구현/everytime_review_1.py"])

# 다른 .py 파일 실행 (에타 강의평 2)
def run_everytime_review_page_2():
    time.sleep(1)
    subprocess.Popen(["streamlit", "run", "Streamlit구현/everytime_review_2.py"])

# 다른 .py 파일 실행 (에타 강의평 3)
def run_everytime_review_page_3():
    time.sleep(1)
    subprocess.Popen(["streamlit", "run", "Streamlit구현/everytime_review_3.py"])

# 다른 .py 파일 실행 (안동대 정보 챗봇)
def run_anu_info_page():
    time.sleep(1)
    subprocess.Popen(["streamlit", "run", "Streamlit구현/anu_bot_info.py"])

# 스트림형식으로 바꾸기
def stream_data():
     for word in answer.split(" "):
        yield word + " "
        time.sleep(0.06) 

# ================================== 변수 ====================================
flag_link=0
llm_answer_jumpit_wanted_name=[]
llm_answer_jumpit_wanted_review_count=[]
llm_answer_subject=[]
llm_answer_pro=[]
max_float = sys.float_info.max
subject=""
professor=""
# button_jumpit_wanted_review = 0  # 또는 False로 설정하여 비활성화

# ================================== 페이지 설정= =================================
st.set_page_config(page_title="ANU BOT", page_icon="🤖", layout="centered")

# =================================== 사이드 바 =============================   
with st.sidebar:
    selected = option_menu("Menu", ["안동대학교 정보", "교과목 정보", "채용공고 정보"], 
         icons=["building", 'book', "mortarboard"], menu_icon="robot", default_index=0)
    
if selected == "안동대학교 정보":
    # 사이드바 
    markdown_str=sidebar_info.f_sidebar_anu_info()
    expander_str=sidebar_info.f_question_ex_anu_info()

    with st.sidebar:
        st.markdown(markdown_str, unsafe_allow_html=True)
    
    with st.sidebar:
        with st.expander("🔎질문 예시", expanded=True):
            st.markdown(expander_str, unsafe_allow_html=True)

    # 메인
    anu_bot_info.f_anu_bot_info()
            
elif selected == "교과목 정보":
    # 사이드바
    markdown_str=sidebar_info.f_sidebar_subject_info()
    expander_str=sidebar_info.f_question_ex_subject_info()

    with st.sidebar:
        st.markdown(markdown_str, unsafe_allow_html=True)
    
    with st.sidebar:
        with st.expander("🔎질문 예시", expanded=True):
            st.markdown(expander_str, unsafe_allow_html=True)

    # 메인
    anu_bot_subject.f_anu_bot_subject()

elif selected == "채용공고 정보":
    # 사이드바
    markdown_str=sidebar_info.f_sidebar_hire_info()
    expander_str=sidebar_info.f_question_ex_hire_info()

    with st.sidebar:
        st.markdown(markdown_str, unsafe_allow_html=True)
    
    with st.sidebar:
        with st.expander("🔎질문 예시", expanded=True):
            st.markdown(expander_str, unsafe_allow_html=True)

    # 메인
    anu_bot_hire.anu_bot_hire()

# with st.sidebar:
#     st.sidebar.button('버튼 1')
#     st.sidebar.button('버튼 2')
#     st.sidebar.button('버튼 3')

#     st.markdown("<br><br>".format(), unsafe_allow_html=True)
#     st.markdown("<h3>😊채용공고를 추천해 드립니다❗</h3>".format(), unsafe_allow_html=True)
#     st.markdown("<p>질문 예시) LLM 챗봇 관련된 채용공고를 추천해 주세요.</p>".format(), unsafe_allow_html=True)
#     st.markdown("<br>".format(), unsafe_allow_html=True)
#     st.markdown("<h3>😊특정 회사에 대한 리뷰를 분석해 드립니다❗</h3>".format(), unsafe_allow_html=True)
#     st.markdown("<p>질문 예시) 000회사의 리뷰를 보여주세요.</p>".format(), unsafe_allow_html=True)
#     st.markdown("<br><br>".format(), unsafe_allow_html=True)


# ================================== 페이지 가장 위에 이모지 애니메이션 =================================
# st.components.v1.html(emoji_moving.f_emoji_moving_whale(), height=42)

# ================================== 페이지 제목 ===============================
# 페이지 제목 구성
# 첫번째 열과 두번째 열의 너비를 상대적으로 1:4로 지정
# title_col1, title_col2, title_col3 = st.columns([0.7, 1, 1])

# 첫 번째 열에 이미지 추가
# with title_col1:
#     st.image("image/ai.png")

# # 두 번째 열에 제목 추가
# with title_col2:
#     st.title("ANU Bot")
#     st.markdown("<h5>안녕하세요🍭</h5>", unsafe_allow_html=True)
#     st.markdown("<p><b>아누봇 입니다🤖</b></p>", unsafe_allow_html=True)

# with title_col3:
#     st.markdown("<br><br><br><br>", unsafe_allow_html=True)
#     if st.button("🍀대화내용삭제🍀"):
#         st.session_state.message_list=[]

# ========================================== 아래부터 주석 ==========================================================
#       
# # ========================== session_state 가 비어있다면 빈 리스트 저장, False 값 저장 =============================
# # st.session_state 는 전역변수 느낌
# # 비어있다면 빈 리스트를 저장하고, 채팅 할때마다 "role" 과 "content"를 딕셔너리로 append함
# if "message_list" not in st.session_state:
#     st.session_state.message_list=[]

# if "button_visible" not in st.session_state:
#     st.session_state.button_visible = False
    
# # ========================== session_state 를 돌면서 내용을 write함 =============================
# for message in st.session_state.message_list:
#     if message["role"] == "user":
#         with st.chat_message("user"):
#             st.write(message["content"])
#     elif message["role"] == "ai":
#         with st.chat_message("ai"):
#             st.write(message["content"])
#     elif message["role"] == "button_factory":
#         if st.session_state.button_visible:
#             random_float_np = np.random.uniform(0, max_float)
#             st.button(message["content"], on_click=run_jumpit_wanted_review_page, key="factory_review_key"+str(random_float_np))
#     elif message["role"] == "button_everytime_1":
#         if st.session_state.button_visible:
#             random_float_np = np.random.uniform(0, max_float)
#             st.button(message["content"], on_click=run_everytime_review_page_1, key="everytime_review_key_1"+str(random_float_np))
#     elif message["role"] == "button_everytime_2":
#         if st.session_state.button_visible:
#             random_float_np = np.random.uniform(0, max_float)
#             st.button(message["content"], on_click=run_everytime_review_page_2, key="everytime_review_key_2"+str(random_float_np))
#     elif message["role"] == "button_everytime_3":
#         if st.session_state.button_visible:
#             random_float_np = np.random.uniform(0, max_float)
#             st.button(message["content"], on_click=run_everytime_review_page_3, key="everytime_review_key_3"+str(random_float_np))
    
# # ========================== session_state 를 돌면서 내용을 write함 =============================
# # for message in st.session_state.message_list:
# #     with st.chat_message(message["role"]):
# #         st.write(message["content"])


# # ================================== 사용자 입력 및 LLM 답변 출력 ===============================
# # 사용자 입력창 추가
# # user_question 에 저장됨
# # st.chat_message("user") 를 통해 user의 바 생성하고 st.wrie()를 통해 텍스트 출력
# # user은 "role" 로 저장됨
# # with를 사용해써 해당 바 안에 텍스트 넣음
# if user_question := st.chat_input(placeholder="질문을 입력해 주세요😀"):
#     with st.chat_message("user"):
#         st.write(user_question)
#         st.session_state.message_list.append({"role":"user", "content":user_question})

#     with st.spinner("답변을 생성하는 중입니다😊"):
#         user_question_precleaning=question_retriever_routing.f_question_precleaning(user_question)
#         retriever_var, prompt_var, flag_sort_chunk, flag_link=question_retriever_routing.f_retriever_routing(user_question_precleaning)
#         prompt_chain=chain.f_chain(retriever_var, prompt_var, flag_sort_chunk)
#         llm_model=llm_model.f_OpenAI_llm_model()
#         total_chain=prompt_chain | llm_model | StrOutputParser()    
#         ai_message=total_chain.invoke({"question":user_question_precleaning})
#     with st.chat_message("ai"):
#         # 스트림을 write_stream으로 출력
#         answer = ai_message if isinstance(ai_message, str) else "No Answer Available."
#         st.write_stream(stream_data)
#         st.session_state.message_list.append({"role":"ai", "content":ai_message})
#         print(flag_link)
#         # 회사 추출하기
#         if flag_link==1:
#             # LLM의 답변에서 회사명 추출하기
#             jumpit_wanted_drop=pd.read_csv("dataset/점핏_원티드_리뷰_전처리완료(중복 제거O)(한줄요약) (final).csv")
#             for x in jumpit_wanted_drop.index:
#                 if jumpit_wanted_drop.loc[x, "회사명"] in ai_message:
#                     llm_answer_jumpit_wanted_name.append(jumpit_wanted_drop.loc[x, "회사명"])
#                     llm_answer_jumpit_wanted_review_count.append(jumpit_wanted_drop.loc[x, "리뷰개수"])
#                     print(llm_answer_jumpit_wanted_name, llm_answer_jumpit_wanted_review_count)
#                     button_jumpit_wanted_review=1
#                     if len(llm_answer_jumpit_wanted_name)>=1:
#                         with open('junmpit_wanted_name.txt', 'w') as f:
#                             f.write(str(llm_answer_jumpit_wanted_name))
#         # 에타 강의평
#         if flag_link==2:
#             # 데이터 로딩
#             everytime_drop=pd.read_csv("dataset/에브리타임 강의평, 평균별점, 리뷰개수, 긍부정, LLM키워드(중복 제거X).csv")
#             everytime_drop=everytime_drop.drop_duplicates(subset=["교과목명", "담당교수"])

#             # 추출된 교과목명과 담당교수 리스트
#             subject_professor_pairs = []
#             result_everytime_sub_pro_1=[]
#             result_everytime_sub_pro_2=[]
#             result_everytime_sub_pro_3=[]

#             # 응답 데이터를 줄 단위로 나누기
#             lines = ai_message.splitlines()

#             # 교과목명과 담당교수 추출
#             for line in lines:
#                 if "교과목명" in line:
#                     for y in everytime_drop["교과목명"]:
#                         if y in line:
#                             subject = y
#                             break  # 교과목명이 발견되면 반복 종료
#                 elif "담당교수" in line:
#                     for z in everytime_drop["담당교수"]:
#                         if z in line:
#                             professor = z
#                             break  # 교수명이 발견되면 반복 종료
                
#                 # 교과목명과 담당교수가 모두 발견된 경우에만 쌍 추가
#                 if subject and professor:
#                     subject_professor_pairs.append([subject, professor])
#                     # 교과목명과 담당교수 초기화
#                     subject = ""
#                     professor = ""

#             # 추출된 쌍 저장
#             result_everytime_sub_pro_1 = subject_professor_pairs[0] if len(subject_professor_pairs) > 0 else []
#             result_everytime_sub_pro_2 = subject_professor_pairs[1] if len(subject_professor_pairs) > 1 else []
#             result_everytime_sub_pro_3 = subject_professor_pairs[2] if len(subject_professor_pairs) > 2 else []

#             # 저장
#             with open('everytime_sub_pro_1.txt', 'w') as f:
#                 f.write(str(result_everytime_sub_pro_1))
#             with open('everytime_sub_pro_2.txt', 'w') as f:
#                 f.write(str(result_everytime_sub_pro_2))
#             with open('everytime_sub_pro_3.txt', 'w') as f:
#                 f.write(str(result_everytime_sub_pro_3))
            

#     # flag_link 가 1이면 회사리뷰
#     if flag_link==1:
#         factory_name="🌈"+llm_answer_jumpit_wanted_name[0]
#         st.session_state.button_visible = True
#         st.session_state.message_list.append({"role": "button_factory", "content": factory_name})
#         st.button(factory_name+"  리뷰 분석 결과🔎", on_click=run_jumpit_wanted_review_page)                      
    
#     # flag_link 가 2라면 에타 (최대 3개)
#     elif flag_link==2:
#         # 첫 번째 조건: a의 길이가 1 이상일 때
#         if len(result_everytime_sub_pro_1) > 0:
#             sub_1=result_everytime_sub_pro_1[0]
#             pro_1=result_everytime_sub_pro_1[1]
#             button_str_1 = "📖"+sub_1 + "🧑‍🏫" +pro_1 + " 교수님"
#             st.session_state.button_visible = True
#             st.session_state.message_list.append({"role": "button_everytime_1", "content": button_str_1})
#             st.button(button_str_1, on_click=run_everytime_review_page_1)
        
#         # 두 번째 조건: a와 b의 길이가 1 이상일 때
#         if len(result_everytime_sub_pro_1) > 0 and len(result_everytime_sub_pro_2) > 0:
#             sub_2=result_everytime_sub_pro_2[0]
#             pro_2=result_everytime_sub_pro_2[1]
#             button_str_2 = "📖"+sub_2 + "🧑‍🏫" +pro_2 + " 교수님"
#             st.session_state.button_visible = True
#             st.session_state.message_list.append({"role": "button_everytime_2", "content": button_str_2})
#             st.button(button_str_2, on_click=run_everytime_review_page_2)

#         # 세 번째 조건: a, b, c 모두의 길이가 1 이상일 때
#         if len(result_everytime_sub_pro_1) > 0 and len(result_everytime_sub_pro_2) > 0 and len(result_everytime_sub_pro_3) > 0:
#             sub_3=result_everytime_sub_pro_3[0]
#             pro_3=result_everytime_sub_pro_3[1]
#             button_str_3 = "📖"+sub_3 + "🧑‍🏫" +pro_3 + " 교수님"
#             st.session_state.button_visible = True
#             st.session_state.message_list.append({"role": "button_everytime_3", "content": button_str_3})
#             st.button(button_str_3, on_click=run_everytime_review_page_3)

