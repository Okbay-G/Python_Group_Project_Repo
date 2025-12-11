# Tax Calculation Application – Zurich Tax Authority
 
## Project Overview
 
The Zurich Tax Authority requires a digital solution to improve the efficiency and accuracy of tax calculations for individual taxpayers. Manual tax processing based on salary data is time-consuming and susceptible to human error, especially when handling a large number of submissions.
 
This project implements a Python-based Tax Calculation Application that automates the tax calculation process. The application validates user input, calculates tax amounts based on predefined salary ranges, and generates an official PDF tax summary letter for each individual.
 
The application supports both manual console input and JSON-based input, allowing integration with existing systems that export taxpayer data as JSON files.
 
---
 
## Project Scope
 
### In Scope
 
* Console-based Python application
* Interactive selection between console input and JSON file input
* Input validation for personal and financial data
* Progressive tax calculation based on net salary
* Generation of a formal PDF tax letter
 
### Out of Scope
 
* Graphical user interface (GUI)
* Database or persistent data storage
 
---
 
## Features
 
### Input Handling
 
* Selection between:
 
  * Manual data entry via the console
  * Loading data from a JSON file
* Guided, interactive input flow
 
### Input Validation
 
* Mandatory field validation for:
 
  * First name
  * Last name
  * Sex
  * Address
  * Salary and deductions
* Validation rules include:
 
  * Numeric validation for salary-related fields
  * Character validation for names
  * Swiss address format validation
  * JSON file format and structure validation
 
### Tax Calculation
 
* Calculation of total deductions and net salary
* Progressive tax calculation based on predefined salary brackets
* Computation of tax percentage and final tax amount
 
### Output Generation
 
* Automatic generation of PDF tax letters
* Each PDF includes:
 
  * Tax authority address
  * Recipient name and address
  * Financial breakdown (gross salary, deductions, net salary)
  * Tax percentage and calculated tax amount
  * Formal letter text and closing
 
---
 
## Project Structure
 
```
.
├── Main.py
├── TaxCalculator.py
├── TaxPrinter.py
├── ConsoleInputProcessor.py
├── JsonInputProcessor.py
├── tax_data.json
└── README.md
```
 
### File Description
 
* Main.py
  Entry point of the application. Handles user interaction for selecting the input method.
 
* TaxCalculator.py
  Contains the tax calculation logic using a progressive tax model based on net salary.
 
* ConsoleInputProcessor.py
  Manages console-based user input, including validation and processing flow.
 
* JsonInputProcessor.py
  Handles reading, validating, and processing of JSON input files.
 
* TaxPrinter.py
  Responsible for generating the PDF tax letter using the ReportLab library.
 
* tax_data.json
  Example JSON input file containing taxpayer records.
 
---
 
## JSON Input Format
 
The JSON input file must contain a list of taxpayer records in the following format:
 
```
[
  {
    "first_name": "Max",
    "last_name": "Muster",
    "sex": "M",
    "address": "Bahnhofstrasse 12 8001 Zürich",
    "gross_salary": 75000,
    "social_deduction": 5000,
    "expenses": 2000
  }
]
```
 
---
 
## How to Run the Application
 
### Requirements
 
* Python 3.9 or higher
* Required Python package:
 
  * reportlab
 
Install dependencies using:
 
```
pip install reportlab
```
 
### Execution
 
Run the application from the project root directory:
 
```
python Main.py
```
 
Follow the on-screen instructions to:
 
1. Select the input method (JSON or CONSOLE)
2. Enter data manually or provide the JSON file path
3. Generate PDF tax summary letters
 
---
 
## Project Management and Work Distribution
 
This project was developed collaboratively by a team of three members:
 
* Roda
 
  * Application entry point (Main.py)
  * Tax calculation logic (TaxCalculator.py)
  * Initial structure of the PDF generation module
 
* Okbay
 
  * Input validation logic
  * JSON file handling and structure validation
  * Tax authority and recipient address sections of the PDF
 
* Pharusa
 
  * Console input processing logic
  * JSON record processing and workflow integration
  * PDF letter body, financial layout, and final implementation
 
Each team member contributed multiple commits representing incremental development and collaborative implementation.
 
---
 
## Conclusion
 
The Tax Calculation Application fulfills all defined project requirements by providing a reliable, validated, and automated solution for tax calculation and reporting. The modular architecture ensures maintainability and allows for future extensions, such as database integration or graphical user interfaces.