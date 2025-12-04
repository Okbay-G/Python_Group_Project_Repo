# Zurich Tax Calculator – Programming Project

> A console-driven Python application that validates taxpayer inputs, computes progressive tax from net salary, and generates formal PDF tax letters.

---

## Features

- **Input Modes**
    - **Console:** Guided prompts with strict validation (names, sex, Swiss address format, numeric fields)
    - **JSON:** Reads records from a JSON file exported by the Zurich Tax Authority GUI
- **Validation**
    - Mandatory fields: `first_name`, `last_name`, `sex`, `address`, `gross_salary`, `social_deduction`, `expenses`
    - Names: letters, spaces, apostrophes, hyphens only
    - Sex normalization: `male/female/m/f/man/woman`
    - Address (console): Swiss format `Street Number ZIP(4) City`
- **Tax Calculation**
    - `net_salary = gross_salary - (social_deduction + expenses)`
    - Progressive rates capped at 32%
- **PDF Output**
    - Formal letter with Zurich tax authority header, financial breakdown
    - Filename: `FirstName_LastName_<timestamp>_tax_report_letter.pdf`

---

## Requirements

- **Python:** 3.10+
- **Dependencies:** `reportlab`

---

## Quick Start

run Main.py

Choose `JSON` or `CONSOLE` mode when prompted.

---
## JSON Mode
- Provide a `.json` file containing an array of person records:
```json
{
  "first_name": "Jane",
  "last_name": "Doe",
  "sex": "F",
  "address": "Bahnhofstrasse 12, 8001 Zürich, Schweiz",
  "gross_salary": 3500,
  "social_deduction": 100,
  "expenses": 50
}
```

## Tax Rates

| Net Salary (CHF) | Rate |
|------------------|------|
| ≤ 24,000         | 0%   |
| 24,001–32,000    | 4%   |
| 40,001–48,000    | 8%   |
| 48,001–56,000    | 10%  |
| 56,001–64,000    | 12%  |
| 64,001–72,000    | 14%  |
| 72,001–80,000    | 16%  |
| 80,001–88,000    | 18%  |
| 88,001–96,000    | 20%  |
| 96,001–104,000   | 22%  |
| 104,001–112,000  | 24%  |
| 112,001–120,000  | 26%  |
| 120,001–128,000  | 28%  |
| 128,001–136,000  | 30%  |
| ≥ 136,001        | 32%  |

---

## Project Structure

```
tax-calculator/
├─ Main.py
├─ ConsoleInputProcessor.py
├─ JsonInputProcessor.py
├─ TaxCalculator.py
├─ TaxPrinter.py
├─ tax_data.json
└─ README.md
```

---

## Testing

```bash
pytest -q
```

**License:** Educational use only.

