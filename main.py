import streamlit as st
from utils.chains import setup_llm, create_chains
from utils.interface import render_headline_generator, render_blog_generator
from utils.state import initialize_session_state
from config.settings import APP_CONFIG

def main():
    
    # Configure page
    st.set_page_config(**APP_CONFIG)
    
    # Set page title and description
    st.title("✍️ Blog Generator")
    st.write("Generate headlines and blog posts with LangChain and Gemini")

    # Initialize session state
    initialize_session_state()
    
    # Set up LLM and chains
    llm = setup_llm()
    chains = create_chains(llm)
    
    # Headline generation section
    st.subheader("Generate Headlines")
    render_headline_generator(chains["headline"])
    
    # Blog post generation section
    st.subheader("Generate Blog Post")
    render_blog_generator(chains["blog"])

if __name__ == "__main__":
    main()