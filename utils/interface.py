import streamlit as st
from config.settings import CUSTOM_CSS

def render_headline_generator(chain_header):
    # Apply custom CSS
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)
    
    # Input elements for headline generation
    col1, col2 = st.columns([3, 1])
    with col1:
        title_input = st.text_input("Enter a topic:", placeholder="e.g., Data Science, Machine Learning")
    with col2:
        num_headlines = st.number_input("Number of headlines:", min_value=1, max_value=20, value=5)

    generate_headlines_button = st.button("Generate Headlines")

    # Generate headlines when button is clicked
    if generate_headlines_button and title_input:
        with st.spinner("Generating headlines..."):
            try:
                response_headers = chain_header.invoke({
                    "number_h": str(num_headlines), 
                    "title": title_input
                })
                st.session_state.generated_headlines = response_headers
            except Exception as e:
                st.error(f"Error: {str(e)}")

    # Display generated headlines
    if st.session_state.generated_headlines:
        st.write("Generated Headlines:")
        st.write(st.session_state.generated_headlines)


def render_blog_generator(chain_blog):
    # Input for adding custom headlines with button on same line
    col1, col2 = st.columns([4, 1])
    with col1:
        st.text_input("Enter a headline:", key="new_headline", placeholder="e.g., Machine Learning Fundamentals")
    with col2:
        st.button("Add", on_click=add_headline)

    # Display added headlines as tags/keywords
    if st.session_state.headlines_list:
        # Create the container for headlines
        headline_html = '<div class="headline-container">'
        
        # Add each headline as a box in the flex container
        for headline in st.session_state.headlines_list:
            headline_html += f'<div class="headline-item">{headline}</div>'
        
        # Close the container
        headline_html += '</div>'
        
        st.markdown(headline_html, unsafe_allow_html=True)

    # Generate blog button
    generate_blog_button = st.button("Generate Blog Post")

    # Generate blog post when button is clicked
    if generate_blog_button:
        if st.session_state.headlines_list:
            headers_input = "\n".join(st.session_state.headlines_list)
        elif st.session_state.generated_headlines:
            headers_input = st.session_state.generated_headlines
        else:
            st.warning("Please generate headlines or add custom headlines first.")
            headers_input = ""
        
        if headers_input:
            with st.spinner("Generating blog post..."):
                try:
                    response_blog = chain_blog.invoke({"headers": headers_input})
                    st.session_state.blog_post = response_blog
                except Exception as e:
                    st.error(f"Error: {str(e)}")

    # Display blog post
    if st.session_state.blog_post:
        st.subheader("Generated Blog Post:")
        st.markdown(st.session_state.blog_post)
        
        # Download button
        st.download_button(
            label="Download Blog Post",
            data=st.session_state.blog_post,
            file_name="generated_blog.md",
            mime="text/markdown"
        )


def add_headline():
    if st.session_state.new_headline.strip():
        st.session_state.headlines_list.append(st.session_state.new_headline.strip())
        st.session_state.new_headline = ""