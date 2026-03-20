# 📄 AI Resume Bullet & ATS Analyzer

An AI-powered web application that analyzes resume bullet points, scores their effectiveness, suggests improvements, and evaluates ATS (Applicant Tracking System) compatibility.

Built with **Streamlit + NLP + Gemini API**, this tool helps users transform weak resume bullets into strong, quantifiable, and ATS-optimized statements.

---

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

### 📄 PDF Upload & Download
- Upload resume in PDF format
- Download AI-improved resume bullets as a PDF

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

## 📂 Project Structure


resume-bullet-quantifier/
│
├── app.py # Main Streamlit app
├── analyzer.py # Bullet scoring logic
├── ai_rewriter.py # Gemini API integration
├── keyword_matcher.py # ATS keyword matching
├── pdf_parser.py # Extract text from PDF
├── resume_writer.py # Generate improved PDF
├── scorecard.py # Resume scoring system
├── utils.py # Bullet extraction helpers
├── .env # API key (not committed)
└── requirements.txt



---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https:https://github.com/Saifza/resume-bullet-quantifier.git
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

*Integrating LLM APIs into real applications

*Prompt engineering for structured outputs

*Building end-to-end NLP pipelines

*Designing user-friendly data apps with Streamlit

*Handling PDF parsing and generation in Python


🔮 Future Improvements

*Resume section detection (Education, Experience, Skills)

*Role-specific optimization (e.g., Data Analyst, SWE)

*Grammar and readability scoring

*Multi-page resume restructuring

*Deployment (Streamlit Cloud / Docker)


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

