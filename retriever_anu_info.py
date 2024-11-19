# retriever_anu_info.py 
# 학교 정보 리트리버 파일

# ======================================= 학사 일정 ========================================
def f_retriever_anu_shedule(db):
    retriever_anu_shedule=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 1,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.5, 
            "filter" : dict(
                source='C:/최종 프로젝트/데이터셋/안동대-2024학년도-학사일정.docx'
            )
        }
    )
    return retriever_anu_shedule

def f_anu_shedule_prompt():
    prompt_template_anu_shedule="""
    다음은 안동대학교의 2024년 학사일정에 대한 정보입니다.
    {context}
    다음은 사용자의 질문입니다.
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}

    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
        - 특정 월을 질문할 경우 (예시 : 9월 학사일정을 알려주세요) 해당 월의 모든 일정(날짜)을 출력해주세요.
        - 특정 행사를 질문할 경우 (예시 : 수강신청기간을 알려주세요) 해당 사건의 일정(날짜)만 출력해주세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.
    
    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    return prompt_template_anu_shedule

# ======================================= 전화번호 =========================================
def f_retriever_anu_phone(db):
    retriever_anu_phone=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 2,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.5, 
            "filter" : dict(
                source='C:/최종 프로젝트/최종 RAG 구성 및 LLM/안동대학교 전화번호.csv'
            )
        }
    )
    return retriever_anu_phone

def f_anu_phone_prompt():
    prompt_template_anu_phone="""
    다음은 안동대학교의 전화번호 정보입니다.
    {context}
    다음은 사용자의 질문입니다.
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    return prompt_template_anu_phone

# ======================================= 취업률 ===========================================
def f_retriever_anu_employment_rate(db):
    retriever_anu_employment_rate=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 3,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.5, 
        "filter" : dict(
                source='C:/최종 프로젝트/최종 RAG 구성 및 LLM/2021~2023년 안동대 취업률, 졸업학점, 취업처.docx'
            )
        }
    )
    return retriever_anu_employment_rate

def f_anu_employment_rate_prompt():
    prompt_template_anu_employment_rate="""
    다음은 2021년, 2022년, 2023년 의 안동대학교 학과(전공)별 취업률과 졸업학점입니다.
    또한 2023년 안동대학교 학과(전공)별 주요 취업처입니다.
    "학과" 은 전자공학과, 컴퓨터공학과, 정보통계학과와 같이 학과(전공)을 구별합니다.
    "취업률" 은 학과(전공)별 취업률(단위:퍼센트)를 나타냅니다.
    "졸업 학점 평균" 은 학과(전공)별 졸업 학점 평균을 나타냅니다. 
    "취업처"는 학과(전공)별로 취업한 학생들의 주요 취업처를 나타냅니다.
    "직무"는 해당되는 취업처에서의 직무를 나타냅니다.

    {context}
    다음은 사용자의 질문입니다.
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    return prompt_template_anu_employment_rate

# ====================================== 통학버스 ================================
def f_retriever_anu_bus(db):
    retriever_anu_bus=db.as_retriever(
        search_type = "mmr",
        search_kwargs={
            "k" : 1,
            "fetch_k" : 54,
            "lambda_mult":0.5,
            "filter" : dict(
                source='C:/최종 프로젝트/데이터셋/통학버스안내.docx'
            )
        }
    )

    return retriever_anu_bus

def f_anu_bus_prompt():
    prompt_template_anu_bus="""
    다음은 안동대학교 통학버스 관련된 정보입니다:
    {context}
    사용자의 질문:
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""

    return prompt_template_anu_bus

# =================================== 생활관(기숙사) ================================
def f_retriever_anu_dormitory(db):
    retriever_anu_dormitory=db.as_retriever(
        search_type = "mmr",
        search_kwargs={
            "k" : 3,
            "fetch_k" : 54,
            "lambda_mult":0.5,
            "filter" : dict(
                source='C:/최종 프로젝트/데이터셋/안동대생활관내용.docx'
            )
        }
    )

    return retriever_anu_dormitory

def f_anu_dormitory_prompt():
    prompt_template_anu_dormitory = """
    당신은 안동대학교 기숙사에 대한 정보를 제공하는 전문가입니다.
    다음은 관련된 정보입니다:
    {context}
    사용자의 질문:
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    
    return prompt_template_anu_dormitory


# =================================== 총동아리연합회 ================================
def f_retriever_anu_club(db):
        retriever_anu_club=db.as_retriever(
            search_type = "mmr",
            search_kwargs={
                "k" : 3,
                "fetch_k" : 54,
                "lambda_mult":0.5,
                "filter" : dict(
                    source='C:/최종 프로젝트/데이터셋/총동아리연합회정보.docx'
                )
            }
        )

        return retriever_anu_club

def f_anu_club_prompt():
    prompt_template_anu_club = """
    다음은 안동대학교 동아리에 대한 정보입니다.
    {context}
    다음은 사용자의 질문입니다.
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""

    return prompt_template_anu_club

# =================================== 안동대학칙 ================================
def f_retriever_anu_rule(db):
        retriever_anu_rule=db.as_retriever(
            search_type = "mmr",
            search_kwargs={
                "k" : 3,
                "fetch_k" : 54,
                "lambda_mult":0.5,
                "filter" : dict(
                    source='C:/최종 프로젝트/데이터셋/국립안동대학교학칙.docx'
                )
            }
        )

        return retriever_anu_rule

def f_anu_rule_prompt():
    prompt_template_anu_rule = """
    다음은 국립안동대학교학칙에 대한 정보입니다.
    {context}
    
    다음은 사용자의 질문입니다.
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    
    return prompt_template_anu_rule

# =================================== 통계연보 ================================
def f_retriever_anu_stat(db):
        retriever_anu_stat=db.as_retriever(
            search_type = "mmr",
            search_kwargs={
                "k" : 3,
                "fetch_k" : 54,
                "lambda_mult":0.5,
                "filter" : dict(
                    source='C:/최종 프로젝트/데이터셋/2023안동대학교통계연보.docx'
                )
            }
        )

        return f_retriever_anu_stat

def f_anu_stat_prompt():
    prompt_template_anu_stat="""
    다음은 안동대학교 통계연보에 대한 정보입니다:
    {context}

    사용자의 질문:
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
    {question}
    
    1. 해당 질문에 대한 정보가 {context} 에 있다면 정확히 답변을 제공하세요.
    2. 해당 질문에 대한 정보가 {context} 에 없다면 해당되는 정보가 없다고 알리고, 정확하지 않은 답변은 하지 마세요.

    각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    모든 대답은 이모지를 사용해서 예쁘게 출력해주세요.
"""
    
    return prompt_template_anu_stat

# =================================== 조직 및 업무 ================================
def f_retriever_anu_organization(db):
        retriever_anu_organization=db.as_retriever(
            search_type = "mmr",
            search_kwargs={
                "k" : 3,
                "fetch_k" : 54,
                "lambda_mult":0.5,
                "filter" : dict(
                    source='C:/최종 프로젝트/데이터셋/안동대학교_조직및업무.docx'
                )
            }
        )

        return retriever_anu_organization

def f_anu_organization_prompt():
    prompt_template_anu_organization="""
    안녕하세요! 무엇을 도와드릴까요?

    당신은 사용자들이 안동대학교의 교내 조직에 대해 도움을 받을 수 있도록 돕는 챗봇입니다.
    당신은 교내의 부서 정보, 연락처, 업무에 대한 종합적인 지식을 가지고 있습니다.
    {context}
    사용자 질문: {question}
    만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.

    교무처에 대한 정보를 제공해주세요:

    1. **부서 기본 정보:**
        - [부서명, 부서설명 제공]

    2. **연락처 및 기타정보:**
        - [부서의 연락처 및 기타 연락 정보 설명]

    3. **주요 책임:**
        - [직무의 주요 책임 나열]

    4. **업무 절차:**
        - [업무 과정의 단계 상세 설명]

    5. **연관 부서 정보:**
        - [부서에 연관된 타 부서 연락처 나열]

    6. **선호 부서 정보:**
        - [추가적으로 선호되는 부서 연락처 나열]

    사용자가 데이터베이스에 저장되지 않은 정보를 문의할 경우, 다음과 같이 응답하세요:
    - "죄송합니다만, 현재 해당 정보를 가지고 있지 않습니다. 추가적인 도움은 총무과 이메일 chongmoo@anu.ac.kr로 문의해주세요."
    - "다른 질문이나 추가적인 도움이 필요하시면, 총무과 이메일 chongmoo@anu.ac.kr로 문의해주세요."

    참고: 모든 [ ]로 표시된 부분은 특정 회사의 세부 정보로 채워야 합니다. 또한 이모지를 사용해서 답해주세요.
    """
    
    return prompt_template_anu_organization

# ====================================== 그 외 (안동대 정보 전체) ===================================
def f_retriever_anu_info_total(db):
    retriever_anu_total=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 2,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.5, 
            "filter" : dict(
                source=[
                    'C:/최종 프로젝트/데이터셋/안동대-2024학년도-학사일정.docx',
                    'C:/최종 프로젝트/최종 RAG 구성 및 LLM/안동대학교 전화번호.csv',
                    'C:/최종 프로젝트/최종 RAG 구성 및 LLM/2021~2023년 안동대 취업률, 졸업학점, 취업처.docx',
                    'C:/최종 프로젝트/데이터셋/통학버스안내.docx',
                    'C:/최종 프로젝트/데이터셋/안동대생활관내용.docx',
                    'C:/최종 프로젝트/데이터셋/총동아리연합회정보.docx',
                    'C:/최종 프로젝트/데이터셋/국립안동대학교학칙.docx',
                    'C:/최종 프로젝트/데이터셋/2023안동대학교통계연보.docx',
                    'C:/최종 프로젝트/데이터셋/안동대학교_조직및업무.docx',
                ]
            )
        }
    )

    return retriever_anu_total

def f_anu_info_total_prompt():
    prompt_template_anu_total = """
        다음은 안동대학교에 대한 전반적인 정보입니다.
        {context}
        다음은 사용자의 질문입니다. 
        만약 사용자가 안동대학교가 아닌 다른 대학교에 대해 질문한다면, 알려줄 수 없음을 알리고, 안동대학교와 관련하여 질문하도록 유도하세요.
        
        {question}
        지침:
        1. 사용자의 질문이 교과목(강의) 정보, 교과목(강의) 추천, 강의평(리뷰)에 관한 것이라면, "교과목 정보" 탭으로 이동하여 질문하도록 유도하세요.
        2. 사용자의 질문이 채용(회사)(기업) 정보, 채용(회사)(기업) 추천, 회사(기업) 리뷰에 해당된다면,  "채용공고 정보" 탭으로 이동하여 질문하도록 유도하세요.
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

        6. 모든 답변은 이모지를 사용해서 예쁘게 출력해주세요. 

    """

    return prompt_template_anu_total
