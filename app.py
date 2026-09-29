import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

# -----------------------------
# Configuration
# -----------------------------
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key is missing.")
    st.stop()

client = genai.Client(api_key=api_key)

st.set_page_config(
    page_title="Gemini AI ChatBot",
    page_icon="🤖",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #0b1020 0%, #111827 50%, #172554 100%);
}

/* Remove Streamlit top padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 850px;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    margin-bottom: 5px;
    background: linear-gradient(90deg, #8b5cf6, #38bdf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #94a3b8;
    font-size: 17px;
    margin-bottom: 30px;
}

/* AI badge */
.ai-badge {
    width: fit-content;
    margin: 0 auto 18px auto;
    padding: 7px 15px;
    border-radius: 30px;
    background: rgba(139, 92, 246, 0.15);
    border: 1px solid rgba(139, 92, 246, 0.4);
    color: #c4b5fd;
    font-size: 14px;
}

/* Prompt box */
.stTextArea textarea {
    background: rgba(15, 23, 42, 0.85) !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 16px !important;
    font-size: 16px !important;
}

/* Generate button */
.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 13px;
    font-size: 17px;
    font-weight: 700;
    color: white;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    transition: 0.3s;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 8px 25px rgba(59, 130, 246, 0.35);
}

/* Response card */
.response-card {
    margin-top: 25px;
    padding: 22px;
    border-radius: 18px;
    background: rgba(15, 23, 42, 0.75);
    border: 1px solid #334155;
    box-shadow: 0px 10px 35px rgba(0, 0, 0, 0.25);
}

.response-title {
    color: #a78bfa;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
}

/* Footer */
.footer {
    text-align: center;
    color: #64748b;
    font-size: 13px;
    margin-top: 35px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Header
# -----------------------------
st.markdown(
    '<div class="ai-badge">✦ POWERED BY GEMINI AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Gemini AI ChatBot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask questions. Explore ideas. Learn something new.</div>',
    unsafe_allow_html=True
)

# -----------------------------
# Prompt
# -----------------------------
prompt = st.text_area(
    "Your prompt",
    placeholder="✨ Ask me anything...",
    height=140,
    label_visibility="collapsed"
)

# -----------------------------
# Generate Response
# -----------------------------
if st.button("✦ Generate Response"):

    if prompt.strip():

        with st.spinner("Gemini is thinking..."):

            try:

                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                st.markdown(
                    '<div class="response-card">'
                    '<div class="response-title">🤖 Gemini Response</div>',
                    unsafe_allow_html=True
                )

                st.write(response.text)

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:

                st.error(f"Something went wrong: {e}")

    else:

        st.warning("Please enter a prompt first.")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    '<div class="footer">Gemini AI ChatBot • Built with Python & Streamlit</div>',
    unsafe_allow_html=True
)