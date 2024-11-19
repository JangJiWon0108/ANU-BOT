# question_retriever_routing.py
# 질문에 대해서 질문 전처리를 하고, 리트리버 라우팅을 하는 파일
import retriever

# ====================================== 질문 전처리 ======================================
def f_question_precleaning(question):
    pass
    return question

# ====================================== 리트리버 라우팅 ======================================
def f_retriever_routing(question):
    import retriever
    import vector_DB
    import embedding_model

    # 임베딩 모델이랑 벡터 DB
    embedding=embedding_model.f_upstage_embedding_model()
    db=vector_DB.f_faiss_vertorDB_upstage(embedding)

    retriever_routing_anu_phone_list=["전화번호", "전화 번호", "번호"]                                       # 전화번호
    retriever_routing_anu_shedule_list=["학사일정", "학사 일정", "기간", "기한", "일정"]                     # 학사일정
    retriever_routing_anu_employment_rate_list=["취업률", "졸업학점"]                                        # 취업률
    retriever_routing_anu_bus_list=["노선", "버스", "통학버스", "통학 버스", "스쿨버스", "스쿨 버스"]        # 통학버스
    retriever_routing_anu_dormitory_list=["기숙사", "생활관", "가람관", "솔뫼관", "솔빛관"]                  # 기숙사
    retriever_routing_anu_club_list=["총동아리", "동아리"]                                                   # 동아리
    retriever_routing_anu_rule_list=["학칙", "개교기념일", "개교 기념일"]                                                                 # 학칙
    retriever_routing_anu_stat_list=["통계연보"]                                                             # 통계연보
    retriever_routing_anu_anu_organization_list=["조직및업무", "조직 및 업무"]                               # 조직 및 업무
    retriever_routing_anu_everytime_list=["강의평", "강의 평", "에브리타임", "에타", "에브리 타임"]          # 에타 강의평
    retriever_routing_jumpit_wanted_review_list=["리뷰", "연봉"]                                             # 회사 리뷰
    retriever_routing_anu_subject_list=["교과목", "교 과목", "과목", "수업", "강의"]                         # 교과목
    retriever_routing_jumpit_wanted_information_list=["회사", "기업", "채용", "채용정보", "채용 정보"]       # 채용정보

    flag_value=0
    flag_sort_chunk=0
    flag_link=0 # 0이면 안함, 1이면 회사, 2면 에타 (링크)

    # 전화번호
    for x in retriever_routing_anu_phone_list:
        if x in question:
            flag_value=1
            flag_sort_chunk=0
            flag_link=0
            print("리트리버 : 학교 전화번호, 청크 정렬 : {}".format(flag_sort_chunk))
            current_retriever=retriever.f_retriever_anu_phone(db)
            prompt_template=retriever.f_anu_phone_prompt()
            break
    # 학사일정
    if flag_value==0:
        for x in retriever_routing_anu_shedule_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 학교 학사일정, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_shedule(db)
                prompt_template=retriever.f_anu_shedule_prompt()
                break
    # 취업률
    if flag_value==0:
        for x in retriever_routing_anu_employment_rate_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 학교 취업률, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_employment_rate(db)
                prompt_template=retriever.f_anu_employment_rate_prompt()
                break
    # 통학버스
    if flag_value==0:
        for x in retriever_routing_anu_bus_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 통학버스, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_bus(db)
                prompt_template=retriever.f_anu_bus_prompt()
                break
    # 기숙사
    if flag_value==0:
        for x in retriever_routing_anu_dormitory_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 기숙사, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_dormitory(db)
                prompt_template=retriever.f_anu_dormitory_prompt()
                break
    # 동아리
    if flag_value==0:
        for x in retriever_routing_anu_club_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 기숙사, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_club(db)
                prompt_template=retriever.f_anu_club_prompt()
                break
    # 학칙
    if flag_value==0:
        for x in retriever_routing_anu_rule_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 학칙, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_rule(db)
                prompt_template=retriever.f_anu_rule_prompt()
                break
    # 통계연보
    if flag_value==0:
        for x in retriever_routing_anu_stat_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 통계연보, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_stat(db)
                prompt_template=retriever.f_anu_stat_prompt()
                break
    # 조직 및 업무
    if flag_value==0:
        for x in retriever_routing_anu_anu_organization_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=0
                print("리트리버 : 조직및업무, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_organization(db)
                prompt_template=retriever.f_anu_organization_prompt()
                break
    # 에브리타임 강의평
    if flag_value==0:
        for x in retriever_routing_anu_everytime_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=2
                print("리트리버 : 에타 강의평, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_everytime(db)
                prompt_template=retriever.f_anu_everytime_prompt()
                break
    # 점핏 원티드 리뷰
    if flag_value==0:
        for x in retriever_routing_jumpit_wanted_review_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=0
                flag_link=1
                print("리트리버 : 회사 리뷰, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_jumpit_wanted_review(db)
                prompt_template=retriever.jumpit_wanted_review_prompt()
                break
    # 안동대 교과목
    if flag_value==0:
        for x in retriever_routing_anu_subject_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=0
                print("리트리버 : 안동대 교과목 정보, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_anu_subject(db)
                prompt_template=retriever.f_anu_subject_prompt()
                break
    # 점핏 원티드 채용 정보
    if flag_value==0:
        for x in retriever_routing_jumpit_wanted_information_list:
            if x in question:
                flag_value=1
                flag_sort_chunk=1
                flag_link=0
                print("리트리버 : 회사 채용정보, 청크 정렬 : {}".format(flag_sort_chunk))
                current_retriever=retriever.f_retriever_jumpit_wanted_information(db)
                prompt_template=retriever.f_jumpit_wanted_information_prompt()
                break
    # 그 외
    if flag_value==0:
        current_retriever=retriever.f_retriever_else(db)
        prompt_template=retriever.f_else_prompt()
        flag_value=1
        flag_sort_chunk=0
        flag_link=0
        print("리트리버 : 그 외, 청크 정렬 : {}".format(flag_sort_chunk))

    # 리트리버랑 프롬프트 리턴
    return current_retriever, prompt_template, flag_sort_chunk, flag_link