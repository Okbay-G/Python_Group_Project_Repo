import time
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from typing import List


def format_timestamped_filename(first_name: str, last_name: str, suffix: str = "tax_report_letter.pdf") -> str:
    """
    Build a unique filename using first name, last name and current timestamp.
    Returns: string filename like "First_Last_165..._tax_report_letter.pdf"
    """
    timestamp = int(time.time() * 1000)
    return f"{first_name}_{last_name}_{timestamp}_{suffix}"


def draw_tax_authority_block(c: canvas.Canvas, width: float, height: float, lines: List[str],
                             right_margin: float = 72, top_offset: float = 60, line_height: float = 15) -> None:
    """
    Draw the tax authority address block at the top-right of the page (German format).
    c: reportlab canvas
    width,height: page dimensions
    lines: list of address lines to print right-aligned
    """
    authority_y = height - top_offset
    # Use a readable font/size for the authority block
    c.setFont("Helvetica", 10)
    for line in lines:
        c.drawRightString(width - right_margin, authority_y, line)
        authority_y -= line_height


def draw_recipient_address(c: canvas.Canvas, first_name: str, last_name: str, address: str,
                           width: float, height: float,
                           left_margin: float = 72, top_offset: float = 100, line_height: float = 15) -> float:
    """
    Draw the recipient name and multi-line address at the top-left.
    Returns the current Y coordinate after drawing the address (to continue drawing below).
    """
    c.setFont("Helvetica", 12)
    text_y = height - top_offset
    c.drawString(left_margin, text_y, f"{first_name} {last_name}")
    text_y -= line_height
    for line in address.split("\n"):
        c.drawString(left_margin, text_y, line)
        text_y -= line_height
    return text_y


def draw_body_and_financials(c: canvas.Canvas, text_y_start: float,
                             sex: str, last_name: str,
                             gross_income: float, deductible: float, net_salary: float,
                             tax_percentage: float, tax_amount: float,
                             left_margin: float = 72) -> None:
    """
    Draw greeting, body text, financial breakdown and closing on the canvas.
    text_y_start: starting y coordinate (below the address block).
    """
    text_y = text_y_start - 30
    greeting = f"Dear Mr. {last_name}" if sex == 'M' else f"Dear Ms. {last_name}"
    c.setFont("Helvetica", 12)
    c.drawString(left_margin, text_y, greeting)

    text_y -= 30
    c.drawString(left_margin, text_y, "We are writing to inform you that your tax has been calculated as follows:")

    text_y -= 30
    # Financials aligned a bit to the right
    c.drawString(100, text_y, f"Gross Income:       CHF {gross_income:,.2f}")
    text_y -= 20
    c.drawString(100, text_y, f"Deductible:         CHF {deductible:,.2f}")
    text_y -= 20
    c.drawString(100, text_y, f"Net Salary:         CHF {net_salary:,.2f}")
    text_y -= 20
    c.drawString(100, text_y, f"Tax Percentage:     {tax_percentage:.2f}%")
    text_y -= 20
    c.drawString(100, text_y, f"Tax to be Paid:     CHF {tax_amount:,.2f}")

    # Closing
    text_y -= 50
    c.drawString(left_margin, text_y, "If you have any questions regarding this calculation, please do not hesitate to contact us.")
    text_y -= 20
    c.drawString(left_margin, text_y, "Best Regards,")
    text_y -= 20
    c.drawString(left_margin, text_y, "Tax Authorities of canton Zurich")


def create_tax_letter(first_name: str, last_name: str, sex: str, address: str,
                      gross_income: float, deductible: float, net_salary: float,
                      tax_percentage: float, tax_amount: float) -> str:
    """
    Create a PDF tax letter for a person. Returns the created filename.
    Behavior preserved from the original implementation:
      - draws Zurich tax authority address (top-right),
      - recipient address (top-left),
      - greeting based on sex ('M' -> Mr., otherwise -> Ms.),
      - financial breakdown and closing,
      - saves PDF and prints confirmation.
    """
    # Tax Authority Address Block (Hardcoded Zurich)
    tax_authority_lines = [
        "Steueramt Zürich",
        "Bändliweg 21",
        "Postfach",
        "8090 Zürich"
    ]

    # Page setup
    width, height = letter

    # Create canvas and filename
    file_name = format_timestamped_filename(first_name, last_name)
    c = canvas.Canvas(file_name, pagesize=letter)

    # Draw blocks
    draw_tax_authority_block(c, width, height, tax_authority_lines)
    address_bottom_y = draw_recipient_address(c, first_name, last_name, address, width, height)
    draw_body_and_financials(c, address_bottom_y, sex, last_name,
                             gross_income, deductible, net_salary, tax_percentage, tax_amount)

    # Save PDF
    c.save()
    print(f"PDF '{file_name}' created successfully!")
    return file_name
