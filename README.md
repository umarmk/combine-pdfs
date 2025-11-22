# PDF Combiner

A simple Flask web application to combine two PDF files into one.

## Prerequisites

- Python 3.x

## Installation

1.  Clone the repository or download the source code.
2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```
3.  Activate the virtual environment:
    - Windows: `.\venv\Scripts\activate`
    - macOS/Linux: `source venv/bin/activate`
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Ensure your virtual environment is activated.
2.  Run the Flask app:
    ```bash
    python app.py
    ```
3.  Open your browser and navigate to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## Usage

1.  Upload the first PDF file.
2.  Upload the second PDF file.
3.  (Optional) Enter a name for the merged file.
4.  Click "Combine PDFs" to download the result.
