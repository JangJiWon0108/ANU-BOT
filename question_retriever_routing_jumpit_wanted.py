# question_retriever_routing_jumpit_wanted.py
# 채용공고, 리뷰에 대해 질문 전처리를 하고, 리트리버 라우팅을 하는 파일
import retriever_jumpit_wanted

# ====================================== 질문 전처리 ======================================
def f_question_precleaning(question):
    pass
    return question

# ====================================== 리트리버 라우팅 ======================================
def f_retriever_routing(question):
    import retriever_jumpit_wanted
    import vector_DB
    import embedding_model

    # 임베딩 모델이랑 벡터 DB
    embedding=embedding_model.f_upstage_embedding_model()
    db=vector_DB.f_faiss_vertorDB_upstage(embedding)

    # 질문 필터링
    retriever_routing_jumpit_wanted_review_list=["리뷰", "연봉"]
    retriever_routing_jumpit_wanted_information_list=["회사", "기업", "채용", "채용정보", "채용 정보"]  

    # 변수
    flag_value=0    
    flag_sort_chunk=0
    flag_link=0 # 0이면 안함, 1이면 회사, 2면 에타 (링크)


    # 점핏 원티드 리뷰
    if flag_value==0:
        for x in retriever_routing_jumpit_wanted_review_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=1
                print("리트리버 : 점핏, 원티드 - 리뷰, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever_jumpit_wanted.f_retriever_jumpit_wanted_review(db)
                prompt_template=retriever_jumpit_wanted.jumpit_wanted_review_prompt()
                break

    # 점핏 원티드 채용 정보
    if flag_value==0:
        for x in retriever_routing_jumpit_wanted_information_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=0
                print("리트리버 : 점핏, 원티드 - 채용정보, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever_jumpit_wanted.f_retriever_jumpit_wanted_information(db)
                prompt_template=retriever_jumpit_wanted.f_jumpit_wanted_information_prompt()
                break
    # 그 외 (채용+리뷰)
    if flag_value==0:
        current_retriever=retriever_jumpit_wanted.f_retriever_jumpit_wanted_total(db)
        prompt_template=retriever_jumpit_wanted.f_jumpit_wanted_total_prompt()
        flag_value=1
        flag_sort_chunk=0
        flag_link=0
        print("리트리버 : 그 외(점핏, 원티드 채용정보+리뷰), 청크 정렬 : {}".format(flag_sort_chunk))

    # 리트리버랑 프롬프트 리턴
    return current_retriever, prompt_template, flag_sort_chunk, flag_link