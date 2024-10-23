from flask import Flask, render_template, request, jsonify
import os
import zipfile

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
LOCKED_FOLDER = 'locked'
UNPACKED_FOLDER = 'unpacked'

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(LOCKED_FOLDER, exist_ok=True)
os.makedirs(UNPACKED_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOCKED_FOLDER'] = LOCKED_FOLDER
app.config['UNPACKED_FOLDER'] = UNPACKED_FOLDER

# Route for homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for uploading and locking the file
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Lock the file (compress it in this case)
    locked_filepath = os.path.join(app.config['LOCKED_FOLDER'], f"{file.filename}.zip")
    with zipfile.ZipFile(locked_filepath, 'w') as zipf:
        zipf.write(filepath, os.path.basename(filepath))
    
    return jsonify({'message': 'File uploaded and locked successfully', 'locked_file': locked_filepath}), 200

# Route for unlocking the file
@app.route('/unlock', methods=['POST'])
def unlock_file():
    data = request.json
    locked_filename = data.get('locked_file', '')  # Get the locked file name from request
    
    # Construct the full path for the locked file
    locked_file_path = os.path.join(app.config['LOCKED_FOLDER'], locked_filename)

    try:
        # Ensure the path exists
        if not os.path.exists(locked_file_path):
            return jsonify({'error': 'File not found'}), 404

        # Unzip the file
        with zipfile.ZipFile(locked_file_path, 'r') as zip_ref:
            extracted_path = app.config['UNPACKED_FOLDER']
            zip_ref.extractall(extracted_path)

        # List extracted files and their content
        extracted_files = os.listdir(extracted_path)
        extracted_content = {}
        for file_name in extracted_files:
            with open(os.path.join(extracted_path, file_name), 'rb') as f:
                extracted_content[file_name] = f.read().decode('utf-8', errors='ignore')  # Decode for display

        return jsonify({
            'message': 'File unlocked successfully',
            'extracted_content': extracted_content
        })
    except Exception as e:
        # Log the error for debugging
        print(f"Error unlocking file: {e}")
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)
