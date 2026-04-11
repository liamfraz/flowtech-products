"""Generate a 1280x720 cover image for Gumroad."""
from reportlab.lib.pagesizes import landscape
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import subprocess, os

OUT_PDF = "/Users/liamfrazer/Documents/flowtech/products/hr-automation-pack/cover.pdf"
OUT_PNG = "/Users/liamfrazer/Documents/flowtech/products/hr-automation-pack/cover.png"

W, H = 320*mm, 180*mm   # approx 1280x720 at 100dpi

NAVY  = colors.HexColor("#1B2A4A")
TEAL  = colors.HexColor("#00A3A3")
WHITE = colors.white
LIGHT = colors.HexColor("#F4F7FA")
GREY  = colors.HexColor("#B0C4DE")

c = canvas.Canvas(OUT_PDF, pagesize=(W, H))

# Background
c.setFillColor(NAVY)
c.rect(0, 0, W, H, fill=1, stroke=0)

# Teal accent bar left
c.setFillColor(TEAL)
c.rect(0, 0, 8*mm, H, fill=1, stroke=0)

# Top label
c.setFillColor(TEAL)
c.setFont("Helvetica-Bold", 11)
c.drawString(18*mm, H - 22*mm, "FLOWTECH ADVISORY")

# Main title
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 36)
c.drawString(18*mm, H - 52*mm, "Power Automate")
c.drawString(18*mm, H - 70*mm, "HR Automation Pack")

# Subtitle
c.setFillColor(GREY)
c.setFont("Helvetica", 16)
c.drawString(18*mm, H - 88*mm, "5 Ready-to-Use M365 Flow Templates")

# Divider
c.setStrokeColor(TEAL)
c.setLineWidth(1.5)
c.line(18*mm, H - 96*mm, 160*mm, H - 96*mm)

# Flow list
flows = [
    "01  New Employee Onboarding",
    "02  Leave Request Approval",
    "03  Monthly Timesheet Reminder",
    "04  Performance Review Reminders",
    "05  Offboarding Checklist",
]
c.setFont("Helvetica", 12)
for i, f in enumerate(flows):
    y = H - 108*mm - i * 10*mm
    c.setFillColor(TEAL)
    c.rect(18*mm, y - 1*mm, 2*mm, 7*mm, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.drawString(24*mm, y, f)

# Price badge
c.setFillColor(TEAL)
c.roundRect(W - 70*mm, H/2 - 18*mm, 55*mm, 36*mm, 4*mm, fill=1, stroke=0)
c.setFillColor(NAVY)
c.setFont("Helvetica-Bold", 11)
c.drawCentredString(W - 42.5*mm, H/2 + 10*mm, "GET IT FOR")
c.setFillColor(WHITE)
c.setFont("Helvetica-Bold", 32)
c.drawCentredString(W - 42.5*mm, H/2 - 8*mm, "$49")

# Bottom watermark
c.setFillColor(GREY)
c.setFont("Helvetica", 9)
c.drawString(18*mm, 8*mm, "flowtech.com.au  |  Power Automate  |  Microsoft 365  |  SharePoint  |  Teams")

c.save()
print("PDF cover saved:", OUT_PDF)

# Convert PDF → PNG using sips (macOS built-in)
try:
    subprocess.run(
        ["sips", "-s", "format", "png", "-z", "720", "1280", OUT_PDF, "--out", OUT_PNG],
        check=True
    )
    print("PNG cover saved:", OUT_PNG)
except Exception as e:
    # Fallback: try ImageMagick
    try:
        subprocess.run(["convert", "-density", "150", OUT_PDF, "-resize", "1280x720", OUT_PNG], check=True)
        print("PNG cover saved (ImageMagick):", OUT_PNG)
    except Exception:
        print("Cover PDF created. Convert manually:", OUT_PDF)
