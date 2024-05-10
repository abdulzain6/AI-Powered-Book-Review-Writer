# AI Powered Book Review Writer

The AI Powered Book Review Writer is a Streamlit application that automates the process of writing book reviews. By uploading a document, the application uses OpenAI's powerful language models to generate insightful and articulate book reviews, which are then formatted and returned as DOCX files.

## Features

- **Document Upload**: Users can upload a book in text format.
- **AI-Generated Reviews**: Utilizes OpenAI to analyze the content and produce a comprehensive review.
- **DOCX Output**: The review is automatically formatted into a DOCX file for easy downloading and sharing.

## Prerequisites

- Python 3.10 or higher
- Streamlit
- OpenAI API Key

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/abdulzain6/AI-Powered-Book-Review-Writer.git
cd AI-Powered-Book-Review-Writer
```

2. **Install the required Python packages:**

```bash
pip install -r requirements.txt
```

## Configuration

Set the `OPENAI_API_KEY` in your environment to interact with OpenAI models:

```bash
export OPENAI_API_KEY='your_openai_api_key_here'
```

## Usage

To run the application:

```bash
streamlit run webapp.py
```

Navigate to `http://localhost:8501` in your web browser to start using the app. Upload your book document and receive a professionally written review in moments.

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.
```
