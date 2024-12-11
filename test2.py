import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=api_key)


@app.route('/generate-response', methods=['POST'])
def generate_response():
    data = request.json
    user_prompt = data.get("prompt")

    # Generate text response
    text_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": user_prompt
            }
        ]
    ).choices[0].text.strip()

    # Generate image response
    response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_response = response.data[0].url

    return jsonify({
        "text": text_response,
        "image": image_response
    })


if __name__ == '__main__':
    app.run(debug=True)
