
# 📄 Chat with Your PDF

A document-based question-answering application built using **Python, Streamlit, LangChain, ChromaDB, and GeminiAI**. Upload PDF documents, extract text, generate embeddings, and ask questions to receive answers grounded in the document.

## 🚀 Features

- Upload one or multiple PDF files.
- Extract text from PDF documents.
- Split text into smaller, searchable chunks.
- Generate embeddings using GeminiAI embedding models.
- Store and retrieve document vectors using ChromaDB.
- Ask questions through an interactive Streamlit chat interface.
- Generate answers using retrieved PDF content.
- Display relevant source passages and page references.
- Maintain conversation history during the session.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web interface |
| LangChain | Document processing and LLM orchestration |
| ChromaDB | Vector database |
| GeminiAI Embeddings | Text vectorization |
| GeminiAI Chat Model | Answer generation |
| PyPDF | PDF text extraction |

## 📁 Project Structure

```text
chat_with_pdf/
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Prerequisites

Install the following:

- Python 3.10 or later
- Visual Studio Code
- An GeminiAI API key with access to the required models

### 2. Open the Project

Open VS Code, select **File → Open Folder**, and choose the project directory.

Open the integrated terminal using **Terminal → New Terminal**.

### 3. Create a Virtual Environment

Run the following command in PowerShell:

```powershell
py -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If activation is blocked, use the virtual environment's Python executable directly.

### 4. Install Dependencies

Upgrade pip:

```powershell
python -m pip install --upgrade pip
```

Install the required packages:

```powershell
pip install -r requirements.txt
```

If the virtual environment is not activated, run:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create the `.env` file from the template:

```powershell
Copy-Item .env.example .env
```

Add your GeminiAI API key to `.env`:

```dotenv
GEMINIAI_API_KEY=your_actual_api_key_here
```

Replace the placeholder with your actual API key.

If `.env.example` does not exist, create a file named `.env` manually in the same directory as `app.py`.

**Security:** Never share your API key or commit the `.env` file to GitHub.

### 6. Run the Application

Start the Streamlit server:

```powershell
python -m streamlit run app.py
```

If the virtual environment is not activated:

```powershell
.\.venv\Scripts\python.exe -m streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 💬 How to Use

1. Open the application in your browser.
2. Upload one or more PDF files.
3. Click the button to process the documents.
4. Wait for text extraction, chunking, embedding, and indexing to finish.
5. Enter a question in the chat input.
6. Review the answer and supporting source passages.

### Example Questions

- Summarize the document.
- What are the main findings?
- Explain the methodology used in the report.
- What important dates are mentioned?
- Which page discusses the conclusion?
- Is a particular fact mentioned in the PDF?

The application is designed to indicate when the retrieved content does not support an answer.

## 🔄 Application Workflow

```text
Upload PDF
    ↓
Extract PDF Text
    ↓
Split Text into Chunks
    ↓
Generate Embeddings
    ↓
Store Vectors in ChromaDB
    ↓
Retrieve Relevant Passages
    ↓
Send Context to the Language Model
    ↓
Display Answer and Source References
```

## 🔐 Answer Grounding

The application uses **Retrieval-Augmented Generation (RAG)**. It retrieves relevant passages from uploaded documents and supplies them to the language model as context.

The prompt instructs the model to answer using only the supplied passages and to indicate when information is unavailable.

This approach reduces unsupported answers but cannot guarantee complete accuracy. Verify source passages for important decisions.

## ⚠️ Troubleshooting

### `requirements.txt` Not Found

Make sure the terminal is open in the project directory containing `requirements.txt`.

Check the current directory:

```powershell
Get-Location
dir -Force
```

### `ModuleNotFoundError`

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

### API Key or Authentication Error

Verify that your API key is valid and that your account has access to the selected models.

### No Text Extracted from PDF

The document may contain scanned images instead of selectable text. OCR is required to extract text from scanned pages.

### Streamlit Command Not Found

Run:

```powershell
python -m streamlit run app.py
```

### Port Already in Use

Run the app on another port:

```powershell
python -m streamlit run app.py --server.port 8502
```


## 👨‍💻 Author
Name     : SIVA SHANKAR MAMIDISETTI
Ph.No    : 7330712258
Email    : sivamamidisetti98765@gmail.com
[Linkedin](https://www.linkedin.com/in/siva-shankar-mamidisetti)

