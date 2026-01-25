from pathlib import Path
import streamlit as st
import pandas as pd
import random

BASE_DIR = Path(__file__).resolve().parent.parent
CATEGORY_DIR = BASE_DIR / "data" / "category"
VERBS_DIR = BASE_DIR / "data" / "alpha-verbs"


@st.cache_data
def load_data(file_name, work="category"):
    if work == "category":
        return pd.read_csv(CATEGORY_DIR / file_name)
    elif work == "verbs":
        return pd.read_csv(VERBS_DIR / file_name)
    else:
        raise ValueError("Invalid work type")

def get_category_map():
    return {
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

def get_eng_or_card_ui(english, odia):
    
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

def random_motivation_emojis():
    MOTIVATION_EMOJIS = [
        "🌟", "🎉", "👏", "💪", "🔥", "🚀", "⭐",
        "😊", "😄", "😁", "🥳", "🏆", "🎯",
        "🧠", "📚", "✌️", "👍", "💡", "🌈"
    ]
    
    emoji = random.choice(MOTIVATION_EMOJIS)
    st.toast(icon=emoji, body=".")

def show_toast_once(message):
    if st.session_state.last_toast != message:
        st.toast(message, icon="😁")
        st.session_state.last_toast = message

def choose_df(
    df,
    category, CATEGORY_MAP,
    alpha_verbs, ALPHABETICAL_MAP
    ):
    
    if category:
        df = load_data(CATEGORY_MAP[category], "category")
        show_toast_once(f"Loaded category: {category}")

    elif alpha_verbs:
        df = load_data(ALPHABETICAL_MAP[alpha_verbs], "verbs")
        show_toast_once(f"Loaded verbs starting with: {alpha_verbs}")

    else:
        st.info("Please select କଣ ଖେଳିବ 👆")

    return df

def get_random(df):
    row = df.sample(1).iloc[0]
    return row["english"], row["odia"]