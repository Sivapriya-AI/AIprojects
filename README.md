
CSV Analyzer with Streamlit UI

A lightweight web-based tool built with Python and Streamlit that allows you to upload any CSV file, automatically detect date/time columns, clean anomalies, and preview cleaned data.

🚀 Features

Upload any CSV file via a browser interface.

Automatic detection of datetime columns using Pandas type inference.

Convert date-like columns to datetime64[ns] format.

Preserve missing datetime values as NaT.

Remove duplicate rows with a single click.

Data preview (first few rows).

Download cleaned data as CSV.

🛠️ Tech Stack

Python 3.8+

Streamlit – Web UI

Pandas – Data processing

📦 Installation

Clone the repository

git clone https://github.com/yourusername/csv-analyzer.git
cd csv-analyzer


Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows


Install dependencies

pip install -r requirements.txt

📜 Usage

Run the Streamlit app:

streamlit run app.py


Open your browser and go to:

http://localhost:8501

🖥️ How It Works

Upload a CSV file using the UI.

The app reads the CSV with Pandas.

Tries to parse object columns as dates.

Cleans the dataset:

Drops duplicate rows.

Keeps missing dates as NaT.

Displays cleaned data in an interactive table.

Option to download the cleaned CSV.


CSV Analyzer with Streamlit UI
<img width="1919" height="735" alt="image" src="https://github.com/user-attachments/assets/61437bc2-e557-444f-9a22-a0f07cd3903d" />
