# retriever.py 
# 각 리트리버 및 프롬프트 정의하는 파일

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
        다음은 안동대학교 2024년, 2025년 2월의 학사일정에 대한 정보입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question}
        당신은 안동대학교 2024년 학사일정을 알려주는 최고의 전문가입니다.
        특정 월을 질문할 경우 (예시 : 9월 학사일정을 알려주세요) 해당 월의 모든 일정(날짜)을 출력해주세요.
        특정 행사를 질문할 경우 (예시 : 수강신청기간을 알려주세요) 해당 사건의 일정(날짜)만 출력해주세요.
        이모지를 사용해서 예쁘게 출력해주세요.
        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
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
        {question}
        당신은 안동대학교 전화번호를 알려주는 최고의 전문가입니다.
        해당되는 전화번호를 출력해주세요.
        이모지를 사용해서 예쁘게 출력해주세요.
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
        {question}
        질문에 해당되는 취업률, 졸업 학점 평균을 정확하게 계산해서 출력해주세요.
        이모지를 사용해서 예쁘게 출력해주세요.
    """
    return prompt_template_anu_employment_rate

# ======================================= 안동대 교과목 ====================================
def f_retriever_anu_subject(db):
    retriever_anu_subject=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 5,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.7, 
            "filter" : dict(
                source='C:/최종 프로젝트/최종 RAG 구성 및 LLM/벡터DB에 넣을 안동대 교과목정보_final.csv'
            )
        }
    )

    return retriever_anu_subject

def f_anu_subject_prompt():
    prompt_template_anu_subject="""
        다음은 대학교 교과목에 대한 정보입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question}
        당신은 안동대학교 교과목을 추천해주는 최고의 전문가입니다.
        가벼운 인사말로 출력을 시작해주세요. 
        교과목번호는 사용자가 물어보지않으면 출력하지 마세요.
        해당되는 교과목에 대해 친절하게 출력해주세요. 교과목의 경우 최대 3개 출력해 주세요.
        이모지를 사용해서 예쁘게 출력해주세요.
        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
    """
    return prompt_template_anu_subject

# ======================================= 에브리타임 강의평 ================================
def f_retriever_anu_everytime(db):

    retriever_anu_everytime=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 6,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.7, 
            "filter" : dict(
                source='C:/최종 프로젝트/최종 RAG 구성 및 LLM/에브리타임 강의평, 평균별점 정보(중복 제거O).csv'
            )
        }
    )
    return retriever_anu_everytime

def f_anu_everytime_prompt():
    prompt_template_anu_everytime="""
        다음은 대학교 교과목에 대한 정보입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question}
        당신은 안동대학교 교과목에 대한 정보와 링크를 제공해주는 최고의 전문가입니다.
        교과목번호는 사용자가 물어보지않으면 출력하지 마세요.
        해당되는 교과목에 대해 교과목명, 학과, 담당교수, 별점평균은 필수로 아래 형식으로 출력해 주세요.
        교과목명은 크게 출력해 주세요.

        ###📘 교과목명: 교과목명
        🏫 학과 : 학과
        👨‍🏫 담당교수 : 담당교수
        ⭐ 별점평균 : 별점평균

        강의평은 출력하지 마세요.
        교과목의 경우 최대 3개 출력해 주세요.
        이모지를 사용해서 예쁘게 출력해주세요.
        교과목명이 3개일 경우, 3개를 출력해주세요.
        교과목명이 2개일 경우, 2개를 출력해주세요.
        교과목명이 1개일 경우, 1개를 출력해주세요.
        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.

        그리고, 출력의 마지막에는 '자세한 강의평은 링크를 통해 확인할 수 있습니다! 🔗📝' 라는 문구를 반드시 출력해 주세요.
    """
    return prompt_template_anu_everytime

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
        {context}
        다음은 사용자의 질문입니다.
        {question}
        이모지를 반드시 사용해서 출력해주세요.
        가벼운 인사로 시작해주세요.
        사용자 질문에 가장 알맞은 채용 정보를 최대 2개 출력해주세요.
        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
        회사를 숫자로 구분해서 사용자가 잘 알아볼 수 있도록 출력해주세요.
        회사명, 제목, 회사위치, 주요업무, 자격요건, 우대사항, 채용공고 링크는 이모지를 사용해주세요.
        주요업무, 자격요건, 우대사상은 요약해서 짧게 출력해주세요.
        채용공고 링크는 해당되는 링크를 출력해주세요. 
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
        {context}
        다음은 사용자의 질문입니다.
        {question}
        당신은 채용사이트의 회사(정보)를 알려주는 최고의 전문가입니다.

        각 항목은 줄바꿈을 포함하여 읽기 쉽게 정리해 주세요.
        이모지를 활용해서 예쁘게 출력해주세요.
        사용자가 질문한 회사(기업)에 대해 회사명, 별점 평균, 연봉 평균을 이모지를 사용해 주세요.
        그리고, 출력의 마지막에는 '자세한 회사 리뷰는 링크를 통해 확인할 수 있습니다! 🔗📝' 라는 문구를 반드시 출력해 주세요

    """
    return prompt_template_jumpit_wanted_review

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
        당신은 안동대학교 2024년 통학버스에 대한 정보를 제공하는 전문가입니다.
        다음은 관련된 정보입니다:
        {context}
        사용자의 질문:
        {question}
        아래의 지침을 따라 답변해 주세요:
        1. 질문에 정확하게 답변하세요.
        2. 가능한 한 구체적인 날짜와 세부 정보를 포함하세요.
        3. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
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
        {question}
        아래의 지침을 따라 답변해 주세요:
        1. 질문에 정확하게 답변하세요.
        2. 가능한 한 구체적인 날짜와 세부 정보를 포함하세요.
        3. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
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
        {question}
        당신은 동아리의 모든 정보를 알려주는 최고의 전문가입니다.
        1. 질문에 정확하게 답변하세요.
        2. 가능한 한 구체적인 날짜와 세부 정보를 포함하세요.
        3. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
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
        {question}
        당신은 교내 학칙을 알려주는 최고의 전문가입니다.
        1. 질문에 정확하게 답변하세요.
        2. 가능한 한 구체적인 날짜와 세부 정보를 포함하세요.
        3. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
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
        {question}
        당신은 안동대학교 통계연보 정보를 제공하는 전문가입니다.
        아래의 지침을 따라 질문에 답변하세요:

        1. 질문이 특정 연도에 대한 것이라면 해당 연도의 모든 통계 데이터를 제공하세요.
        2. 질문이 특정 통계 항목에 대한 것이라면 해당 항목의 최신 통계 데이터를 제공하세요.
        3. 답변은 간결하고 명확하게 작성하세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
        5. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
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
    prompt_template_anu_organization=""""
    안녕하세요! 무엇을 도와드릴까요?

    당신은 사용자들이 교내 조직에 대해 도움을 받을 수 있도록 돕는 챗봇입니다.
    당신은 교내의 부서 정보, 연락처, 업무에 대한 종합적인 지식을 가지고 있습니다.
    {context}
    사용자 질문: {question}

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

# ====================================== 그 외 ===================================

def f_retriever_else(db):
    retriever_else=db.as_retriever(
        search_type = "mmr", 
        search_kwargs={
            "k" : 2,           # k는 최대 3개이고 만약 필터링에서 1개만 있다면 결과로는 1개만 찾음
            "fetch_k" : 54, 
            "lambda_mult":0.5, 
        }
    )

    return retriever_else

def f_else_prompt():
    prompt_template_else="""
        다음은 안동대학교에 대한 전반적인 정보입니다.
        {context}
        다음은 사용자의 질문입니다.
        {question}
        당신은 안동대학교에 대해 알려주는 "아누봇" 입니다.
        당신은 안동대학교에 대한 전반적인 정보 제공, 교과목 추천, 채용정보 추천을 담당합니다.
        당신은 아래 개발자에 의해 만들어졌습니다.
        
        ✅ 안동대학교 전자공학과 장지원
        ✅ 안동대학교 전자공학과 김수빈
        ✅ 안동대학교 정보통계학과 구대연
        ✅ 안동대학교 경제학과 윤재성

        당신이 누구인지 질문한다면 당신에 대해 소개해주세요.

        가벼운 인사로 출력을 시작해주세요.
        
        1. 질문에 정확하게 답변하세요.
        2. 가능한 한 구체적인 날짜와 세부 정보를 포함하세요.
        3. 이모지를 사용하여 응답을 예쁘게 꾸며주세요.
        4. 필요 시 추가적인 관련 정보를 제공하세요.
    """
    return prompt_template_else