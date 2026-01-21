import streamlit as st
from pathlib import Path
import pandas as pd
import tempfile
import base64
from gtts import gTTS

# ---------------- Page Config ----------------
st.set_page_config(
    page_icon="🧑‍🏫",
    page_title="English-Odia Speaking",
)

# ---------------- Sidebar ----------------
with st.sidebar:
    category = st.selectbox(
        "📚 Select Category",
        [
            "Animal 🐘",
            "Fruits 🍎",
            "Colour 🎨",
            "Body Parts 👀👃👂",
            "Family 👨‍👩‍👧‍👦",
            "Noun Word 🫡",
            "Adjective 📢",
            "Classroom Objects 📏",
            "House Objects 🛖",
            "Prepositions",
            "Polite Word",
            "Daily Actions",
            "Play Actions",
            "Home Actions",
            "School Actions",
            "Small Sentences",
            "Questions Sentences"
         ]
    )

# ---------------- Load Data ----------------
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def load_data(file_name):
    return pd.read_csv(DATA_DIR / file_name)

if category == "Animal 🐘":
    df = load_data("animals.csv")
elif category == "fruits.csv":
    df = load_data("fruits.csv")
elif category == "Body Parts 👀👃👂":
    df = load_data("body-part.csv")
elif category == "Family 👨‍👩‍👧‍👦":
    df = load_data("family.csv")
elif category == "Noun Word 🫡":
    df = load_data("noun-word.csv")
elif category == "Colour 🎨":
    df = load_data("colour.csv")
elif category == "Classroom Objects 📏":
    df = load_data("classroom-objects.csv")
elif category == "House Objects 🛖":
    df = load_data("house-objects.csv")
elif category == "Adjective 📢":
    df = load_data("adjective.csv")
elif category == "Prepositions":
    df = load_data("prepositions.csv")
elif category == "Polite Word":
    df = load_data("polite-word.csv")
elif category == "Daily Actions":
    df = load_data("daily-actions.csv")
elif category == "Play Actions":
    df = load_data("play-actions.csv")
elif category == "School Actions":
    df = load_data("school-actions.csv")
elif category == "Home Actions":
    df = load_data("home-actions.csv")
elif category == "Small Sentences":
    df = load_data("small-sentences.csv")
elif category ==  "Questions Sentences":
    df = load_data("questions-sentences.csv")
    
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

# ---------------- Speak Logic ----------------
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name

# ---------------- Buttons ----------------
col1, col2 = st.columns(2)

audio_placeholder = st.empty()

with col1:
    if st.button("Speak 🔊"):
        audio_file = speak(english, lang="en")

        with open(audio_file, "rb") as f:
            audio_bytes = f.read()

        audio_base64 = base64.b64encode(audio_bytes).decode()

        audio_html = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """

        audio_placeholder.markdown(audio_html, unsafe_allow_html=True)


with col2:
    if st.button("Random 🎲"):
        st.session_state.word = get_random(df)
        st.rerun()