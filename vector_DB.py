# vector DB.py
# FAISS 벡터 db를 가져오는 파일

# ===================================== FAISS 벡터 DB 로딩 ===========================================
def f_faiss_vertorDB_upstage(embedding_model):
    # 저장된 db 불러오기
    # db이름, 임베딩 모델, 허용을 True로 설정

    from langchain_community.vectorstores import FAISS

    db = FAISS.load_local(
        "faiss_db_upstage_anu_total_jw_js_final_final", 
        embedding_model, 
        allow_dangerous_deserialization=True
    )

    return db


# ===================================== FAISS 벡터 DB 로딩 ===========================================
def f_faiss_vertorDB_openai(embedding_model):
    # 저장된 db 불러오기
    # db이름, 임베딩 모델, 허용을 True로 설정

    from langchain_community.vectorstores import FAISS

    db = FAISS.load_local(
        "faiss_db_openai_anu_total_jw_js_final_final", 
        embedding_model, 
        allow_dangerous_deserialization=True
    )

    return db