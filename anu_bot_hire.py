# anu_bot_hire.py
# 채용정보, 리뷰 관련 파일

def anu_bot_hire():
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
    import retriever
    import chain
    import sidebar_info
    import emoji_moving
    import question_retriever_routing_jumpit_wanted

    # =============================================== 함수 ====================================================
    # 다른 .py 파일 실행 (회사 리뷰)
    def run_jumpit_wanted_review_page():
        time.sleep(1)
        subprocess.Popen(["streamlit", "run", "Streamlit구현/jumpit_wanted_review.py"])

    # 스트림형식으로 바꾸기
    def stream_data():
        for word in answer.split(" "):
            yield word + " "
            time.sleep(0.06) 

    # ================================== 변수 ====================================
    flag_link=0
    llm_answer_jumpit_wanted_name=[]
    llm_answer_jumpit_wanted_review_count=[]
    max_float = sys.float_info.max
    button_jumpit_wanted_review = 0  # 또는 False로 설정하여 비활성화
    
    # ================================== 페이지 가장 위에 이모지 애니메이션 =================================
    st.components.v1.html(emoji_moving.f_emoji_moving_bee(), height=42)

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
        if st.button("🍁대화내용삭제🍁"):
            st.session_state.message_list_jumpit_wanted=[]
            
    # ========================== session_state 가 비어있다면 빈 리스트 저장, False 값 저장 =============================
    # st.session_state 는 전역변수 느낌
    # 비어있다면 빈 리스트를 저장하고, 채팅 할때마다 "role" 과 "content"를 딕셔너리로 append함
    if "message_list_jumpit_wanted" not in st.session_state:
        st.session_state.message_list_jumpit_wanted=[]

    if "button_visible_jumpit_wanted" not in st.session_state:
        st.session_state.button_visible_jumpit_wanted = False
        
    # ========================== session_state 를 돌면서 내용을 write함 =============================
    for message in st.session_state.message_list_jumpit_wanted:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        elif message["role"] == "ai":
            with st.chat_message("ai"):
                st.write(message["content"])
        elif message["role"] == "button_factory":
            if st.session_state.button_visible_jumpit_wanted:
                random_float_np = np.random.uniform(0, max_float)
                st.button(message["content"]+"  리뷰 분석 결과🔎", on_click=run_jumpit_wanted_review_page, key="factory_review_key"+str(random_float_np))

    # ========================== session_state 를 돌면서 내용을 write함 =============================
    # for message in st.session_state.message_list:
    #     with st.chat_message(message["role"]):
    #         st.write(message["content"])


    # ================================== 사용자 입력 및 LLM 답변 출력 ===============================
    # 사용자 입력창 추가
    # user_question 에 저장됨
    # st.chat_message("user") 를 통해 user의 바 생성하고 st.wrie()를 통해 텍스트 출력
    # user은 "role" 로 저장됨
    # with를 사용해써 해당 바 안에 텍스트 넣음
    if user_question := st.chat_input(placeholder="채용/회사 관련해 질문해 주세요😀"):
        with st.chat_message("user"):
            st.write(user_question)
            st.session_state.message_list_jumpit_wanted.append({"role":"user", "content":user_question})

        with st.spinner("답변을 생성하는 중입니다😊"):
            user_question_precleaning=question_retriever_routing_jumpit_wanted.f_question_precleaning(user_question)
            retriever_var, prompt_var, flag_sort_chunk, flag_link=question_retriever_routing_jumpit_wanted.f_retriever_routing(user_question_precleaning)
            prompt_chain=chain.f_chain(retriever_var, prompt_var, flag_sort_chunk)
            llm_model=llm_model.f_OpenAI_llm_model()
            total_chain=prompt_chain | llm_model | StrOutputParser()    
            ai_message=total_chain.invoke({"question":user_question_precleaning})
        with st.chat_message("ai"):
            # 스트림을 write_stream으로 출력
            answer = ai_message if isinstance(ai_message, str) else "No Answer Available."
            st.write_stream(stream_data)
            st.session_state.message_list_jumpit_wanted.append({"role":"ai", "content":ai_message})
            print(flag_link)
            # 회사 추출하기
            if flag_link==1:
                # LLM의 답변에서 회사명 추출하기
                jumpit_wanted_drop=pd.read_csv("streamlit구현/dataset/점핏_원티드_리뷰_전처리완료(중복 제거O)(한줄요약) (final).csv")
                for x in jumpit_wanted_drop.index:
                    if jumpit_wanted_drop.loc[x, "회사명"] in ai_message:
                        llm_answer_jumpit_wanted_name.append(jumpit_wanted_drop.loc[x, "회사명"])
                        llm_answer_jumpit_wanted_review_count.append(jumpit_wanted_drop.loc[x, "리뷰개수"])
                        print(llm_answer_jumpit_wanted_name, llm_answer_jumpit_wanted_review_count)
                        button_jumpit_wanted_review=1
                        if len(llm_answer_jumpit_wanted_name)>=1:
                            with open('junmpit_wanted_name.txt', 'w') as f:
                                f.write(str(llm_answer_jumpit_wanted_name))

        # flag_link 가 1이면 회사리뷰
        if flag_link==1:
            factory_name="🌈"+llm_answer_jumpit_wanted_name[0]
            st.session_state.button_visible_jumpit_wanted = True
            st.session_state.message_list_jumpit_wanted.append({"role": "button_factory", "content": factory_name})
            st.button(factory_name+"  리뷰 분석 결과🔎", on_click=run_jumpit_wanted_review_page)

            