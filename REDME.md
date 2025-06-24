# 🧠 Mini RAG App

A minimal Retrieval-Augmented Generation (RAG) application using Python. This project shows how to combine document retrieval with a language model to answer questions using your own data.

---

## 🚀 Quick Start

### 1. Clone the project

```bash
git clone https://github.com/IsraaSaede/mini-rag.git
cd mini-rag
````

### 2. Set up environment

Make sure you have **Python 3.10+** installed.

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the `.env` example and add your OpenAI key:

```bash
cp .env.example .env
```

Edit `.env` and set your API key:

```env
OPENAI_API_KEY=your_key_here
```

---

## ▶️ Run the App

```bash
python app.py
```

Or if using Streamlit:

```bash
streamlit run app.py
```

---

## 🛑 Notes

* Don't include large files like `Miniconda3-latest-Linux-x86_64.sh`
* Use `.gitignore` to avoid tracking virtual environments and binaries

