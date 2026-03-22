# app.py

import streamlit as st
from utils import extract_bullets
from analyzer import analyze_bullet
from ai_rewriter import rewrite_bullet_ai
from keyword_matcher import calculate_match_score
from pdf_parser import extract_text_from_pdf
from resume_writer import create_resume_pdf
from scorecard import generate_scorecard

import os

st.set_page_config(
    page_title="Resume Bullet Quantifier",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Bullet & ATS Analyzer")

st.write(
    "Upload a resume or paste bullets to analyze strength, generate AI improvements, "
    "compare against a job description, and download improved bullets."
)

# -------------------------
# INPUT
# -------------------------

resume_input = st.text_area(
    "Paste resume bullets (optional)",
    height=150,
)

uploaded_file = st.file_uploader(
    "Or upload resume (PDF)",
    type=["pdf"]
)

job_description = st.text_area(
    "Paste Job Description (optional)",
    height=150
)

analyze_button = st.button("Analyze Resume")

# -------------------------
# ANALYSIS
# -------------------------

if analyze_button:

    resume_text = ""

    if uploaded_file:
        resume_text = extract_text_from_pdf(uploaded_file)

    elif resume_input:
        resume_text = resume_input

    else:
        st.error("Please paste bullets or upload a resume.")
        st.stop()

    bullets = extract_bullets(resume_text)

    if not bullets:
        st.error("No bullet points detected.")
        st.stop()

    # limit bullets to prevent huge output
    bullets = bullets[:15]

    scores = []
    results_list = []
    improved_bullets = []

    st.subheader("Bullet Analysis")

    for bullet in bullets:

        result = analyze_bullet(bullet)
        results_list.append(result)

        score = result["score"]
        scores.append(score)

        st.markdown("---")
        st.markdown("### Original Bullet")
        st.write(bullet)

        if score >= 80:
            st.success(f"Strong Bullet: {score}/100")
        elif score >= 60:
            st.warning(f"Decent Bullet: {score}/100")
        else:
            st.error(f"Weak Bullet: {score}/100")

        st.progress(score / 100)

        with st.spinner("Generating AI suggestions..."):
            suggestions = rewrite_bullet_ai(bullet)

        st.markdown("### ✨ Improved Versions")

        for s in suggestions:
            st.success(s)

        # save first suggestion for PDF
        if suggestions:
            improved_bullets.append(suggestions[0])

    # -------------------------
    # SUMMARY
    # -------------------------

    avg_score = sum(scores) / len(scores)

    st.markdown("---")
    st.subheader("Resume Summary")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Average Bullet Score", round(avg_score, 1))

    with col2:
        st.metric("Total Bullets", len(bullets))

    # -------------------------
    # ATS MATCH
    # -------------------------

    match_score = None  # important default

    if job_description:

        st.markdown("---")
        st.subheader("ATS Keyword Match")

        match_score, matched, missing = calculate_match_score(
            resume_text,
            job_description
        )

        st.metric("ATS Match Score", f"{match_score}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("✅ Matched Keywords")
            for word in matched[:10]:
                st.write("-", word)

        with col2:
            st.write("❌ Missing Keywords")
            for word in missing[:10]:
                st.write("-", word)

    # -------------------------
    # RESUME SCORECARD
    # -------------------------

    st.markdown("---")
    st.subheader("📊 Resume Scorecard")

    scorecard = generate_scorecard(
        results_list,
        bullets,
        match_score
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Final Resume Score", scorecard["final_score"])

    with col2:
        st.metric("Avg Bullet Score", scorecard["avg_score"])

    with col3:
        st.metric("Bullets Without Metrics", scorecard["no_metrics"])

    col4, col5 = st.columns(2)

    with col4:
        st.metric("Weak Verbs", scorecard["weak_verbs"])

    with col5:
        st.metric("Generic Phrases", scorecard["generic_phrases"])

    # feedback message
    if scorecard["final_score"] >= 80:
        st.success("Excellent Resume 🚀")
    elif scorecard["final_score"] >= 60:
        st.warning("Good Resume — room for improvement")
    else:
        st.error("Needs Improvement")

    # -------------------------
    # DOWNLOAD IMPROVED RESUME
    # -------------------------

    st.markdown("---")
    st.subheader("Download Improved Resume")

   # pdf_file = create_resume_pdf(improved_bullets)

   # with open(pdf_file, "rb") as file:
   #     st.download_button(
   #         label="Download Improved Resume",
   #         data=file,
   #         file_name="improved_resume.pdf",
   #         mime="application/pdf"
   #     )

# -------------------------
# SIDEBAR
# -------------------------

with st.sidebar:

    st.header("About")

    st.write(
        "AI-powered resume bullet analyzer that scores resume bullets, "
        "suggests improvements, and compares resumes against job descriptions."
    )

    st.write("---")

    st.write("Built with:")
    st.write("• Python")
    st.write("• Streamlit")
    st.write("• Gemini API")