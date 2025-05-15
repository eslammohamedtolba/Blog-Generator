import streamlit as st

def initialize_session_state():
    # Initialize session state for headline generator
    if 'generated_headlines' not in st.session_state:
        st.session_state.generated_headlines = ""
    
    # Initialize session state for blog generator
    if 'blog_post' not in st.session_state:
        st.session_state.blog_post = ""
    
    # Initialize session state for headline list
    if 'headlines_list' not in st.session_state:
        st.session_state.headlines_list = []

def clear_headlines():
    st.session_state.headlines_list = []

def use_generated_headlines():
    if st.session_state.generated_headlines:
        headlines = [
            h.strip() for h in st.session_state.generated_headlines.split('\n') 
            if h.strip() and not h.startswith('-')
        ]
        st.session_state.headlines_list.extend(headlines)