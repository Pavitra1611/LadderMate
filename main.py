import openai
import streamlit as st

# Point to LM Studio's local API
openai.api_base = "http://127.0.0.1:1234/v1"
openai.api_key = "lm-studio"  # Dummy key for local models

# Function to send a Ladder Logic prompt
def ask_model(prompt, system_instruction=None):
    messages = []

    if system_instruction:
        messages.append({"role": "system", "content": system_instruction})

    messages.append({"role": "user", "content": prompt})

    try:
        response = openai.ChatCompletion.create(
            model="deepseek-coder-6.7b-instruct",
            messages=messages,
            temperature=0.5,
            max_tokens=1024,
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Example Streamlit UI usage
if __name__ == "__main__":
    st.title("LadderMate: PLC Ladder Logic AI")
    user_input = st.text_area("Enter your Ladder Logic or question:")
    
    if st.button("Explain / Translate"):
        with st.spinner("Thinking..."):
            explanation = ask_model(user_input, system_instruction="You are a helpful assistant that explains PLC Ladder Logic to beginners.")
            st.markdown("### 🔍 Explanation:")
            st.write(explanation)
