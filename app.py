
import os
from flask import Flask, request, render_template, jsonify
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import base64

app = Flask(__name__)

# Konfigurasi Gemini API
import os
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# Konfigurasi keamanan
safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file:
            # Baca file gambar
            image_data = file.read()
            image_parts = [
                {
                    "mime_type": file.content_type,
                    "data": base64.b64encode(image_data).decode('utf-8')
                }
            ]
            
            prompt = "Berikan pujian dan motivasi positif dalam bahasa Indonesia yang santai dan lucu berdasarkan foto ini. Fokus pada aspek-aspek positif dan berikan dorongan yang membangun."
            
            # Generate konten
            response = model.generate_content(
                [prompt] + image_parts,
                safety_settings=safety_settings
            )
            
            return jsonify({'roast': response.text})
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
