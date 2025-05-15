from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from dotenv import load_dotenv
import os
from config.settings import LLM_CONFIG, PROMPT_TEMPLATES

def setup_llm():

    # Load environment variables
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError("Google API key not found. Please set it in your .env file.")
    
    # Initialize LLM
    llm = ChatGoogleGenerativeAI(
        model=LLM_CONFIG["model"],
        google_api_key=api_key,
        temperature=LLM_CONFIG["temperature"]
    )
    
    return llm

def create_chains(llm):
    
    # Headline generation chain
    prompt_template_header = ChatPromptTemplate(PROMPT_TEMPLATES["headline"])
    chain_header = prompt_template_header | llm | StrOutputParser()
    
    # Blog generation chain
    prompt_template_blog = ChatPromptTemplate(PROMPT_TEMPLATES["blog"])
    chain_blog = prompt_template_blog | llm | StrOutputParser()
    
    return {
        "headline": chain_header,
        "blog": chain_blog
    }