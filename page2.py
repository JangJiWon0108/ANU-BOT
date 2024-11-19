import streamlit as st

def page2():
    st.title("Page 2")

    if st.button("Back to Main Page"):
        st.experimental_set_query_params(page="main")
        st.experimental_rerun()

if __name__ == "__main__":
    page2()
