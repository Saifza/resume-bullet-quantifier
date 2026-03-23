# 📄 AI Resume Bullet & ATS Analyzer

An AI-powered web application that analyzes resume bullet points, scores their effectiveness, suggests improvements, and evaluates ATS (Applicant Tracking System) compatibility.

Built with **Streamlit + NLP + Gemini API**, this tool helps users transform weak resume bullets into strong, quantifiable, and ATS-optimized statements.

---

## 🚀 Live Demo
-🔗 [Open Live App](https://resume-bullet-quantifier-dclyn4upucat4jvbv66vpr.streamlit.app/)

## ⚠️ Deployment Notes

- PDF export feature is currently disabled in the live app due to environment limitations with image/PDF dependencies.
- Full functionality is available when running locally.


## 📸 Screenshots
 -screenshots/input.png
 -screenshots/analysis.png
 -screenshots/scorecard.png

## 🚀 Features

### 🔍 Resume Analysis
- Extracts bullet points from pasted text or uploaded PDF resumes
- Scores each bullet (0–100) based on:
  - Action verbs
  - Clarity
  - Impact
  - Quantification

### ✨ AI Bullet Rewriting
- Uses **Google Gemini API** to generate:
  - Stronger action verbs
  - Quantified achievements
  - ATS-friendly phrasing
- Produces **3 improved versions per bullet**

### 📊 Resume Scorecard
- Final Resume Score
- Average Bullet Score
- Weak Verb Detection
- Generic Phrase Detection
- Missing Quantification Analysis

### 🧠 ATS Keyword Matching
- Compares resume against a job description
- Outputs:
  - Match Score (%)
  - Matched Keywords
  - Missing Keywords

### 📄 PDF Upload
- Upload resume in PDF format


---

## 🔥 Why This Project Stands Out

Unlike basic resume tools, this project goes beyond simple text analysis by combining **rule-based NLP + AI-powered rewriting + ATS optimization** into a single workflow.

### 💡 What makes it unique:
- **Hybrid Approach:** Combines deterministic scoring (action verbs, quantification) with LLM-generated improvements
- **Real-World Relevance:** Directly targets ATS systems used in modern hiring pipelines
- **Actionable Feedback:** Not just scores — provides **improved bullet rewrites**
- **End-to-End System:** From input → analysis → AI enhancement → scoring → keyword matching
- **Deployed Application:** Fully accessible via live web app (not just a local script)

### 🧠 Engineering Highlights:
- Modular architecture (separate analyzers, AI layer, scoring system)
- Clean separation of concerns (NLP logic vs AI vs UI)
- Environment-aware deployment (handling dependency constraints like PDF processing)

This project demonstrates the ability to build **practical AI applications**, not just experiments.

---

## 🖼️ Demo

> *(Add screenshots here after running the app)*

Example sections:
- Bullet Analysis
- AI Suggestions
- ATS Match Score
- Resume Scorecard

---

## 🛠️ Tech Stack

- **Frontend/UI:** Streamlit  
- **Backend Logic:** Python  
- **AI Integration:** Google Gemini API  
- **PDF Processing:** PyPDF / ReportLab  
- **NLP Techniques:** Rule-based scoring + keyword extraction  

---


## 📂 Project Structure


resume-bullet-quantifier/
│
├── app.py # Main Streamlit app
├── analyzer.py # Bullet scoring logic
├── ai_rewriter.py # Gemini API integration
├── keyword_matcher.py # ATS keyword matching
├── pdf_parser.py # Extract text from PDF
├── resume_writer.py # (Optional) PDF generation module (currently disabled in deployment)
├── scorecard.py # Resume scoring system
├── utils.py # Bullet extraction helpers
├── .env # API key (not committed)
└── requirements.txt



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Saifza/resume-bullet-quantifier.git
cd resume-bullet-quantifier

2. Create Virtual Environment

python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Mac/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Add API Key
Create a .env file:

GOOGLE_API_KEY=your_api_key_here

5. Run the App

streamlit run app.py

📊 Example Output

Before:
Responsible for improving system performance

After:
Optimized system performance, reducing response time by 35% and improving user experience across 10K+ daily requests

🎯 Key Learnings

-Integrating LLM APIs into real applications

-Prompt engineering for structured outputs

-Building end-to-end NLP pipelines

-Designing user-friendly data apps with Streamlit

-Handling PDF parsing and generation in Python


🔮 Future Improvements

*Resume section detection (Education, Experience, Skills)

*Role-specific optimization (e.g., Data Analyst, SWE)

*Grammar and readability scoring

*Multi-page resume restructuring

*Deployment (Streamlit Cloud / Docker)

- 📥 Export AI-improved resume bullets as a PDF *(Feature temporarily disabled in live demo)*

🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.


📜 License

This project is open-source and available under the MIT License.


⭐ Acknowledgements

Google Gemini API for AI text generation

Streamlit for rapid UI development


💡 Author

Saif Zaman

If you found this project useful, consider giving it a ⭐ on GitHub!

