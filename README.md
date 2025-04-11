# TokenFlow->Tokenization-and-Frequency

# TokenTally - Simple Text Tokenizer and Frequency Analyzer

This project is a basic text tokenizer and frequency analyzer implemented in Python, with a Flask web application interface. It provides functionality to upload a text file, tokenize it, and display the tokenized output along with the frequency of each token.

## Features

* **File Upload:** Allows users to upload text files (.txt, .md).
* **Tokenization:** Tokenizes the input text into words, punctuation, and whitespace.
* **NLP Preprocessing:** Includes lowercasing, stop word removal, and basic stemming.
* **Frequency Analysis:** Calculates the frequency of each token.
* **Flask Web App:** Provides a simple web interface for easy use.

## Usage

1.  **Installation:**
    * Ensure you have Python installed.
    * Install Flask: `pip install Flask`
2.  **Running the Application:**
    * Place `tokeniser.py` and `app.py` in the same directory.
    * Run `app.py`: `python app.py`
    * Open your web browser and navigate to `http://127.0.0.1:5000/`.
3.  **Using the Web App:**
    * Upload a text file using the provided form.
    * The tokenized output and token frequencies will be displayed on the results page.

## Important Notes

* **Lossy Tokenization:** The tokenization process includes lossy operations like lowercasing, stop word removal, and stemming. The original text cannot be perfectly reconstructed from the tokenized output.
* **Customization:** The `stop_words` list in `app.py` can be modified to customize stop word removal.
* **Basic Stemming:** The stemming algorithm is very basic. For more accurate stemming, consider using dedicated libraries like NLTK or SpaCy.
* **File Handling:** The uploaded file is saved temporarily and then deleted after processing.
