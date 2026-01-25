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

st.header("👩‍🏫 English-Odia Speaking Practice")

# ---------------- Paths ----------------
BASE_DIR = Path(__file__).parent
CATEGORY_DIR = BASE_DIR / "data" / "category"
VERBS_DIR = BASE_DIR / "data" / "alpha-verbs"

# ---------------- Load Data ----------------
@st.cache_data
def load_data(file_name, work="category"):
    if work == "category":
        return pd.read_csv(CATEGORY_DIR / file_name)
    elif work == "verbs":
        return pd.read_csv(VERBS_DIR / file_name)
    else:
        raise ValueError("Invalid work type")

# ---------------- Category Mapping ----------------
CATEGORY_MAP = {
    "🐘 Animal": "animals.csv",
    "🍎 Fruits": "fruits.csv",
    "🎨 Colors": "colour.csv",
    "👀 Body Parts": "body-part.csv",
    "👨‍👩‍👧‍👦 Family": "family.csv",
    "🫡 Noun Word": "noun-word.csv",
    "📏 Classroom Objects": "classroom-objects.csv",
    "🛖 House Objects": "house-objects.csv",
    "♾️ Adjective": "adjective.csv",
    "🔅 Prepositions": "prepositions.csv",
    "😃 Polite Word": "polite-word.csv",
    "🌞 Daily Actions": "daily-actions.csv",
    "⛹️ Play Actions": "play-actions.csv",
    "🏠 Home Actions": "home-actions.csv",
    "🎒 School Actions": "school-actions.csv",
    "🤏 Small Sentences": "small-sentences.csv",
    "🙋 Questions Sentences": "questions-sentences.csv",
}

ALPHABETICAL_MAP = {
    chr(i): f"{chr(i).lower()}.csv" for i in range(ord("A"), ord("Z") + 1)
}

# ---------------- Toast Logic ----------------
if "last_toast" not in st.session_state:
    st.session_state.last_toast = None

def show_toast_once(message):
    if st.session_state.last_toast != message:
        st.toast(message, icon="😁")
        st.session_state.last_toast = message

# ---------------- UI Selection ----------------
with st.expander(" 🔖 Select Category"):
    category = st.pills(
        label="",
        options=list(CATEGORY_MAP.keys()),
        selection_mode="single"
    )

with st.expander("🔠 Verbs"):
    alpha_verbs = st.pills(
        label="",
        options=list(ALPHABETICAL_MAP.keys()),
        selection_mode="single"
    )

# ---------------- Choose df ----------------
df = None

if category:
    df = load_data(CATEGORY_MAP[category], "category")
    show_toast_once(f"Loaded category: {category}")

elif alpha_verbs:
    df = load_data(ALPHABETICAL_MAP[alpha_verbs], "verbs")
    show_toast_once(f"Loaded verbs starting with: {alpha_verbs}")

else:
    st.info("Please select a category or verb 👆")

with st.expander("😉 All Words"):
    st.dataframe(df)
    
st.write("---")

# ---------------- Helper ----------------
def get_random(df):
    row = df.sample(1).iloc[0]
    return row["english"], row["odia"]

# ---------------- Session State ----------------
if df is not None:
    if "word" not in st.session_state:
        st.session_state.word = get_random(df)

# ---------------- UI Display ----------------
if df is not None and "word" in st.session_state:

    english, odia = st.session_state.word

    col_en, col_or = st.columns(2)

    with col_en:
        st.markdown(
            f"""
            <div style="background:#e3f2fd;padding:20px;border-radius:20px;text-align:center;">
                <div style="font-size:22px;">🇬🇧</div>
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
                <div style="font-size:22px;">🇮🇳</div>
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
if df is not None and "word" in st.session_state:

    col1, col2 = st.columns(2)
    audio_placeholder = st.empty()

    with col1:
        if st.button("🔊 Speak"):
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
        if st.button("🎲 Random"):
            st.session_state.word = get_random(df)
            st.rerun()

