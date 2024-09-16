
# Code2Code Translator API

This is a simple Flask API named `code2code_translator` that leverages OpenAI's GPT-4 model to translate programming code from one language to another. The API is particularly useful for converting SQL queries into DataFrame operations or other equivalent programming constructs in different languages.

## Features

- **Language Translation**: Convert code snippets from one programming language to another using GPT-4.
- **SQL to DataFrame**: Specifically designed to translate SQL queries into DataFrame operations or other approaches in languages that support them.
- **Easy Integration**: Can be easily integrated into other systems or used as a standalone service.

## Requirements

- Python 3.7+
- Flask
- OpenAI Python Client Library
- Python Dotenv

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/code2code_translator.git
   cd code2code_translator
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   Create a `.env` file in the root directory of the project to store your OpenAI API key.

   ```plaintext
   OPENAI_API_KEY=your-openai-api-key
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

## Usage

Send a POST request to the `/translate` endpoint with a JSON body containing the code snippet and the target language.

Example request body:

```json
{
    "program": "SELECT * FROM orders WHERE order_date > '2023-01-01';",
    "language": "python"
}
```

## License

This project is licensed under the MIT License.
