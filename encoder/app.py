from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Function to encode text (Caesar cipher for simplicity)
def encode_text(text):
    shift = 3
    encoded = ''.join([chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() 
                       else chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() 
                       else char for char in text])
    return encoded

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encode', methods=['POST'])
def encode():
    data = request.json
    text = data.get('text', '')
    encoded = encode_text(text)
    return jsonify({
        'received_text': text,
        'encoded_text': encoded
    })

if __name__ == '__main__':
    app.run(debug=True)
