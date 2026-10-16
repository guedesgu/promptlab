# PromptLab 🧪

**A hands-on laboratory for prompt engineering and generative AI experimentation.**

PromptLab is a Python application built with Streamlit and the Google Gemini API. It allows users to test instructions, experiment with different prompts, and explore how prompt design influences AI-generated responses.

## ✨ Features

- **Custom prompts:** Write and modify instructions for the AI.
- **Text input:** Provide content for the model to analyze.
- **AI-generated responses:** Process inputs using the Google Gemini API.
- **Interactive interface:** Run experiments through a simple Streamlit web app.
- **Secure API configuration:** Keep credentials outside the source code.

## 🛠️ Technologies

- Python
- Streamlit
- Google Gen AI SDK
- Gemini API
- Git and GitHub

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/guedesgu/promptlab.git
cd promptlab
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install streamlit google-genai
```

### 4. Configure the Gemini API key

Create a file named `.streamlit/secrets.toml` in the project directory:

```toml
GEMINI_API_KEY = "YOUR_API_KEY_HERE"
```

Replace the placeholder with your own Gemini API key. Never commit this file or share your API key publicly.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

## 🎯 Project Goals

PromptLab is a learning and portfolio project focused on:

- Prompt engineering experimentation.
- Generative AI integration with Python.
- Evaluating how instructions affect model outputs.
- Building practical applications with AI APIs.

## 🗺️ Roadmap

- [x] Integrate the Gemini API.
- [x] Build an interactive Streamlit interface.
- [ ] Compare different prompts using the same input.
- [ ] Add structured response evaluation criteria.
- [ ] Track and compare experiment results.
- [ ] Deploy a public demo.

## 👨‍💻 Author

**Gustavo Guedes de Macena**

Software Engineering student interested in Python, generative AI, prompt engineering, and practical software development.

GitHub: [@guedesgu](https://github.com/guedesgu)

---

*Built as a hands-on project to explore prompt engineering and generative AI development.*