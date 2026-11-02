# 🚀 ATS Resume Scorer

**An AI-powered resume analyzer that evaluates how well your resume matches a job description and provides actionable recommendations to improve your chances of passing Applicant Tracking Systems (ATS).**

Built using **FastAPI, Streamlit, spaCy, Sentence Transformers, and Groq LLM**.

---

## ✨ Key Features

- 📄 **Resume Parsing:** Upload resumes in PDF, DOC, or DOCX format.
- 🎯 **ATS Compatibility Score:** Evaluate how well your resume aligns with a job description.
- 🧠 **Semantic Matching:** Use Sentence Transformers to measure contextual similarity between resumes and job descriptions.
- 🔍 **Skill Validation:** Identify matching skills and missing qualifications.
- 📊 **Detailed Score Breakdown:** Analyze formatting, keywords, content, skill validation, and ATS compatibility.
- 🤖 **AI-Powered Suggestions:** Generate personalized improvement recommendations using the Groq API (Llama 3).
- 📚 **Analysis History:** Save previous resume analyses and revisit them through your account.
- 📑 **PDF Reports:** Export detailed analysis reports.

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | FastAPI |
| Programming Language | Python |
| NLP | spaCy (`en_core_web_md`) |
| Semantic Similarity | Sentence Transformers (`all-MiniLM-L6-v2`) |
| LLM Integration | Groq API (Llama 3) |
| Authentication | Supabase Auth |
| Database | Supabase |
| PDF Generation | WeasyPrint, Jinja2 |

---

## ⚙️ How It Works

1. **Upload Resume:** Upload your resume in PDF, DOC, or DOCX format.
2. **Enter Job Description:** Paste the job description for the role you are targeting.
3. **Resume Parsing:** The backend extracts relevant information, skills, and experience.
4. **Semantic Analysis:** NLP models compare your resume with the job description.
5. **ATS Scoring:** Generate an overall score and category-wise evaluation.
6. **AI Recommendations:** Receive actionable suggestions to improve your resume.
7. **Download Report:** Export your results as a PDF report.

---

## 📁 Project Structure

```text
ATS_SCORER/
│
├── backend/                    # FastAPI backend and NLP services
│   ├── api/                    # API routes and authentication
│   ├── core/                   # Application configuration
│   ├── database/               # Supabase database integration
│   ├── models/                 # Pydantic schemas
│   ├── services/               # Resume analysis and scoring services
│   ├── templates/              # PDF report templates
│   └── utils/                  # Utility functions
│
├── frontend/                   # Streamlit frontend
│   ├── assets/                 # CSS and static assets
│   ├── components/              # Reusable UI components
│   ├── services/                # API and Supabase clients
│   ├── views/                   # Application pages
│   └── streamlit_app.py         # Frontend entry point
│
├── dataset/                    # Resume and job description datasets
│
├── jupyter_notebook/           # Model experimentation and research
│   ├── BERT_FINETUNE.ipynb
│   ├── BERT_embeddings.ipynb
│   └── EDA_and_data_prep.ipynb
│
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
└── README.md
```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/tanvisharma5485/ATS_SCORER.git
cd ATS_SCORER
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS:**

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Download the spaCy language model:

```bash
python -m spacy download en_core_web_md
```

### 4. Install WeasyPrint System Dependencies

WeasyPrint requires additional system libraries on Linux.

**Fedora:**

```bash
sudo dnf install -y cairo pango gdk-pixbuf2 libffi
```

**Debian / Ubuntu:**

```bash
sudo apt install -y libcairo2 libpango-1.0-0 libpangoft2-1.0-0 libffi-dev
```

### 5. Configure Environment Variables

Create your environment file:

```bash
cp .env.example .env
```

On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Configure the following credentials in `.env`:

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_service_role_key
SUPABASE_ANON_KEY=your_supabase_anon_key
GROQ_API_KEY=your_groq_api_key
```

**Required services:**

- **Supabase:** Create a project and obtain your API credentials from Project Settings → API.
- **Groq:** Generate an API key from [Groq Console](https://console.groq.com/).
- **Google OAuth (Optional):** Configure Google sign-in through your Supabase dashboard.

The Streamlit frontend also uses:

```text
frontend/.streamlit/secrets.toml
```

Create it using your `secrets.toml.example` template and configure the required Supabase credentials.

**Never commit `.env` or `secrets.toml` to GitHub.**

---

## ▶️ Running the Application

The application consists of two independent services: a FastAPI backend and a Streamlit frontend.

### 1. Start the Backend

From the project root:

```bash
uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000
```

Backend API:

```text
http://localhost:8000
```

### 2. Start the Frontend

Open a new terminal, activate your virtual environment, and run:

```bash
streamlit run frontend/streamlit_app.py
```

Frontend application:

```text
http://localhost:8501
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/v1/analyze-resume` | Analyze a resume against a job description |
| GET | `/api/v1/history` | Retrieve analysis history |
| DELETE | `/api/v1/history/:id` | Delete a history entry |
| GET | `/api/v1/health` | Check backend health |
| POST | `/api/v1/generate-pdf` | Generate a PDF report |

---

## 🧠 NLP Models

| Model | Purpose |
|---|---|
| spaCy `en_core_web_md` | Resume text processing and linguistic analysis |
| Sentence Transformers `all-MiniLM-L6-v2` | Semantic similarity between resumes and job descriptions |
| Groq Llama 3 | AI-generated resume improvement suggestions |

**Note:** The Sentence Transformer model is downloaded automatically on its first use and cached locally (approximately 80 MB for the standard model).

---

## 🔐 Security & Configuration

- Keep API keys and credentials in environment variables.
- Never upload `.env` or `secrets.toml` to GitHub.
- Use Supabase authentication for user access.
- Keep sensitive credentials out of source code.
- Store production secrets securely rather than embedding them in Docker images.

---

## 📝 Additional Notes

- The Jupyter notebooks are intended for experimentation, model development, and dataset preparation. They are not required to run the application.
- The exported fine-tuned model artifacts are maintained separately from the main Git repository.
- If a Groq API key is not configured, scoring can still work, but LLM-generated suggestions may be unavailable.

---

## 👩‍💻 Author

**Tanvi Sharma**

GitHub: [@tanvisharma5485](https://github.com/tanvisharma5485)

---

⭐ **If you find this project interesting, consider giving the repository a star!**