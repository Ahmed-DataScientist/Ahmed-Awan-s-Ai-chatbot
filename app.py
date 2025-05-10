import streamlit as st
import google.generativeai as genai

# Page configuration (must be the first Streamlit command)
st.set_page_config(page_title="Ahmed Awan's Chatbot", page_icon="🤖")

# App title
st.title("💬 Ahmed Awan's AI Chatbot")

# Personal introduction
with st.expander("👨‍💻 About Ahmed Awan"):
    st.markdown("""
    **👋 Meet Ahmed Awan**  
    - Google Certified Data Analyst  
    - IBM Certified Data Analyst  
    - Skilled in Python, SQL, Power BI, Machine Learning, Deep Learning, and AI  
    - Experienced with tools like Roboflow, Hugging Face, Ultralytics Hub  
    - Currently pursuing BS at **UET**, Class of 2026  
    - Interned as Data Analyst at NSDIC, Business Analyst at Meri Skills, SOC Analyst at UIG Software House  
    - Enrolled in Agentic AI and Robotics Engineer program at PIAIC  
    - Active on [GitHub](https://github.com/Ahmed-DataScientist) and [LinkedIn](https://www.linkedin.com/in/ahmed-awan-792795229)

    This chatbot is powered by Ahmed Awan and Google's Gemini model to help you learn, explore, and chat intelligently! 🤖💬
    """)

# Replace with your Gemini API key
api_key = "AIzaSyAgoVIGdbMhE_p2-us4rAxbr3lIVcBi1Ak"
genai.configure(api_key=api_key)

# Use the correct model name
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

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
