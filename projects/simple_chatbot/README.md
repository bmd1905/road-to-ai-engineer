# ChatGPT-like Clone

![CleanShot 2024-10-10 at 00 39 55@2x](https://github.com/user-attachments/assets/92040bc1-0227-4bda-b1ad-272201d0cde6)

## Overview
This project is a web application that mimics the functionality of ChatGPT, allowing users to interact with an AI model in a chat format. Built using Streamlit, it provides a user-friendly interface for chatting with the AI.

## Features
- User can input messages and receive responses from the AI.
- Chat history is maintained across sessions.
- Supports multiple AI models (default is `gpt-4o-mini`).

## Requirements
To run this application, please create a `.env` file with the following environment variable:
```bash
OPENAI_API_KEY=<your-openai-api-key>
```

Go to [OpenAI](https://platform.openai.com/api-keys) to get your API key.

Then create a virtual environment and install the dependencies:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application

### 1. Start standalone

If you don't want to use the backend and frontend seperately, you can start the standalone application by running the following command:
```bash
python simple_aio.py
```

### 2. Separate backend and frontend

First start the backend service:
```bash
uvicorn backend.main:app --reload
```

Then start the frontend:

```bash
streamlit run frontend/app.py
```

## Usage
1. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
2. Type your message in the input box and hit enter.
3. The AI's response will be displayed in the chat interface.
