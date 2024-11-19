# question_retriever_routing_anu_subject.py
# 안동대 교과목 혹은 에타 강의평에 대해 질문 전처리를 하고, 리트리버 라우팅을 하는 파일

# retriever_anu_subject 모듈 임포트
import retriever_anu_subject

# ====================================== 질문 전처리 ======================================
def f_question_precleaning(question):
    pass
    return question

# ====================================== 리트리버 라우팅 ======================================
def f_retriever_routing(question):
    import retriever_anu_subject
    import vector_DB
    import embedding_model

    # 임베딩 모델이랑 벡터 DB
    embedding=embedding_model.f_upstage_embedding_model()
    db=vector_DB.f_faiss_vertorDB_upstage(embedding)

    # 질문 필터링
    retriever_routing_anu_everytime_list=["강의평", "강의 평", "리뷰"]
    retriever_routing_anu_subject_list=["교과목", "교 과목", "과목", "수업", "강의"]

    flag_value=0
    flag_sort_chunk=0
    flag_link=0 # 0이면 안함, 1이면 회사, 2면 에타 (링크)

    # 에브리타임 강의평
    if flag_value==0:
        for x in retriever_routing_anu_everytime_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=2
                print("리트리버 : 안동대 교과목 - 에타 강의평, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever_anu_subject.f_retriever_anu_everytime(db)
                prompt_template=retriever_anu_subject.f_anu_everytime_prompt()
                break
    # 안동대 교과목
    if flag_value==0:
        for x in retriever_routing_anu_subject_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=0
                print("리트리버 : 안동대 교과목 - 교과목정보, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever_anu_subject.f_retriever_anu_subject(db)
                prompt_template=retriever_anu_subject.f_anu_subject_prompt()
                break
    # 그 외(교과목+강의평)
    if flag_value==0:
        current_retriever=retriever_anu_subject.f_retriever_anu_subject_total(db)
        prompt_template=retriever_anu_subject.f_anu_subject_total_prompt()
        flag_value=1
        flag_sort_chunk=0
        flag_link=0
        print("리트리버 : 그 외(교과목+에타강의평), 청크 정렬 : {}".format(flag_sort_chunk))

    # 리트리버랑 프롬프트 리턴
    return current_retriever, prompt_template, flag_sort_chunk, flag_link