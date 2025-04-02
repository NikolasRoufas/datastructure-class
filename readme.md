# How to Run the Script

## Prerequisites
- Python 3.6 or higher installed on your system
- pip package manager

## Setup Instructions

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv env
   ```

2. **Activate the virtual environment**:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run your script**:
   ```bash
   python your_script_name.py
   ```

## Notes
- The only external dependency is matplotlib. The other imports (`time`, `random`, `copy`, `string`, `os`, `json`) are part of Python's standard library.
- Make sure your script has the proper file extension `.py` and includes the necessary functions and code execution statements.
- If your script generates matplotlib plots, they will either be displayed in a pop-up window or saved to a file depending on your code.