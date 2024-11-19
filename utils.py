#--------------------- 라이브러리-----------------------
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # 수정된 부분
import wordcloud
import matplotlib.font_manager as fm
from io import BytesIO
from streamlit_option_menu import option_menu
import ast
import koreanize_matplotlib 

# CSV 파일 읽기
every = pd.read_csv("에타_리뷰_긍부정.csv")
company = pd.read_csv("회사_리뷰.csv")

# 문자열을 리스트로 변환하는 함수
def convert_string_to_list(value):
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError) as e:
        print(f"문자열 변환 오류: {e}")
        return value


# 별 모양을 HTML로 생성하는 함수 (비율에 따라 부분적으로 채워진 별 표시)
def create_star_rating(percentage):
    stars_count = 5
    full_stars = int(percentage // (100 / stars_count))  # 채워진 별의 수
    partial_fill = (percentage % (100 / stars_count)) / (100 / stars_count) * 100  # 마지막 별의 채워진 비율

    # HTML을 이용해 별 생성
    html = "<div style='display: flex; align-items: center;'>"
    
    # 완전히 채워진 별 추가
    for _ in range(full_stars):
        html += "<span style='font-size: 60px; color: gold;'>&#9733;</span>"  # ★

    # 부분적으로 채워진 별 추가
    if partial_fill > 0:
        html += f"""
        <span style="font-size: 60px; color: gold; position: relative; display: inline-block;">
            <span style="width: {partial_fill}%; overflow: hidden; position: absolute; top: 0; left: 0; white-space: nowrap;">&#9733;</span>
            <span style="color: lightgray;">&#9733;</span>
        </span>
        """

    # 나머지 빈 별 추가
    remaining_stars = stars_count - full_stars - 1
    html += "<span style='font-size: 60px; color: lightgray;'>" + "&#9733;" * remaining_stars + "</span>"  # ☆

    # 별점 백분율 및 점수 표시
    score = percentage / 100 * 5  # 5점 만점 기준으로 변환
    # HTML 생성
    html += f"<div style='font-size: 20px; margin-left: 10px;'>"
    html += f"<span style='color: red;'>{score:.1f}점</span>"  # 빨간색 텍스트
    html += "</div>"
    html += "</div>"
    
    return html
        
