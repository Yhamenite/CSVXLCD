# 🧹 Batch CSV Column Remover

A Python automation tool designed to efficiently remove specific columns from multiple CSV files simultaneously. It utilizes a user-friendly terminal interface with color-coded prompts to guide you through selecting deletion ranges using standard Excel column letters (e.g., A, Z, AA).

> **Note:** This tool processes data safely by creating a separate output directory, ensuring your original files remain untouched.

## 📑 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [How to Use](#-how-to-use)
  - [Input Syntax](#-input-syntax)
- [Directory Structure](#-directory-structure)
- [Troubleshooting](#-troubleshooting)

## 🚀 Features

* **Batch Processing:** transform an entire directory of CSV files in seconds.
* **Excel-Style Indexing:** Define columns using letters (`A`, `B`, `AA`) rather than confusing zero-based numerical indices.
* **Safe Execution:** Automatically generates a specific output folder (`03-deleted_unwanted_features`) for cleaned files.
* **Interactive CLI:** Features a colored command-line interface (Blue for info, Green for success, Red for errors, Yellow for warnings).
* **Smart Validation:** Checks for valid range pairs and existing directories to prevent errors.

## 📋 Prerequisites

To run this tool, ensure you have **Python 3.x** installed. The script relies on the following external libraries:

* `pandas` (for data manipulation)
* `numpy` (for numerical operations)

## ⚙️ Installation

1.  **Clone this repository** (or download the script):
    ```bash
    git clone https://github.com/Yhamenite/CSVXLCD.git
    ```

2.  **Install the required dependencies** using pip:
    ```bash
    pip install pandas numpy
    ```

## 🛠️ How to Use

1.  **Run the script** from your terminal:
    ```bash
    python main.py
    ```

2.  **Provide Input Directory:**
    The script will ask: `[*] Please provide the input directory:`
    * Paste the path to the folder containing your raw CSV files.

3.  **Define Deletion Ranges:**
    The script will ask: `Deletion ranges:`
    * Enter your column ranges separated by commas.
    * **Crucial:** You must provide pairs of Start and End columns.

### 📝 Input Syntax

The tool accepts ranges in the format: `Start,End,Start,End`.

**Example:**
If you enter: `A,C,F,H`

* **Range 1:** Deletes columns from **A to C** (inclusive).
* **Range 2:** Deletes columns from **F to H** (inclusive).

## 📂 Directory Structure

The tool keeps your workspace organized. When you run the script, it creates a dedicated output folder.

```text
Your_Project_Root/
│
├── main.py                     # This script
├── input_data_folder/          # Your source folder
│   ├── data_file_01.csv
│   └── data_file_02.csv
│
└── 03-deleted_unwanted_features/   # 🟢 Output folder (Created Automatically)
    ├── data_file_01.csv            # Cleaned file
    └── data_file_02.csv            # Cleaned file
