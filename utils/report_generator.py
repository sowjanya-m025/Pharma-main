import os
import re
from xml.sax.saxutils import escape

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer


def _safe_filename(query, max_len=60):
    """Turn free text into a safe file name (no slashes, newlines or '?')."""
    name = re.sub(r"[^\w\-]+", "_", query.strip()).strip("_")
    return name[:max_len] or "report"


def create_pdf_report(query, text):
    os.makedirs("reports", exist_ok=True)
    file_path = f"reports/{_safe_filename(query)}_report.pdf"

    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()
    # Escape <, > and & so model output can never break ReportLab's mini-XML parser.
    story = [
        Paragraph(f"<b>Product Story for:</b> {escape(query)}", styles["Title"]),
        Spacer(1, 20),
    ]
    story.append(Paragraph(escape(text).replace("\n", "<br/>"), styles["Normal"]))
    doc.build(story)

    return file_path
