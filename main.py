import streamlit as st

def main():
    # URL 파라미터를 가져옴
    query_params = st.experimental_get_query_params()
    page = query_params.get("page", ["main"])[0]

    # 페이지에 따라 해당 모듈을 임포트하고 실행
    if page == "main":
        import main
        main.main()
    elif page == "page2":
        import page2
        page2.page2()

if __name__ == "__main__":
    main()