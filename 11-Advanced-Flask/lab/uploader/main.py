from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/add-item')
def add_item():
   return render_template('add-item.html')
	
@app.route('/uploader', methods = ['POST'])
def upload_file():
    f = request.files['image']
    f.save(f.filename)
    return 'File uploaded successfully'
		
if __name__ == '__main__':
   app.run(debug = True)
