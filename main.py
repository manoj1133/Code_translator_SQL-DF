import os
from openai import OpenAI
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_key)
app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    program = data.get('program')
    language = data.get("language")

    if not program:
        return jsonify({'error': 'No program provided'}), 400

    prompt = f"""Discover the following programming language into the {language}. If the request it to translate sql to any language, then don't use the sql queries in the programming language. Use DataFrame operations if available or any other approaches.

Program:
```
{program}
```"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=5000,  # Adjust based on the expected length of the output
            temperature=0.3
        )

        full_response = response.choices[0].message.content.strip()

        # Split the response into the code block and the explanation
        if "```python" in full_response and "```" in full_response:
            start = full_response.index("```python")
            end = full_response.index("```", start + 1)
            pyspark_code = full_response[start + len("```python"):end].strip()
            explanation = full_response[end + len("```"):].strip()
        else:
            pyspark_code = full_response
            explanation = ""

        # Format the PySpark code as a code block
        pyspark_code_block = f"```python\n{pyspark_code}\n```"

        return jsonify({
            'pyspark_code': pyspark_code_block,
            'explanation': explanation
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
