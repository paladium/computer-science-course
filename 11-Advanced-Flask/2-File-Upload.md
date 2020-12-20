# File uploading in Flask
Handling file upload in Flask is very easy. It needs an HTML form with its enctype attribute set to 'multipart/form-data', posting the file to a URL. The URL handler fetches file from request.files[] object and saves it to the desired location.

Each uploaded file is first saved in a temporary location on the server, before it is actually saved to its ultimate location. Name of destination file can be hard-coded or can be obtained from filename property of request.files[file] object. However, it is recommended to obtain a secure version of it using the secure_filename() function.

```html
<html>
   <body>
      <form action = "{{ url_for('upload_file') }}" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "image" />
         <input type = "submit"/>
      </form>
   </body>
</html>
```

```python
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route('/add-item')
def add_item():
   return render_template('add-item.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['image']
      f.save(f.filename)
      return 'File uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
```

## Displaying images
To display images, we first need to configure the upload folder where the images will be stored:

```python
from flask import Flask, render_template, request, redirect
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#Max 16 mb
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
```

Next, let's change our upload function slightly:

TODO fix secure_filename new file

```python
@app.route('/uploader', methods = ['POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['image']
      filename = secure_filename(f.filename)
      f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      return 'File uploaded successfully'
```
So first of all, we use the function secure_filename, which will create a unique random string (called UUID) with the correct extension of the file, next we join the filename with the path to our upload folder (do not forget to create it static/uploads). Finally, the file is saved into that path.

Next, we need to add a new route:

```python
@app.route('/display/<filename>')
def display_image(filename):
	return redirect(url_for('static', filename='uploads/' + filename))
```

This function uses redirect function provided by Flask to redirect to a different URL, in this case we want to redirect to full url on the server, where images are stored.
