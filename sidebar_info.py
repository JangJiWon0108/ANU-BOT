# sidebar_info.py
# 사이드바 관련 파일

# =============================================== 라이브러리 ====================================================
import streamlit as st

# ========================================= 안동대학교 정보 =============================================== 
def f_sidebar_anu_info():
    markdown_str="""
        <style>
            .option {
                margin-left: 30px; /* 원하는 공백의 크기 조정 */
            }
        </style>
        <h3>😁안동대학교에 대해 알려드립니다❗</h3>
        <h4>👇아래 항목들에 대해 질문해 주세요👇</h4>
        <p class='option'>✅학사일정&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅통학버스</p>
        <p class='option'>✅전화 번호&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅동아리</p> 
        <p class='option'>✅취업률&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅주요 취업처</p>
        <p class='option'>✅기숙사&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✅학칙</p>
    """
    return markdown_str

def f_question_ex_anu_info():
    markdown_str="""
        <style>
            .text {
                font-size: 15px; /* 폰트 크기를 20px로 설정 */
                color: #7C00A0; /* 텍스트 색상 설정 (옵션) */
            }
        </style>
        <p class='text'>9월 학사일정 알려주세요</p>
        <p class='text'>2학기 중간고사 기간이 언제인가요?</p>
        <p class='text'>구미쪽 하교 통학버스 노선 알려주세요</p>
        <p class='text'>박미경선생님 전화번호 알려주세요</p> 
        <p class='text'>전자공학과 학과사무실 전화번호 알려주세요</p> 
        <p class='text'>댄스 동아리가 있나요?</p> 
        <p class='text'>전자공학과 취업률과 주요 취업처가 궁금해요</p>
        <p class='text'>기숙사 등록하는 방법이 궁금해요</p>
        <p class='text'>개교기념일이 언제인가요?</p>
    """
    return markdown_str

# ========================================= 교과목 정보 ===============================================
def f_sidebar_subject_info():
    markdown_str="""
        <style>
            .option {
                margin-left: 30px; /* 원하는 공백의 크기 조정 */
            }
        </style>
        <h3>😁교과목 정보를 제공해 드립니다❗</h3>
        <h4>👇아래 항목들에 대해 질문해 주세요👇</h4>
        <p class='option'>✅교과목 추천/질문</p>
        <p class='option'>✅교과목 강의평</p> 
    """
    return markdown_str

def f_question_ex_subject_info():
    markdown_str="""
        <style>
            .text {
                font-size: 15px; /* 폰트 크기를 20px로 설정 */
                color: #7C00A0; /* 텍스트 색상 설정 (옵션) */
            }
        </style>
        <p class='text'>진로/취업관련된 교양과목 추천해 주세요</p>
        <p class='text'>인공지능(AI)관련된 과목을 추천해 주세요</p>
        <p class='text'>직업의 세계와 진로선택 과목의 강의평이 궁금해요</p> 
        <p class='text'>취업역량개발 과목의 강의평이 궁금해요</p> 
    """
    return markdown_str
# ========================================= 채용정보 ===============================================
def f_sidebar_hire_info():
    markdown_str="""
        <style>
            .option {
                margin-left: 30px; /* 원하는 공백의 크기 조정 */
            }
        </style>
        <h3>😁채용(회사) 정보를 제공해 드립니다❗</h3>
        <h4>👇아래 항목들에 대해 질문해 주세요👇</h4>
        <p class='option'>✅채용공고(회사) 추천/질문</p>
        <p class='option'>✅회사 리뷰</p> 
    """
    return markdown_str

def f_question_ex_hire_info():
    markdown_str="""
        <style>
            .text {
                font-size: 15px; /* 폰트 크기를 20px로 설정 */
                color: #7C00A0; /* 텍스트 색상 설정 (옵션) */
            }
        </style>
        <p class='text'>LLM 챗봇 관련 채용공고 추천해 주세요</p>
        <p class='text'>데이터 분석 관련 채용공고 추천해 주세요</p>
        <p class='text'>마케팅 관련 채용공고 추천해 주세요</p> 
        <p class='text'>빗썸코리아 회사의 리뷰가 궁금해요</p> 
        <p class='text'>딥노이드 회사의 리뷰를 보고싶어요</p> 
        <p class='text'>쏘카 회사의 리뷰를 보고싶어요</p> 
    """
    return markdown_str