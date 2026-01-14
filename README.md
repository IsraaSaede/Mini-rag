# 🧠 mini-rag-app

A lightweight, modular **Retrieval-Augmented Generation (RAG)** application built with Python. This project demonstrates how to combine document retrieval with large language models to answer user queries using custom, context-rich data.

---

## 🔍 What is RAG?

**Retrieval-Augmented Generation (RAG)** is an approach that enhances a language model’s output by retrieving relevant information from external sources (e.g., local documents or databases). Instead of relying solely on pre-trained knowledge, RAG systems search for context and then generate informed, accurate, and up-to-date responses.

---

## 🚀 Features

* 🔎 Embed and search documents using vector stores like FAISS or Chroma
* 🧠 Augment LLM responses with retrieved context
* 📂 Support for local files (e.g., PDF, TXT)
* 🧪 Simple API interface (via FastAPI)
* 🧰 Easily extendable for OpenAI, Hugging Face, or local models

---

## ⚙️ Requirements

Make sure you have **Python 3.9+** installed.

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Key dependencies include:

* `fastapi`
* `uvicorn[standard]`
* `python-multipart`
* `langchain`
* `openai` *(optional if using OpenAI models)*
* `chromadb` or `faiss-cpu`
* `python-dotenv`

---

## 🔐 Environment Variables

You’ll need to provide API keys and other settings in an environment file.

### Step 1: Copy the example environment file

```bash
cp .env.example .env
```

### Step 2: Set your OpenAI API key

Edit `.env` and replace with your actual credentials:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> You can add other keys depending on your model provider (e.g., Hugging Face).

---

## 🧪 Running the App

You can run the application using FastAPI and Uvicorn:

```bash
uvicorn app:app --reload
```

Or if you’ve built a Streamlit-based UI:

```bash
streamlit run app.py
```

---

## 💡 Terminal Customization (Optional)

For a cleaner terminal prompt while working on the project, run:

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

To make it permanent, add it to your shell config file:

```bash
echo 'export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "' >> ~/.bashrc
```

---

## 🧰 Coming Soon / Ideas

* 🔄 Document upload endpoint
* 🧩 Pluggable LLM backends
* 🧠 Multi-document context retrieval
* 📈 Vector DB switch (e.g., Qdrant, Weaviate)

---

## 📝 License

This project is open-source and available under the MIT License.
