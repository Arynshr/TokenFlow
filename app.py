from flask import Flask, render_template, request, jsonify
import os
import tokeniser

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error = 'No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error = 'No file selected')
        if file:
            file_path = 'uploaded_file.txt'
            file.save(file_path)
            stop_words = ["is","a","the","and","are","about","it","lets"]
            tokens, frequency = tokeniser.process_file(file_path, stop_words)
            os.remove(file_path)
            return render_template('result.html', tokens=tokens, frequency = frequency)
        return render_template('index.html')
    
@app.route('/result')
def results():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(debug = True)
