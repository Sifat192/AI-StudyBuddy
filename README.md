# AI Study Buddy

AI Study Buddy is a Streamlit-based Generative AI application that helps students understand topics, generate concise essays, and create exam-ready notes using Google's Gemini AI model.

## Features

* Explain complex concepts in simple language
* Generate concise essays on any topic
* Create exam-ready notes with key points and bullet summaries
* Interactive Streamlit-based user interface
* Powered by Google Gemini

## Tech Stack

* Python
* Streamlit
* Google Gemini API

## Project Workflow

```text
User Input
    ↓
Select Study Mode
    ↓
Gemini AI
    ↓
Generated Study Material
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Sifat192/AI-StudyBuddy.git
cd AI-StudyBuddy
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run product.py
```

If the default port is already in use:

```bash
streamlit run product.py --server.port 8505
```

## Usage

1. Enter a topic you want to study.
2. Select a study mode:

   * Explain Concept
   * Summarise in Essay
   * Exam Minutes
3. Click **Generate**.
4. View the AI-generated response.

## Project Structure

```text
AI-StudyBuddy/
│
├── product.py
├── README.md
└── requirements.txt
```

## Future Enhancements

* Quiz Generator
* Flashcard Generator
* PDF Notes Summarizer
* Personalized Learning Recommendations
* Multi-language Support

## Author

Sifat Bhatia

