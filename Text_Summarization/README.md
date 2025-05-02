 # Text Summarization using NLP

This project implements an **Extractive Text Summarizer** using basic NLP techniques. It identifies the most informative sentences in a document by scoring them based on **word frequency**. The summarizer is lightweight, interpretable, and built entirely using Python and NLTK.

---

## Features

- Extractive summarization using word frequency
- Preprocessing: sentence and word tokenization, stopword removal
- Scoring and ranking sentences
- Clean, readable implementation
- Suitable for summarizing long articles or technical documents

---

## Project Structure
textSummarization.ipynb   # Main Jupyter Notebook
sample_text.txt           # (Optional) You can add articles here

---

## How It Works

1. **Text Cleaning**: Removes newline characters and lowercases the text.
2. **Tokenization**: Splits text into words and sentences.
3. **Frequency Calculation**: Counts word frequencies excluding stopwords.
4. **Sentence Scoring**: Each sentence is scored based on the sum of its word frequencies.
5. **Summary Extraction**: Top N highest scoring sentences are selected for the summary.

---

## Dependencies

- Python 3.x
- NLTK

---

## Install requirements:
```bash
pip install nltk

*Make sure to download NLTK corpora:*
import nltk
nltk.download('punkt')
nltk.download('stopwords')

---

### Future Work

Add abstractive summarization using models like BART or T5

Evaluate summaries using ROUGE, BLEU, or BERTScore

Apply the summarizer to domain-specific texts like DRDO news or defense reports

Convert notebook into a Streamlit app

---

## Author

Dwiti Thaker