# AI Study Buddy

AI Study Buddy is a Streamlit-based Generative AI application that helps students understand topics, generate summaries, and create exam-ready notes using Google's Gemini model.

## Features

* Explain Concepts
* Essay Summaries
* Exam Notes Generation
* AI-Powered Responses using Gemini
* Interactive Streamlit Interface

## Tech Stack

* Python
* Streamlit
* Google Gemini API

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/AI-StudyBuddy.git
cd AI-StudyBuddy
```

2. Install dependencies

```bash
pip install streamlit
pip install google-genai
```

3. Add your Gemini API Key

Create a `.env` file:

```text
GEMINI_API_KEY=your_api_key
```

4. Run the application

```bash
streamlit run product.py
```

If the default port is occupied:

```bash
streamlit run product.py --server.port 8505
```

## Project Structure

```text
AI-StudyBuddy/
│
├── product.py
├── README.md
├── .gitignore
└── .env (not uploaded to GitHub)
```

## Future Enhancements

* Quiz Generator
* Flashcard Generator
* PDF Notes Summarizer
* Personalized Learning Recommendations

## Author

Sifat Bhatia
