import streamlit as st
import google.generativeai as genai

# Page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Ahmed Awan's Chatbot", page_icon="🤖")

# App title
st.title("💬 Ahmed Awan's  AI Chatbot")

# Replace with your Gemini API key
api_key = "AIzaSyAgoVIGdbMhE_p2-us4rAxbr3lIVcBi1Ak"
genai.configure(api_key=api_key)

# Use the correct model name
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Input box at the top
query = st.text_input("Ask anything you want:")

# Handle query and display response
if st.button("Get Answer"):
    if query:
        with st.spinner("Generating response..."):
            try:
                response = model.generate_content(query)
                st.markdown("### 🤖 Answer:")
                st.markdown(response.text)
            except genai.exceptions.GenerationError as e:
                st.error(f"❌ Generation error: {e}")
            except Exception as e:
                st.error(f"❌ Unexpected error: {e}")
    else:
        st.warning("Please enter a question.")
