# ✍️ Blog Generator

A Streamlit application that generates blog post headlines and content using LangChain and Google's Gemini AI.

![Blog generator](<Blog generator.png>)

---

## Features

- Generate multiple headlines based on a topic
- Create structured blog posts from selected headlines
- Simple and intuitive user interface
- Download generated content as markdown files

---

## Technology Stack

- **Streamlit**: Web application framework
- **LangChain**: Framework for LLM applications
- **Google Gemini**: Large Language Model
- **Python**: Programming language

---

## Project Structure

```
blog-generator/
├── .env.example       # environment variables file
├── README.md          # Project documentation
├── requirements.txt   # Project dependencies
├── main.py            # Main Streamlit application
├── config/            # Configuration directory
│   ├── __init__.py    # Package initialization
│   └── settings.py    # Configuration settings
└── utils/             # Utilities directory
    ├── __init__.py    # Package initialization
    ├── chains.py      # LangChain components
    ├── interface.py   # UI components
    └── state.py       # State management functions
```

---

## Installation

1. Clone the repository:
   ```bash
   https://github.com/eslammohamedtolba/Blog-Generator.git
   cd Blog-Generator
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your Google API key:
   ```
   GOOGLE_API_KEY=your_api_key_here
   ```

---

## Usage

1. Run the application:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Enter a topic and generate headlines

4. Use the generated headlines or add custom headlines to create a complete blog post

5. Download your blog post as a markdown file

---

## Requirements

- Python 3.7+
- Google API key with access to Gemini models

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
