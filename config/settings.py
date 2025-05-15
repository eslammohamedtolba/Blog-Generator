# Streamlit app configuration
APP_CONFIG = {
    "page_title": "Blog Generator",
    "page_icon": "✍️",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# LLM Configuration
LLM_CONFIG = {
    "model": "gemini-2.0-flash",
    "temperature": 0.7
}

# Prompt templates
PROMPT_TEMPLATES = {
    "headline": [
        ("system", "You are a helpful assistant"),
        ("human", "Write {number_h} headlines or headers about this title: {title} "
                 "directly without any introductions or pleasantries as 'Here is...' "
                 "or conclusions as 'if you need anything else...'")
    ],
    "blog": [
        ("system", "You are a helpful assistant"),
        ("human", "Write a blog post using these headers: {headers} "
                "directly without any introductions or pleasantries as 'Here is...' "
                "or conclusions as 'if you need anything else...'")
    ]
}

# Custom CSS for styling
CUSTOM_CSS = """
<style>
.headline-container {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-top: 10px;
}
.headline-item {
    border: 2px solid red;
    border-radius: 4px;
    padding: 8px 12px;
    display: inline-flex;
    background-color: transparent;
    color: white;
}
.stButton button {
    margin-top: 22px;
}
</style>
"""