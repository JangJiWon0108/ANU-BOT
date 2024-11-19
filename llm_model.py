# llm_model.py
# Upstage LLM 모델을 불러오는 파일

# ============================================= Upstage LLM 모델 로딩 ==================================================
def f_Upstage_llm_model():
    from langchain_upstage import ChatUpstage

    upstage_llm_model=ChatUpstage(api_key="up_D8sLGDa0x7FknzDfrMuiVMxEObmEP")

    return upstage_llm_model

def f_OpenAI_llm_model():
    from langchain_community.chat_models import ChatOllama
    from langchain_core.output_parsers import StrOutputParser
    from langchain_core.prompts import ChatPromptTemplate
    from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
    from langchain_core.callbacks.manager import CallbackManager
    from langchain.chat_models import ChatOpenAI

    # OPEN AI 의 llm 실습
    from langchain_core.output_parsers import StrOutputParser
    # from langchain_openai import ChatOpenAI
    from langchain_community.chat_models import ChatOpenAI
    

    # llm 모델 불러오기
    llm=ChatOpenAI(model="gpt-4o", api_key="sk-0JQIqlXIpJng0M1enJYOIj073FoYqq_IzMTX30zn0lT3BlbkFJarPwhYTedklDROKIX3-h1Ox9t7Lmyx0qCgP3G1NngA")

    return llm