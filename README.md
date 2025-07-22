# 🧠 GenAI Medical Chatbot

A GenAI-powered chatbot designed to assist with medical queries using Retrieval-Augmented Generation (RAG) via LangChain, HuggingFace Embeddings, OpenAI LLMs, and Pinecone Vector DB.

## 🚀 Features

- Flask-based web interface
- Retrieval-Augmented Generation (RAG) architecture
- Context-aware medical Q&A using OpenAI
- HuggingFace embeddings for document representation
- Pinecone vector store for similarity search
- Simple and extensible codebase

---

## 🧱 Tech Stack

- **Backend**: Python, Flask
- **LLM**: OpenAI GPT models
- **Embeddings**: HuggingFace
- **Vector DB**: Pinecone
- **RAG**: LangChain framework
- **Environment**: dotenv for API keys

---

## 🗂️ Project Structure

## 🗂️ Project Structure

```text
├── app.py               # Main Flask app
├── templates/
│   └── index.html       # Chat UI (Flask template)
├── src/
│   ├── helper.py        # Embedding download and helpers
│   └── prompt.py        # Custom system prompt
├── .env                 # API keys and config (not committed)
├── requirements.txt     # Python dependencies
└── README.md
```


---

## 🔑 Environment Variables

Create a `.env` file in the root directory with the following:

```env
OPENAI_API_KEY=your_openai_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## 1. Clone the repo

```
git clone https://github.com/phaniram05/genai-medical-chatbot.git
cd genai-medical-chatbot
```

## 2. Create and activate a virtual environment

```
conda create --name <ENV_NAME>
conda activate <ENV_NAME>
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

## 4. Update API Keys

```
Add / Update your API Keys inside .env
```

## Running the App

```
python app.py
```
