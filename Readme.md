# CSV Smart CLI

A simple command-line utility written in Python that analyzes CSV files
and generates text reports.

## 🚀 Features

- Read CSV files with headers
- Generate summary or full reports
- Automatically creates output directories
- Simple and clear CLI interface

## 📦 Project Structure

Project_3/
├── app.py
├── src/
│ ├── init.py
│ ├── loader.py
│ └── report.py
├── data/
│ └── sample.csv
├── outputs/
│ └── report.txt
└── README.md


## ⚙️ Requirements

- Python 3.9+

No external libraries are required.

## ▶️ Usage

### Summary report (default)

```bash
python app.py --input data/sample.csv

Full report
python app.py --input data/sample.csv --format full

Custom output file
python app.py --input data/sample.csv --format full --output outputs/full_report.txt

Output Example
CSV REPORT
==========
Rows count: 3
Columns: name, score

What this project demonstrates

Building CLI tools with argparse

Clean project structure

Separation of logic and interface

Working with real files and directories

Production-oriented Python code

📌 Notes

This project is intended as a portfolio example demonstrating
command-line application design and clean Python architecture.