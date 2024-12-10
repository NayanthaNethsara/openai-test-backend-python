from flask import Flask, request, jsonify, send_file
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
import os

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Multimodal Backend!"})


# Text to Image Conversion
@app.route('/text-to-image', methods=['POST'])
def text_to_image():
    data = request.json
    text = data.get('text', 'Hello World!')
    img = Image.new('RGB', (500, 300), color=(73, 109, 137))
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    draw.text((50, 150), text, fill="white", font=font)
    img_path = "output.png"
    img.save(img_path)
    return send_file(img_path, mimetype='image/png')


# Text to Speech Conversion
@app.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    data = request.json
    text = data.get('text', 'Hello World!')
    tts = gTTS(text)
    audio_path = "output.mp3"
    tts.save(audio_path)
    return send_file(audio_path, mimetype='audio/mpeg')


# Image Captioning
@app.route('/image-captioning', methods=['POST'])
def image_captioning():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    image = request.files['image']
    image.save("uploaded_image.png")
    caption = "This is a beautiful image!"
    return jsonify({"caption": caption})


if __name__ == '__main__':
    # Clean up previous output files
    if os.path.exists("output.png"):
        os.remove("output.png")
    if os.path.exists("output.mp3"):
        os.remove("output.mp3")
    if os.path.exists("uploaded_image.png"):
        os.remove("uploaded_image.png")

    app.run(debug=True)
