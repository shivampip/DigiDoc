from flask import Flask, render_template, request
from werkzeug import secure_filename

from myocr import ocr

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_fileg():
   if request.method == 'POST':
      f = request.files['file']
      fname= secure_filename(f.filename)
      f.save("imgs/"+fname)
      text= ocr(fname) 
      return text
		
if __name__ == '__main__':
   app.run(debug = True)