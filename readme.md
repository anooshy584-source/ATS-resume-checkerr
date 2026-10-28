
# AI Learning Roadmap Generator

An AI-powered web application that creates personalized learning roadmaps.

## Features

- Select a learning field.
- Choose Beginner, Intermediate, or Advanced level.
- Set the learning duration and weekly study hours.
- Generate a week-by-week learning roadmap.
- Get practical exercises and a final project.
- Receive free learning resources.
- Download the roadmap as a Markdown file.
- Test the Groq API connection.

## Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Model (LLM)

## Installation

1. Install Python.
2. Install the required packages:

   pip install -r requirements.txt

3. Configure your Groq API key using an environment variable
   or Streamlit Secrets.

4. Start the application:

   python -m streamlit run app.py

## API Configuration

Add the following to Streamlit Secrets:

GROQ_API_KEY = "your_actual_groq_api_key"

Optionally, you can set a model:

GROQ_MODEL = "llama-3.3-70b-versatile"

Never upload your real API key to GitHub.

## Disclaimer

The generated roadmaps are AI-generated suggestions.
Check the learning resources and adapt the plan to your needs.
