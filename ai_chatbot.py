import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ( SystemMessagePromptTemplate, HumanMessagePromptTemplate, AIMessagePromptTemplate, ChatPromptTemplate)

st.markdown("""
<style>
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea, .stSelectbox div[data-baseweb="select"] {
        color: #ffffff;
        background-color: #3d3d3d ;
    }
    .stSelectbox svg {
        fill: white ;
    }
    .stSelectbox option, div[role="listbox"] div {
        background-color: #2d2d2d ;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 🎯 Application Title and Description
st.title("AI Business & Tech Consultant")
st.caption("Get insights on market trends, business strategies, AI applications, data analysis, and coding best practices.")

# 🛠️ Sidebar Settings
with st.sidebar:
    st.header("🔧 Settings")

    # Model selection
    selected_model = st.selectbox("Choose Model", ["deepseek-r1:1.5b", "deepseek-r1:3b"], index=0)

    # Button to start a new conversation
    if st.button("Start New Chat"):
        st.session_state.message_log = []
        st.rerun()
   
    # Example questions
    st.markdown(
        """
        **Try asking:**
        - "What are the latest AI trends in business?"
        - "How can I improve my product development process?"
        - "What are the best data visualization tools?"
        - "How do I scale my startup using AI?"
        """
    )
    
    st.divider()
    st.markdown("This app is built using [Ollama](https://ollama.ai/) and [LangChain](https://python.langchain.com/).")

# 🌟 Define the system message to set AI behavior
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are an AI consultant specializing in business, data analysis, and technology trends. "
    "Assist users with insights on market trends, business strategies, product development, AI applications, and coding best practices."
)

def initialize_llm(selected_model):
    """
    Initialize the LLM engine with the selected model.
    """
    return ChatOllama(
        model=selected_model,
        base_url="http://localhost:11434"
    )

def construct_prompt_chain(message_log):
    """
    Builds a structured conversation flow based on chat history.
    """
    prompt_sequence = [system_prompt]

    # Iterate over message history to build a contextual conversation
    for msg in message_log:
        if msg["role"] == "user":
            prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))

    return ChatPromptTemplate.from_messages(prompt_sequence)

def generate_response(prompt_chain, llm_engine):
    """
    Process the AI response using LangChain pipeline.
    """
    processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
    return processing_pipeline.invoke({})

# 🚀 Initialize AI Model
llm_engine = initialize_llm(selected_model)

# 🔄 Load chat history
if "message_log" not in st.session_state:
    st.session_state.message_log = [{"role": "ai", "content": "Hello! I'm your AI Business & Tech Consultant. How can I assist you today?"}]

# 📜 Chat Container
chat_container = st.container()

# Display past messages
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 📝 Get user input
user_query = st.chat_input("Ask about market trends, business strategies, AI applications, and more...")

# 🚀 Generate AI Response
if user_query:
    # Add user input to message log
    st.session_state.message_log.append({"role": "user", "content": user_query})

    # Show loading spinner while AI generates a response
    with st.spinner("Generating response..."):
        prompt_chain = construct_prompt_chain(st.session_state.message_log)
        ai_response = generate_response(prompt_chain, llm_engine)

    # Append AI response to chat history
    st.session_state.message_log.append({"role": "ai", "content": ai_response})

    # Refresh the chat interface
    st.rerun()
