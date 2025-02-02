# AI Business & Tech Consultant - Streamlit App

This is a Streamlit-based web application designed to provide AI-powered insights on various topics including market trends, business strategies, AI applications, data analysis, and coding best practices. The app uses the Ollama LLM (Language Learning Model) and LangChain library to process user queries and provide tailored responses.
<img width="1274" alt="Ekran Resmi 2025-02-03 00 46 32" src="https://github.com/user-attachments/assets/fe6513be-a24d-483e-89b2-1d452528188e" />
<img width="1275" alt="Ekran Resmi 2025-02-03 00 46 10" src="https://github.com/user-attachments/assets/51e64fd4-e55a-48d5-94db-c8dedaf39cfd" />

## Features:
- **AI-powered business & tech consultation**: Users can ask about the latest trends in AI, market analysis, product development, business strategies, and more.
- **Model Selection**: The app allows users to choose between two different models (deepseek-r1:1.5b, deepseek-r1:3b) to generate responses.
- **New Conversation**: Start a fresh conversation with a click of a button, clearing the chat history.
- **Interactive UI**: A user-friendly interface built with Streamlit, providing a clean and intuitive chat experience.

## Setup Instructions:


### Prerequisites:

- Python 3.7 or higher
- Streamlit
- LangChain
- Ollama

### Installation:
1. Clone this repository:
   ```bash
   git clone <repository_url>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables (Create a `.env` file in the root directory of the project with the following content):
   ```env
   OLLAMA_BASE_URL=http://localhost:11434
   ```

   Ensure that **Ollama** is running locally on port `11434`. You can configure this in the Ollama setup.

6. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

### Configuration:
The app uses **Ollama's** language model API. Set up Ollama and make sure it's running locally on port `11434`:
- Download and set up Ollama from [ollama.ai](https://ollama.ai/)

Once the app is running, open it in your browser to interact with the AI Business & Tech Consultant.

## How to Use:
1. **Choose a model**: From the sidebar, select the AI model you want to use for generating responses (e.g., `deepseek-r1:1.5b`, `deepseek-r1:3b`).
2. **Ask a question**: Type a question in the chat input field related to business strategies, tech trends, AI applications, or coding best practices.
3. **Receive responses**: After asking, wait for the AI to generate a response and it will appear in the chat window.
4. **Start a new chat**: Press the "Start New Chat" button in the sidebar to clear the chat history and begin a fresh conversation.

### Example Questions:
- "What are the latest AI trends in business?"
- "How can I improve my product development process?"
- "What are the best data visualization tools?"
- "How do I scale my startup using AI?"

## Development:
This app uses the **LangChain** library to structure and process prompts for the chosen model, and it utilizes **Streamlit** to build the web interface. The application is extensible, allowing for future improvements like model fine-tuning and adding new features.

