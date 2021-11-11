import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
from classes import detect_object   

UPLOAD_FOLDER ='static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png','.jpeg'}

app = Flask(__name__, static_url_path="/static")

# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# limit upload size upto 3mb
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('error_404.html')
        file = request.files['file']
        if file.filename == '':
            return render_template('error_404.html')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            process_file(os.path.join(UPLOAD_FOLDER, filename), filename)
            data={
                "processed_img":'static/downloads/'+filename ,
                "uploaded_img":'static/uploads/'+filename
            }
            return render_template("index.html",data=data)   

    return render_template('index.html')

@app.route('/flush')
def flush():    
    return ""

def process_file(path, filename):
    img = detect_object(path, filename)
    cv2.imwrite(f"{DOWNLOAD_FOLDER}{filename}",img)


if __name__ == '__main__':
    app.run()
