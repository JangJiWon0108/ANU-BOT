# chain.py
# 체인을 만드는 파일
import question_retriever_routing

# ============================================ page_content 만 가져오는 함수 ===============================================
def page_content_f(doc):
    return "\n\n".join(x.page_content for x in doc)

# ============================================ 청크 리뷰 순 내림 정렬하는 함수 ===============================================
def sort_chunk_f(doc):
    sort_list=sorted([float(x.page_content.split(":")[-1].replace(" ", "")) for x in doc], reverse=True)
    retriever_answer_sort=[]
    count=0
    for x in sort_list:
        for y in doc:
            if float(y.page_content.split(":")[-1].replace(" ", ""))==x:
                retriever_answer_sort.append(y)
                count+=1
                if count==2:
                    break
        if count==2:
            break
    return retriever_answer_sort

# ============================================ 체인 생성하는 함수 ===============================================
def f_chain(current_retriever, current_prompt_template, flag_sort_chunk):
    from langchain_core.prompts import PromptTemplate
    from operator import itemgetter
    import question_retriever_routing

    print(current_prompt_template)
    
    prompt=PromptTemplate(
        template=current_prompt_template,
        input_variables=["question", "context"]
    )

    prompt_chain={"question" : itemgetter("question"), "context" : itemgetter("question") | current_retriever}
    prompt_chain=prompt_chain|prompt

    # flag_sort_chunk 에 따라 정렬 여부 결정
    if flag_sort_chunk==0:
        prompt_chain={
            "question":itemgetter("question"),
            "context":itemgetter("question") | current_retriever | page_content_f
        } | prompt
    elif flag_sort_chunk==1:
        prompt_chain={
            "question":itemgetter("question"),
            "context":itemgetter("question") | current_retriever | sort_chunk_f | page_content_f
        } | prompt

    return prompt_chain

