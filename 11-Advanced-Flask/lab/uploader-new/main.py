from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/add-item')
def add_item():
   return render_template('add-item.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['image']
    filename = secure_filename(f.filename)
    print(filename.split('.'))
    extension = (filename.split('.')[1]).lower()
    if extension in ['svg', 'png', 'jpeg', 'jpg']:
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'File uploaded successfully {}'.format(filename)
    else:
        return "Wrong extension"
		
@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename))


if __name__ == '__main__':
   app.run(debug = True)