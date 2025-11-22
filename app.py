import os
from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from pypdf import PdfWriter
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# Configure upload and merged folders
UPLOAD_FOLDER = 'uploads'
MERGED_FOLDER = 'merged'
ALLOWED_EXTENSIONS = {'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MERGED_FOLDER'] = MERGED_FOLDER

# Ensure directories exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(MERGED_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/merge', methods=['POST'])
def merge_pdfs():
    if 'file1' not in request.files or 'file2' not in request.files:
        flash('No file part')
        return redirect(request.url)
    
    file1 = request.files['file1']
    file2 = request.files['file2']
    output_filename = request.form.get('filename', 'merged')
    
    if file1.filename == '' or file2.filename == '':
        flash('No selected file')
        return redirect(request.url)
    
    if file1 and allowed_file(file1.filename) and file2 and allowed_file(file2.filename):
        filename1 = secure_filename(file1.filename)
        filename2 = secure_filename(file2.filename)
        
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], filename1)
        path2 = os.path.join(app.config['UPLOAD_FOLDER'], filename2)
        
        file1.save(path1)
        file2.save(path2)
        
        merger = PdfWriter()
        merger.append(path1)
        merger.append(path2)
        
        if not output_filename.endswith('.pdf'):
            output_filename += '.pdf'
            
        output_path = os.path.join(app.config['MERGED_FOLDER'], secure_filename(output_filename))
        merger.write(output_path)
        merger.close()
        
        return send_file(output_path, as_attachment=True)
    else:
        flash('Invalid file type. Please upload PDF files only.')
        return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)
