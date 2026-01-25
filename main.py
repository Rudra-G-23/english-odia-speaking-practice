import streamlit as st

from app.see import (
    get_category_map,
    get_eng_or_card_ui,
    random_motivation_emojis,
    choose_df,
    get_random
)

from app.quiz import (
    speak,
    hide_audio_track,
    random_trigger
)


st.set_page_config(
    page_icon="🧑‍🏫",
    page_title="English-Odia Speaking",
)

st.header("👩‍🏫 English-Odia Speaking Practice")


CATEGORY_MAP = get_category_map()

ALPHABETICAL_MAP = {
    chr(i): f"{chr(i).lower()}.csv" for i in range(ord("A"), ord("Z") + 1)
}

# ---------------- UI Display ----------------
tab1, tab2 = st.tabs(["🙈 ଦେଖ (See)", "🙉 ଶୁଣ (Listen)"])

with tab1:
    # ---------------- UI Selection ----------------
    with st.expander(" 🔖 ଶ୍ରେଣୀ: Select Category"):
        category = st.pills(
            label="",
            options=list(CATEGORY_MAP.keys()),
            selection_mode="single"
        )

    with st.expander("🔠 କ୍ରିୟା : Verbs"):
        alpha_verbs = st.pills(
            label="",
            options=list(ALPHABETICAL_MAP.keys()),
            selection_mode="single"
        )

    # ---------------- Choose df ----------------
    df = None
    
    df = choose_df(df,
        category, CATEGORY_MAP,
        alpha_verbs, ALPHABETICAL_MAP
        )

    with st.expander("😉 ସବୁ ଶବ୍ଦ: All Words"):
        st.dataframe(df)
        
    st.write("---")

    # ---------------- Session State ----------------
    if df is not None:
        if "word" not in st.session_state:
            st.session_state.word = get_random(df)
                
    if df is not None and "word" in st.session_state:
        english, odia = st.session_state.word
        get_eng_or_card_ui(english, odia)
        
    if df is not None and "word" in st.session_state:

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🔊 Speak"):
                audio_file = speak(english, lang="en")
                hide_audio_track(audio_file)

        with col2:
            if st.button("🎲 Random"):
                st.session_state.word = get_random(df)
                random_motivation_emojis
                st.rerun()



with tab2:
            
    if "target_word" not in st.session_state:
        st.session_state.target_word = None
        st.session_state.options = []
        st.session_state.answered = False

    col1, col2 = st.columns(2)

    with col2:
        if st.button("⏭️"):
            random_trigger()
            random_motivation_emojis()
            
    with col1:
        if st.session_state.target_word:
            if st.button("🔊"):
                audio_path = speak(st.session_state.target_word)
                hide_audio_track(audio_path)
                

    if st.session_state.options:
        user_choice = st.pills(
            label="Choose the correct word / କେଉଁ ଶବ୍ଦ ଶୁଣିଲ ? ",
            options=st.session_state.options,
            selection_mode="single"
        )

        if user_choice:
            
            if user_choice == st.session_state.target_word:
                st.success("✅ ଠିକ୍ ଅଛି, ଆଉ ଥରେ . . . . !", icon="🎉")
            
            else:
                st.toast("😜 ନା, ଭଲ କି ଶୁଣନ୍ତୁ !", icon="⚠️")
                audio_path = speak(user_choice)
                hide_audio_track(audio_path)
