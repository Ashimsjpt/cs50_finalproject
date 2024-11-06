from flask import Flask, request, send_file
import cv2
import numpy as np
import os

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

#upload
def index():
    return render_template('index.html') 

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    z_height = request.form.get('z_height', '5')  #defult size of z height 5mm

    if not file or file.filename == '':
        return "No file selected", 400
    if not z_height.isdigit():
        return "Invalid z-height", 400
    
# save file
 file_path = os.path.join(UPLOAD_FOLDER, file.filename)
 file.save(file_path)


#edge detection outline 



# convert to stl