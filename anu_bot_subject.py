# anu_bot_subject.py
# 교과목, 강의평 관련 파일

def f_anu_bot_subject():
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
    import question_retriever_routing_aun_subject
    # =============================================== 함수 ===================================================
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

    # ================================== 페이지 가장 위에 이모지 애니메이션 =================================
    st.components.v1.html(emoji_moving.f_emoji_moving_chicken(), height=42)

    # ================================== 페이지 제목 ===============================
    # 페이지 제목 구성
    # 첫번째 열과 두번째 열의 너비를 상대적으로 1:4로 지정
    title_col1, title_col2, title_col3 = st.columns([1, 1, 1])

    # 첫 번째 열에 이미지 추가
    with title_col1:
        st.image("Streamlit구현/image/ANU_BOT.jpg")

    # 두 번째 열에 제목 추가
    with title_col2:
        st.markdown(
            """
            <h1 style='color: black;'>ANU BOT</h1>
            """, 
            unsafe_allow_html=True
        )
        st.markdown("<h5>안녕😁</h5>", unsafe_allow_html=True)
        st.markdown("<h6>나는 아누봇이야🌈</h6>", unsafe_allow_html=True)

    with title_col3:
        st.markdown("<br><br><br><br>", unsafe_allow_html=True)
        if st.button("🌷대화내용삭제🌷"):
            st.session_state.message_list_subject=[]
            
    # ========================== session_state 가 비어있다면 빈 리스트 저장, False 값 저장 =============================
    # st.session_state 는 전역변수 느낌
    # 비어있다면 빈 리스트를 저장하고, 채팅 할때마다 "role" 과 "content"를 딕셔너리로 append함
    if "message_list_subject" not in st.session_state:
        st.session_state.message_list_subject=[]

    if "button_visible_subject" not in st.session_state:
        st.session_state.button_visible_subject = False
        
    # ========================== session_state 를 돌면서 내용을 write함 =============================
    for message in st.session_state.message_list_subject:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        elif message["role"] == "ai":
            with st.chat_message("ai"):
                st.write(message["content"])
        elif message["role"] == "button_everytime_1":
            if st.session_state.button_visible_subject:
                random_float_np = np.random.uniform(0, max_float)
                st.button(message["content"], on_click=run_everytime_review_page_1, key="everytime_review_key_1"+str(random_float_np))
        elif message["role"] == "button_everytime_2":
            if st.session_state.button_visible_subject:
                random_float_np = np.random.uniform(0, max_float)
                st.button(message["content"], on_click=run_everytime_review_page_2, key="everytime_review_key_2"+str(random_float_np))
        elif message["role"] == "button_everytime_3":
            if st.session_state.button_visible_subject:
                random_float_np = np.random.uniform(0, max_float)
                st.button(message["content"], on_click=run_everytime_review_page_3, key="everytime_review_key_3"+str(random_float_np))
        

    # ================================== 사용자 입력 및 LLM 답변 출력 ===============================
    # 사용자 입력창 추가
    # user_question 에 저장됨
    # st.chat_message("user") 를 통해 user의 바 생성하고 st.wrie()를 통해 텍스트 출력
    # user은 "role" 로 저장됨
    # with를 사용해써 해당 바 안에 텍스트 넣음
    if user_question := st.chat_input(placeholder="교과목 관련해 질문해 주세요😀"):
        with st.chat_message("user"):
            st.write(user_question)
            st.session_state.message_list_subject.append({"role":"user", "content":user_question})

        with st.spinner("답변을 생성하는 중입니다😊"):
            user_question_precleaning=question_retriever_routing_aun_subject.f_question_precleaning(user_question)
            retriever_var, prompt_var, flag_sort_chunk, flag_link=question_retriever_routing_aun_subject.f_retriever_routing(user_question_precleaning)
            prompt_chain=chain.f_chain(retriever_var, prompt_var, flag_sort_chunk)
            llm_model=llm_model.f_OpenAI_llm_model()
            total_chain=prompt_chain | llm_model | StrOutputParser()    
            ai_message=total_chain.invoke({"question":user_question_precleaning})
        with st.chat_message("ai"):
            # 스트림을 write_stream으로 출력
            answer = ai_message if isinstance(ai_message, str) else "No Answer Available."
            st.write_stream(stream_data)
            st.session_state.message_list_subject.append({"role":"ai", "content":ai_message})
            print(flag_link)

            # 에타 강의평
            if flag_link==2:
                # 데이터 로딩
                everytime_drop=pd.read_csv("streamlit구현/dataset/에브리타임 강의평, 평균별점, 리뷰개수, 긍부정, LLM키워드(중복 제거X).csv")
                everytime_drop=everytime_drop.drop_duplicates(subset=["교과목명", "담당교수"])

                # 추출된 교과목명과 담당교수 리스트
                subject_professor_pairs = []
                result_everytime_sub_pro_1=[]
                result_everytime_sub_pro_2=[]
                result_everytime_sub_pro_3=[]

                # 응답 데이터를 줄 단위로 나누기
                lines = ai_message.splitlines()

                # 교과목명과 담당교수 추출
                for line in lines:
                    if "교과목명" in line:
                        for y in everytime_drop["교과목명"]:
                            if y in line:
                                subject = y
                                break  # 교과목명이 발견되면 반복 종료
                    elif "담당교수" in line:
                        for z in everytime_drop["담당교수"]:
                            if z in line:
                                professor = z
                                break  # 교수명이 발견되면 반복 종료
                    
                    # 교과목명과 담당교수가 모두 발견된 경우에만 쌍 추가
                    if subject and professor:
                        subject_professor_pairs.append([subject, professor])
                        # 교과목명과 담당교수 초기화
                        subject = ""
                        professor = ""

                # 추출된 쌍 저장
                result_everytime_sub_pro_1 = subject_professor_pairs[0] if len(subject_professor_pairs) > 0 else []
                result_everytime_sub_pro_2 = subject_professor_pairs[1] if len(subject_professor_pairs) > 1 else []
                result_everytime_sub_pro_3 = subject_professor_pairs[2] if len(subject_professor_pairs) > 2 else []

                # 저장
                with open('everytime_sub_pro_1.txt', 'w') as f:
                    f.write(str(result_everytime_sub_pro_1))
                with open('everytime_sub_pro_2.txt', 'w') as f:
                    f.write(str(result_everytime_sub_pro_2))
                with open('everytime_sub_pro_3.txt', 'w') as f:
                    f.write(str(result_everytime_sub_pro_3))
                
        # flag_link 가 2라면 에타 (최대 3개)
        if flag_link==2:
            # 첫 번째 조건: a의 길이가 1 이상일 때
            if len(result_everytime_sub_pro_1) > 0:
                sub_1=result_everytime_sub_pro_1[0]
                pro_1=result_everytime_sub_pro_1[1]
                button_str_1 = "📖"+sub_1 + "🧑‍🏫" +pro_1 + " 교수님"
                st.session_state.button_visible_subject = True
                st.session_state.message_list_subject.append({"role": "button_everytime_1", "content": button_str_1})
                st.button(button_str_1, on_click=run_everytime_review_page_1)
            
            # 두 번째 조건: a와 b의 길이가 1 이상일 때
            if len(result_everytime_sub_pro_1) > 0 and len(result_everytime_sub_pro_2) > 0:
                sub_2=result_everytime_sub_pro_2[0]
                pro_2=result_everytime_sub_pro_2[1]
                button_str_2 = "📖"+sub_2 + "🧑‍🏫" +pro_2 + " 교수님"
                st.session_state.button_visible_subject = True
                st.session_state.message_list_subject.append({"role": "button_everytime_2", "content": button_str_2})
                st.button(button_str_2, on_click=run_everytime_review_page_2)

            # 세 번째 조건: a, b, c 모두의 길이가 1 이상일 때
            if len(result_everytime_sub_pro_1) > 0 and len(result_everytime_sub_pro_2) > 0 and len(result_everytime_sub_pro_3) > 0:
                sub_3=result_everytime_sub_pro_3[0]
                pro_3=result_everytime_sub_pro_3[1]
                button_str_3 = "📖"+sub_3 + "🧑‍🏫" +pro_3 + " 교수님"
                st.session_state.button_visible_subject = True
                st.session_state.message_list_subject.append({"role": "button_everytime_3", "content": button_str_3})
                st.button(button_str_3, on_click=run_everytime_review_page_3)