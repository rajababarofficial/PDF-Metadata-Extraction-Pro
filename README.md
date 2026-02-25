# 📄 PDF-Metadata-Extraction-Pro

A streamlined, high-performance desktop application designed to extract deep metadata from multiple PDF files simultaneously. This tool automates the process of gathering document properties and organizes them into a structured CSV format.

## ✨ Core Features
- **Modern GUI:** Clean and intuitive interface built with `CustomTkinter`.
- **Smart Data Sequencing:** Automatically organizes data into a logical hierarchy:
    1. **Primary Info:** File Name, Title, Author, Page Count.
    2. **Custom Metadata:** Automatically detects and sorts unique user-defined fields.
    3. **System Properties:** File Size (MB), Producer, Creator, and Timestamps.
- **Batch Processing:** Handles entire directories of PDFs in seconds.
- **Excel-Ready Export:** Generates `UTF-8-SIG` encoded CSV files for perfect compatibility with Microsoft Excel and other data tools.

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- PyPDF2
- CustomTkinter

### Installation
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rajababarofficial/PDF-Metadata-Extraction-Pro.git](https://github.com/rajababarofficial/PDF-Metadata-Extraction-Pro.git)
   cd PDF-Metadata-Extraction-Pro

```

2. **Install dependencies:**
```bash
pip install customtkinter PyPDF2

```


3. **Run the script:**
```bash
python Script.py

```



## 🛠️ Usage

1. **Source Folder:** Click "Choose Source Folder" to select your PDF directory.
2. **Export Path:** (Optional) Define a custom filename and location.
3. **Process:** Click "RUN EXTRACTION" to generate your structured CSV report.

## ⚖️ License

This project is licensed under the MIT License.