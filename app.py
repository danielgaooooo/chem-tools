from flask import Flask, request, render_template
from calculate import main

app = Flask(__name__)

@app.route('/')
def upload_form():
    return '''
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file uploaded", 400
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file", 400

    # Process file here (e.g., save or analyze)
    content = file.read().decode('utf-8')  # Example: Read as text
    return f"File received! Content:\n{content}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)