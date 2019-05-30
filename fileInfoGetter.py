"""
Author: Cheng Gao

"""
import os

from flask import Flask, render_template, request, send_file,after_this_request,g
from flask_dropzone import Dropzone
from infoGetter import infoGetter
from openpyxl import Workbook

basedir = os.path.abspath(os.path.dirname(__file__))
ig = infoGetter()
app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_DEFAULT_MESSAGE = "Click and Drag Your Folder Here. Please Rename the File as a JPG File for Object Recognition, and PNG for Optical Character Recognition",
    DROPZONE_MAX_FILE_SIZE=1024,  # set max size limit to a large number, here is 1024 MB
    DROPZONE_TIMEOUT=30000 * 1000,  # set upload timeout to a large number, here is 5 minutes
    DROPZONE_ALLOWED_FILE_CUSTOM = True,
    DROPZONE_ALLOWED_FILE_TYPE = 'image/*, .pdf, .txt, .doc, .docx, .mp4, .pptx, .xls, .xlsx, .msg',
    DROPZONE_PARALLEL_UPLOADS=3,  # set parallel amount
    DROPZONE_UPLOAD_MULTIPLE=True,  # enable upload multiple
    DROPZONE_MAX_FILES = 10000,

)

dropzone = Dropzone(app)

@app.route('/', methods=['POST', 'GET'])
def upload():
    fileList = []
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
        ig.getFileInfo(ig.flattenPaths(app.config['UPLOADED_PATH']))
    return render_template('index.html')
@app.route('/download', methods=['POST', 'GET'])
def download():
    @after_this_request
    def remove_file(response):  
        for f in ig.flattenPaths(app.config['UPLOADED_PATH']):
            os.remove(f)
        return response
    if request.method == 'POST':
        if request.form['Button'] == 'Download Result':
            return send_file("result.xlsx",
                             attachment_filename= 'result.xlsx',
                             as_attachment = True)
        if request.form['Button'] == 'Empty Folder':
            for f in ig.flattenPaths(app.config['UPLOADED_PATH']):
                os.remove(f)
            return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True, use_reloader=False)
