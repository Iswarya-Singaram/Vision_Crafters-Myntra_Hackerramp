from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_cors import CORS
from pythonscripts import blenderinvoker
import webbrowser

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

def open_browser():
    webbrowser.open_new_tab('http://127.0.0.1:5000/')

@app.route('/')
def initial():
    return render_template('home.html')

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        obj = request.json
        if obj:
            print(obj)
            blenderinvoker.execute(obj)
            return jsonify({"status": "done"})
        else:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400
    else:
        return render_template('index.html')

@app.route('/try_on_clothes', methods=['GET', 'POST'])
def try_on_clothes():
    if request.method == 'POST':
        obj = request.json
        if obj:
            print(obj)
            blenderinvoker.try_on_clothes(obj)
            return jsonify({"status": "done"})
        else:
            return jsonify({"status": "error", "message": "No JSON data received"}), 400

@app.route('/model')
def model():  
    return send_from_directory('projectexports', 'generatedbody.glb')

@app.route('/final_model')
def final_model():  
    return send_from_directory('projectexports', 'final_model.glb')

@app.route('/avatar')
def avatar():
    return render_template('avatar.html')

if __name__ == '__main__':
    open_browser()
    app.run(debug=True)
