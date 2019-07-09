from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename

#from myocr import ocr
from src.processor import process, get_pdf

app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('home.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_fileg():
   if request.method == 'POST':
      f = request.files['file']
      fname= secure_filename(f.filename)
      f.save("static/imgs/"+fname)
      out= process("static/imgs/"+fname) 
      return render_template("result.html", data= out ) 
		

@app.route('/pdf_downloader', methods = ['GET', 'POST'])
def download_pdf():
   #return "<h3>Hello World</h3>"
   fname= request.form['fname'] 
   outfile= get_pdf(fname)
   return send_file(outfile, as_attachment=True)


if __name__ == '__main__':
   app.run(debug = True)

