import streamlit as st
from pathlib import Path
import random
import os
import tempfile
import base64
from gtts import gTTS

BASE_DIR = Path(__file__).resolve() .parent.parent
TEXT_FILE_DIR = BASE_DIR / "data" / "text"
ONLY_ENGLISH_WORD_FILE_PATH = os.path.join(TEXT_FILE_DIR, "one-lakhs-english-words-formatted.txt")

def selected_random_line(path, k):
    """
    Reservoir Sampling method used for memory efficiently.
        
    :param path: path of the file.
    :param k: num_line
    """
    selected_lines = []

    with open(path, 'r') as f:
        
        for i, line in enumerate(f):
            if i <  1:
                selected_lines.append(line)
            
            elif random.random() < k / (i +1):
                replace_idx = random.randrange(k)
                selected_lines[replace_idx] = line

    return selected_lines

def clean_list(list_of_words):
    
    result_list = []
    
    for item in list_of_words:
        words = item.split(',')
        
        for word in words:
            clean_word = word.strip().replace('\n', '')
            
            if clean_word:
                result_list.append(clean_word)

    return result_list

def question_generator(list_of_words):
    three_words = set(random.sample(list_of_words, 3))
    question_word = random.choice(list(three_words))
    return question_word, three_words

def get_target_and_options(path, num_line):
    """
    Get text from the file and clean and provide the target and options.
    """
    list_of_words = selected_random_line(path, k=num_line)
    list_of_words = clean_list(list_of_words)
    target_word, options = question_generator(list_of_words)
    return target_word, options

def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        return fp.name
    
def hide_audio_track(audio_path):
    audio_placeholder = st.empty()
    
    with open(audio_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    audio_base64 = base64.b64encode(audio_bytes).decode('utf-8')
    audio_tag = f"""
        <audio autoplay>
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
    """
    audio_placeholder.markdown(audio_tag, unsafe_allow_html=True)

def random_trigger():
        target, options = get_target_and_options(ONLY_ENGLISH_WORD_FILE_PATH, num_line=1)
        st.session_state.target_word = target
        st.session_state.options = options
        st.session_state.answered = False
        