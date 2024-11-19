# embedding model.py
# 임베딩 모델을 정의하는 파일

# ===================================== Upstage Embedding Model ======================================
def f_upstage_embedding_model():
    import pandas as pd 
    from dotenv import load_dotenv
    from langchain_upstage import UpstageEmbeddings

    # 환경변수 설정
    load_dotenv(dotenv_path="C:/최종 프로젝트/.env")

    # upstage 임베딩을 가져옴
    upstage_embedding_model=UpstageEmbeddings(model="solar-embedding-1-large")
    
    return upstage_embedding_model

# ===================================== OpenAI Embedding Model ======================================
def f_openai_embedding_model():
    import pandas as pd 
    from dotenv import load_dotenv
    from langchain_upstage import UpstageEmbeddings
    from langchain_openai import OpenAIEmbeddings

    # openai 임베딩을 가져옴
    openai_embedding_model=OpenAIEmbeddings(
        model="text-embedding-ada-002", 
        api_key="sk-0JQIqlXIpJng0M1enJYOIj073FoYqq_IzMTX30zn0lT3BlbkFJarPwhYTedklDROKIX3-h1Ox9t7Lmyx0qCgP3G1NngA"
    )

    return openai_embedding_model

