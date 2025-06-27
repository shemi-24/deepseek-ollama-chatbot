# import streamlit as st
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     ChatPromptTemplate
# )

# # Custom CSS styling
# st.markdown("""
# <style>
#     /* Existing styles */
#     .main {
#         background-color: #1a1a1a;
#         color: #ffffff;
#     }
#     .sidebar .sidebar-content {
#         background-color: #2d2d2d;
#     }
#     .stTextInput textarea {
#         color: #ffffff !important;
#     }
    
#     /* Add these new styles for select box */
#     .stSelectbox div[data-baseweb="select"] {
#         color: white !important;
#         background-color: #3d3d3d !important;
#     }
    
#     .stSelectbox svg {
#         fill: white !important;
#     }
    
#     .stSelectbox option {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
    
#     /* For dropdown menu items */
#     div[role="listbox"] div {
#         background-color: #2d2d2d !important;
#         color: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)
# st.title("🧠 DeepSeek Code Companion")
# st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")


# # Sidebar configuration
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     selected_model = st.selectbox(
#         "Choose Model",
#         ["deepseek-r1:1.5b", "deepseek-r1:3b"],
#         index=0
#     )
#     st.divider()
#     st.markdown("### Model Capabilities")
#     st.markdown("""
#     - 🐍 Python Expert
#     - 🐞 Debugging Assistant
#     - 📝 Code Documentation
#     - 💡 Solution Design
#     """)
#     st.divider()
#     st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# # initiate the chat engine

# llm_engine=ChatOllama(
#     model=selected_model,
#     base_url="http://localhost:11434",
#     # base_url="http://192.168.5.106:11434",

    

#     temperature=0.3

# )

# # System prompt configuration
# system_prompt = SystemMessagePromptTemplate.from_template(
#     "You are an expert AI coding assistant. Provide concise, correct solutions "
#     "with strategic print statements for debugging. Always respond in English."
# )

# # Session state management
# if "message_log" not in st.session_state:
#     st.session_state.message_log = [{"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}]

# # Chat container
# chat_container = st.container()

# # Display chat messages
# with chat_container:
#     for message in st.session_state.message_log:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # Chat input and processing
# user_query = st.chat_input("Type your coding question here...")

# def generate_ai_response(prompt_chain):
#     processing_pipeline=prompt_chain | llm_engine | StrOutputParser()
#     return processing_pipeline.invoke({})

# def build_prompt_chain():
#     prompt_sequence = [system_prompt]
#     for msg in st.session_state.message_log:
#         if msg["role"] == "user":
#             prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
#         elif msg["role"] == "ai":
#             prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
#     return ChatPromptTemplate.from_messages(prompt_sequence)

# if user_query:
#     # Add user message to log
#     st.session_state.message_log.append({"role": "user", "content": user_query})
    
#     # Generate AI response
#     with st.spinner("🧠 Processing..."):
#         prompt_chain = build_prompt_chain()
#         ai_response = generate_ai_response(prompt_chain)
    
#     # Add AI response to log
#     st.session_state.message_log.append({"role": "ai", "content": ai_response})
    
#     # Rerun to update chat display
#     st.rerun()



# import streamlit as st
# from langchain_ollama import ChatOllama
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     AIMessagePromptTemplate,
#     ChatPromptTemplate
# )

# # -------------------- Styling --------------------
# st.markdown("""
# <style>
#     .main {
#         background-color: #1a1a1a;
#         color: #ffffff;
#     }
#     .sidebar .sidebar-content {
#         background-color: #2d2d2d;
#     }
#     .stTextInput textarea {
#         color: #ffffff !important;
#     }
#     .stSelectbox div[data-baseweb="select"],
#     .stSelectbox option,
#     div[role="listbox"] div {
#         color: white !important;
#         background-color: #2d2d2d !important;
#     }
#     .stSelectbox svg {
#         fill: white !important;
#     }
# </style>
# """, unsafe_allow_html=True)

# # -------------------- UI Setup --------------------
# st.title("🧠 DeepSeek Code Companion")
# st.caption("🚀 Your AI Pair Programmer with Debugging Superpowers")

# with st.sidebar:
#     st.header("⚙️ Configuration")
#     selected_model = st.selectbox(
#         "Choose Model",
#         ["deepseek-r1:1.5b", "deepseek-r1:3b"],
#         index=0
#     )
#     st.divider()
#     st.markdown("### Model Capabilities")
#     st.markdown("""
#     - 🐍 Python Expert  
#     - 🐞 Debugging Assistant  
#     - 📝 Code Documentation  
#     - 💡 Solution Design  
#     """)
#     st.divider()
#     st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# # -------------------- Chat Engine --------------------
# llm_engine = ChatOllama(
#     model=selected_model,
#     base_url="http://localhost:11434",
#     temperature=0.3
# )

# # -------------------- System Prompt with Restrictions --------------------
# system_prompt = SystemMessagePromptTemplate.from_template(
#     "You are an expert AI coding assistant. Your purpose is to help users with software development "
#     "by providing accurate, safe, and clear guidance. Always reply in English.\n\n"
#     "Strict Rules:\n"
#     "- Do NOT generate or engage in any conversation related to adult content, sexual material, or erotic themes.\n"
#     "- Avoid topics related to gambling, betting, or casino games.\n"
#     "- Do not discuss or support illegal activities, violence, hacking, or unethical behavior.\n"
#     "- Never generate code or advice that could be used maliciously or violate terms of service or laws.\n"
#     "- If a query contains unsafe or inappropriate content, politely refuse and inform the user.\n\n"
#     "If a user tries to go off-topic or requests anything against these rules, respond with:\n"
#     "\"\"Sorry, I cannot assist with that request. Let's focus on safe and productive coding topics.\"\"\"\n\n"
#     "Provide concise, correct solutions with strategic print statements for debugging."
# )

# # -------------------- Session State --------------------
# if "message_log" not in st.session_state:
#     st.session_state.message_log = [
#         {"role": "ai", "content": "Hi! I'm DeepSeek. How can I help you code today? 💻"}
#     ]

# # -------------------- Chat History --------------------
# chat_container = st.container()
# with chat_container:
#     for message in st.session_state.message_log:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

# # -------------------- Chat Input --------------------
# user_query = st.chat_input("Type your coding question here...")

# # -------------------- Blocked Content Filtering --------------------
# blocked_keywords = [
#     "sex", "porn", "nude", "xxx", "gamble", "casino", "bet", "drugs",
#     "violence", "kill", "murder", "hack", "crack", "exploit", "terrorism", "fire", "theft", "weapon", 
# ]

# def contains_blocked_content(text):
#     text_lower = text.lower()
#     return any(word in text_lower for word in blocked_keywords)

# # -------------------- Prompt Chain --------------------
# def build_prompt_chain():
#     prompt_sequence = [system_prompt]
#     for msg in st.session_state.message_log:
#         if msg["role"] == "user":
#             prompt_sequence.append(HumanMessagePromptTemplate.from_template(msg["content"]))
#         elif msg["role"] == "ai":
#             prompt_sequence.append(AIMessagePromptTemplate.from_template(msg["content"]))
#     return ChatPromptTemplate.from_messages(prompt_sequence)

# def generate_ai_response(prompt_chain):
#     processing_pipeline = prompt_chain | llm_engine | StrOutputParser()
#     return processing_pipeline.invoke({})

# # -------------------- Handle User Input --------------------
# if user_query:
#     if contains_blocked_content(user_query):
#         warning_message = "🚫 Sorry, I can't assist with that request. Let's stick to safe and productive coding topics."
#         st.session_state.message_log.append({"role": "ai", "content": warning_message})
#         st.rerun()
#     else:
#         st.session_state.message_log.append({"role": "user", "content": user_query})

#         with st.spinner("🧠 Processing..."):
#             prompt_chain = build_prompt_chain()
#             ai_response = generate_ai_response(prompt_chain)

#         st.session_state.message_log.append({"role": "ai", "content": ai_response})
#         st.rerun()



import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    ChatPromptTemplate
)

# ---------------------- Custom CSS Styling ----------------------
st.markdown("""
<style>
    .main {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #2d2d2d;
    }
    .stTextInput textarea {
        color: #ffffff !important;
    }
    .stSelectbox div[data-baseweb="select"] {
        color: white !important;
        background-color: #3d3d3d !important;
    }
    .stSelectbox svg {
        fill: white !important;
    }
    .stSelectbox option {
        background-color: #2d2d2d !important;
        color: white !important;
    }
    div[role="listbox"] div {
        background-color: #2d2d2d !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------- UI Title & Description ----------------------
st.title("🧠EduBot")
st.caption("🎓 An AI Learning Companion for Students under 18")

# ---------------------- Sidebar Configuration ----------------------
# with st.sidebar:
#     st.header("⚙️ Configuration")
#     selected_model = st.selectbox(
#         "Choose Model",
#         ["deepseek-r1:1.5b", "deepseek-r1:3b"],
#         index=0
#     )
#     st.divider()
#     st.markdown("### Capabilities")
#     st.markdown("""
#     - 📘 Learn to Code
#     - 🔍 Debug with Help
#     - ✍️ Write and Explain Code
#     - 💡 Brainstorm Student Projects
#     """)
#     st.divider()
#     st.markdown("Built with [Ollama](https://ollama.ai/) | [LangChain](https://python.langchain.com/)")

# ---------------------- Safety Filter Configuration ----------------------
blocked_keywords = [
    "sex", "porn", "nude", "xxx", "gamble", "casino", "bet", "drug",
    "violence", "kill", "murder", "weapon", "terrorism", "hack", "crack", "exploit",
    "adult", "nsfw", "18+", "suicide", "self-harm"
]
warning_message = (
    "🚫 I'm here to help with safe and educational topics for students. "
    "Let's focus on learning something fun and useful!"
)

# ---------------------- AI Engine Initialization ----------------------
llm_engine = ChatOllama(
    model='deepseek-r1:1.5b',
    base_url="http://localhost:11434",
    temperature=0.3
)

# ---------------------- System Prompt for Safety and Relevance ----------------------
system_prompt = SystemMessagePromptTemplate.from_template(
    "You are a friendly and responsible AI assistant designed to help students under the age of 18 with learning-related questions.\n\n"
    "Your primary goals:\n"
    "- Help students understand academic subjects such as coding, math, science, writing, and creative thinking.\n"
    "- Encourage curiosity, problem-solving, and learning.\n"
    "- Be clear, polite, and age-appropriate in all responses.\n"
    "- Only provide helpful, educational, and safe content.\n\n"
    "Strict rules:\n"
    "- DO NOT answer or engage with any questions involving adult content, sexual material, gambling, violence, hacking, drugs, weapons, or other mature or illegal topics.\n"
    "- DO NOT include content that could be inappropriate, dangerous, or offensive for minors.\n"
    "- Politely refuse and redirect the conversation if asked about any restricted topics.\n\n"
    "If a user says something inappropriate or unsafe, reply with:\n"
    "\"I'm here to help with learning and educational questions. Let's keep things safe and focused on learning!\"\n\n"
    "Always be positive, educational, and supportive. Respond in simple, clear English for students."
)

# ---------------------- Session State for Chat ----------------------
if "message_log" not in st.session_state:
    st.session_state.message_log = [
        {"role": "ai", "content": "Hi! I'm EduBot. What would you like to learn today? 📘"}
    ]

# ---------------------- Chat Display ----------------------
chat_container = st.container()
with chat_container:
    for message in st.session_state.message_log:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# ---------------------- Chat Input and Processing ----------------------
user_query = st.chat_input("Ask your question here...")

def generate_ai_response(prompt_chain):
    pipeline = prompt_chain | llm_engine | StrOutputParser()
    return pipeline.invoke({})

def build_prompt_chain():
    messages = [system_prompt]
    for msg in st.session_state.message_log:
        if msg["role"] == "user":
            messages.append(HumanMessagePromptTemplate.from_template(msg["content"]))
        elif msg["role"] == "ai":
            messages.append(AIMessagePromptTemplate.from_template(msg["content"]))
    return ChatPromptTemplate.from_messages(messages)

if user_query:
    # Check for blocked content
    if any(bad_word in user_query.lower() for bad_word in blocked_keywords):
        st.session_state.message_log.append({"role": "user", "content": user_query})
        st.session_state.message_log.append({"role": "ai", "content": warning_message})
        st.rerun()

    # Add valid user message
    st.session_state.message_log.append({"role": "user", "content": user_query})

    with st.spinner("🧠 Thinking..."):
        prompt_chain = build_prompt_chain()
        ai_response = generate_ai_response(prompt_chain)

    st.session_state.message_log.append({"role": "ai", "content": ai_response})
    st.rerun()
