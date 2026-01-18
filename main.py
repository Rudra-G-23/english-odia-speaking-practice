import streamlit as st
from pathlib import Path
import pandas as pd
import pyttsx3
import tempfile

# ---------------- Page Config ----------------
st.set_page_config(
    page_icon="🧑‍🏫",
    page_title="English-Odia Speaking",
)

# ---------------- Sidebar ----------------
with st.sidebar:
    category = st.selectbox(
        "📚 Select Category",
        ["Animal 🐘", "Fruits 🍎"]
    )

    rate = st.slider("Rate:", 100, 250, 150, step=10)
    volume = st.slider("Volume:", 0.1, 1.0, 0.9, step=0.1)

# ---------------- Load Data ----------------
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data(file_name):
    return pd.read_csv(DATA_DIR / file_name)

if category == "Animal 🐘":
    df = load_data("animals.csv")
else:
    df = load_data("fruits.csv")

# ---------------- Helper ----------------
def get_random(df):
    row = df.sample(1).iloc[0]
    return row["english"], row["odia"]

# ---------------- Session State ----------------
if "word" not in st.session_state:
    st.session_state.word = get_random(df)

english, odia = st.session_state.word

# ---------------- UI ----------------
st.header("👩‍🏫 English-Odia Speaking Practice")

col_en, col_or = st.columns(2)

with col_en:
    st.markdown(
        f"""
        <div style="background:#e3f2fd;padding:20px;border-radius:20px;text-align:center;">
            <div style="font-size:22px;">🇬🇧 English</div>
            <div style="font-size:32px;font-weight:800;color:#1565c0;margin-top:10px;">
                {english}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col_or:
    st.markdown(
        f"""
        <div style="background:#e8f5e9;padding:20px;border-radius:20px;text-align:center;">
            <div style="font-size:22px;">🇮🇳 Odia</div>
            <div style="font-size:36px;font-weight:800;color:#2e7d32;margin-top:10px;">
                {odia}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# ---------------- Speak Logic (SAFE) ----------------
def speak(text, rate, volume):
    # create temp wav file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as fp:
        audio_path = fp.name

    engine = pyttsx3.init(driverName="sapi5")
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)

    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[0].id)

    engine.save_to_file(text, audio_path)
    engine.runAndWait()
    engine.stop()

    return audio_path


# ---------------- Buttons ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("Speak 🔊"):
        audio_file = speak(english, rate, volume)
        st.audio(audio_file, format="audio/wav")

with col2:
    if st.button("Random 🎲"):
        st.session_state.word = get_random(df)
        st.rerun()