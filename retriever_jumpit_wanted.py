# retriever_jumpit_wanted.py 
# 채용정보 관련 리트리버

# ======================================= 점핏, 원티드 채용정보 ============================
def f_retriever_jumpit_wanted_information(db):
    retriever_jumpit_wanted_information=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 5,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.8, 
            "filter" : dict(
                source='C:/최종 프로젝트/데이터셋/점핏_원티드_세부테이터_링크붙임_DB에 넣을 것(final).csv'
            )
        }
    )

    return retriever_jumpit_wanted_information

def f_jumpit_wanted_information_prompt():
    prompt_template_jumpit_wanted_information="""
        다음은 회사(기업)들의 채용 정보 입니다.
        출처는 원티드(wanted), 점핏(jumpit) 사이트 입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question} 
        1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요:
            - 회사를 숫자로 구분해서 사용자가 잘 알아볼 수 있도록 출력해주세요.
            - 회사명, 제목, 회사위치, 주요업무, 자격요건, 우대사항, 복지 및 혜택은 이모지를 사용해 출력해주세요.
            - 주요업무, 자격요건, 우대사상, 복지 및 혜택은 요약해서 짧게 출력해주세요.
            - 자세한 채용공고는 링크를 통해 확인할 수 있다는 문구와 함께 "채용공고 링크" 를 이모지와 함께 출력해주세요.
        2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
        모든 답변은 반드시 이모지를 사용해서 출력해주세요.
    """
    return prompt_template_jumpit_wanted_information

# ======================================= 점핏, 원티드 리뷰 ================================
def f_retriever_jumpit_wanted_review(db):
    retriever_jumpit_wanted_review=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 1,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.8, 
            "filter" : dict(
                source='C:/최종 프로젝트/데이터셋/점핏_원티드_리뷰(중복 제거O) (final).csv'
            )
        }
    )

    return retriever_jumpit_wanted_review

def jumpit_wanted_review_prompt():
    prompt_template_jumpit_wanted_review="""
        다음은 채용사이트의 회사(기업)들에 대한 평균별점, 평균연봉입니다.
        출처는 잡플래닛(jobplanet) 사이트 입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question}
        
        1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하고, 출력의 마지막에는 출력의 마지막에는 '자세한 회사 리뷰는 링크를 통해 확인할 수 있습니다! 🔗📝' 라는 문구를 반드시 출력해 주세요.
            - 회사명, 평균별점, 평균연봉을 출력해주세요.
        2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
        모든 답변은 반드시 이모지를 사용해서 출력해주세요.
    """
    return prompt_template_jumpit_wanted_review

# ======================================= 그 외 (점핏, 원티드 채용공고+리뷰)  ======================================
def f_retriever_jumpit_wanted_total(db):
    retriever_jumpit_wanted_total=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 2,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.8, 
            "filter" : dict(
                source=[
                    'C:/최종 프로젝트/데이터셋/점핏_원티드_세부테이터_링크붙임_DB에 넣을 것(final).csv',
                    'C:/최종 프로젝트/데이터셋/점핏_원티드_리뷰(중복 제거O) (final).csv',
                ]
            )
        }
    )

    return retriever_jumpit_wanted_total

def f_jumpit_wanted_total_prompt():
    prompt_template_jumpit_wanted_total = """
        다음은 회사(기업)들의 채용 정보에 관한 전반적인 정보입니다.
        학사일정,  통학버스(스쿨버스),  전화번호(번호),  동아리,  취업률,  취업처,  학칙,  기숙사(생활관)(솔뫼관)(솔빛관)(가람관)에 대한 정보는 절대 포함하지 않는 정보입니다.
        교과목(강의) 정보, 교과목(강의) 추천, 강의평(리뷰)에 대한 정보는 절대 포함하지 않는 정보입니다 . :
        {context}
        다음은 사용자의 질문입니다.
        {question}
        지침:
        1. 사용자의 질문이 학사일정, 통학버스(스쿨버스), 전화번호, 동아리, 취업률, 취업처, 학칙, 기숙사(생활관)(솔뫼관)(솔빛관)(가람관) 에 해당된다면 "안동대학교 정보" 탭으로 이동하여 질문하도록 유도하세요.
        2. 사용자의 질문이 교과목(강의) 정보, 교과목(강의) 추천, 강의평(리뷰)에 관한 것이라면, "교과목 정보" 탭으로 이동하여 질문하도록 유도하세요.
        3. 1, 2번에서 제시된 내용이 아니고, 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요. 
        4. 1, 2번에서 제시된 내용이 아니고, 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.
        5. "당신은 누구인가요?", 와 같은 본인을 소개하는 질문일때만, 아래와 같이 자신을 소개하세요:

            ✅ 저는 안동대학교에 대해 알려주는 "아누봇"입니다.
            ✅ 저는 안동대학교에 대한 전반적인 정보 제공, 교과목 추천, 채용정보 추천을 담당합니다.
            ✅ 저는 아래 학생들에 의해 개발되었습니다:
            
                - 안동대학교 전자공학과 장지원
                - 안동대학교 전자공학과 김수빈
                - 안동대학교 정보통계학과 구대연
                - 안동대학교 경제학과 윤재성
                
        모든 답변은 반드시 이모지를 사용해서 출력해주세요.
    """
    return prompt_template_jumpit_wanted_total