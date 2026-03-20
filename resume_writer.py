# resume_writer.py

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch


def create_resume_pdf(improved_bullets, filename="improved_resume.pdf"):

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("Improved Resume Bullets", styles["Title"]))
    story.append(Spacer(1, 20))

    for bullet in improved_bullets:

        bullet_text = "• " + bullet.strip()
        story.append(Paragraph(bullet_text, styles["Normal"]))
        story.append(Spacer(1, 10))

    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )

    doc.build(story)

    return filename