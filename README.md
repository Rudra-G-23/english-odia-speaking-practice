# 🧑‍🏫 English–Odia Speaking Practice App

A simple and interactive **Streamlit-based learning app** to help 5 to 8 year small children practice **English and Odia words with pronunciation**.  

This project is especially useful for **children and early learners** to improve speaking and vocabulary.

Build for my small little brother. 😉

![pic](/assets/english-to-odia-speaking-v2.png)

[Live: https://english-odia-speaking-practice-with-rudra.streamlit.app/](https://english-odia-speaking-practice-with-rudra.streamlit.app/)

---

## ✨ Features

- 📚 Category-wise learning (Animals, Fruits)
- 🔤 English ↔ Odia word display
- 🔊 Text-to-Speech pronunciation
- 🎲 Random word generator
- 🎚 Adjustable speech rate & volume
- 🌐 Runs in browser using Streamlit

---

## 🛠 Tech Stack

- **Python**
- **Streamlit** – UI & web app
- **pandas** – data handling
- **gTTS** – text-to-speech (audio file generation)
- **HTML** – simple styling

---

## 📂 Project Structure

```
english-odia-speaking-practice/
│
├── main.py
├── README.md
├── data/
│   ├── animals.csv
│   └── fruits.csv
│   └── ..
└── pyproject.toml
```

---

## ▶️ How to Run the App

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/english-odia-speaking-practice.git
cd english-odia-speaking-practice
```

### 2️⃣ Create virtual environment (optional but recommended)

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit app

```bash
streamlit run main.py
```

---

## 📊 Dataset Format

### Example (`animals.csv`)

```csv
english,odia
Dog,କୁକୁର
Cat,ବିଲେଇ
Elephant,ହାତୀ
```

---

## 🧠 Learning Use Case

* English–Odia beginners
* Children pronunciation practice
* Spoken English foundation
* Regional language learning support

---

## 🚀 Category are available
```python
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

"Alphabetical Verbs Dataset"
```



---

## 👤 Author

**Rudra Prasad Bhuyan**

* GitHub: [https://github.com/Rudra-G-23](https://github.com/Rudra-G-23)
* LinkedIn: [https://www.linkedin.com/in/rudra-prasad-bhuyan-44a388235](https://www.linkedin.com/in/rudra-prasad-bhuyan-44a388235)

---

## 📜 License

This project is open-source and free to use for learning purposes.

