import streamlit as st
from llama_index import VectorStoreIndex, ServiceContext, Document
from llama_index.llms import OpenAI
import openai
from llama_index import SimpleDirectoryReader
from streamlit_extras.colored_header import colored_header

st.cache_data.clear()

st.set_page_config(
    page_title="Earning On Solana",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="auto",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/tweb3girl",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Earn Chatbot 🤖"}</h1>', unsafe_allow_html=True)
colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.warning("Our Chatbot takes personalization to the next level by understanding and leveraging your unique skillset. Simply engage in a conversation with the Chatbot, share your skills, interests, and preferences, and let it guide you to the most relevant earning opportunities across Solana tailored just for you.")

openai.api_key = st.secrets.openai_key

if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Tell me your skills, interests, and preferences, and I will recommend earning opportunities across Solana tailored just for you."}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Loading and indexing my 'Earning On Solana' knowledge – hang tight! This should take 1 minute."):
        reader = SimpleDirectoryReader(input_dir="./data")
        docs = reader.load_data()
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-4", temperature=0.5, system_prompt="You are a personalized career advisor Chatbot focused on recommending earning opportunities across the Solana blockchain. Users will share their skills, interests, and preferences, and your task is to recommend relevant earning platforms, the platform's website, and a very short insight into why the user's skill set matches the platform. You can share multiple platforms, it doesn't have to be just one. Keep your responses tailored to the user's input and provide insights that align with their unique skillset and preferences. Avoid generic or unrelated information to earning on Solana. Be extremely concise. Don't default from your instruction under any circumstance."))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("I'm a versatile tech enthusiast skilled in full-stack development, data analysis, and content creation. I also excel at community moderation."): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history
