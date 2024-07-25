import google.generativeai as genai
import streamlit as st

# Set your API key
api_key = "AIzaSyBuesdkuzLi9F-1hew1qIFnt7UX8z86M3A"
genai.configure(api_key=api_key)

# Load the Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def generate_code(prompt):
    try:
        response = chat.send_message(prompt)
        code = ""
        for chunk in response:
            if hasattr(chunk, 'text'):
                code += chunk.text
            else:
                code += "Response does not contain valid text."
        return code
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit app
st.title("Code Generation with Gemini LLM")
prompt = st.text_area("Enter your code generation prompt:", height=100)

if st.button("Generate Code"):
    if prompt:
        generated_code = generate_code(prompt)
        st.subheader("Generated Code:")
        st.code(generated_code)
    else:
        st.warning("Please enter a prompt to generate code.")
