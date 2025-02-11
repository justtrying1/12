from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

json_file_path = 'data.json'

# Главная страница с формой
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['GET'])
def get_data():
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)
        return jsonify(data)
    return jsonify([])

@app.route('/data', methods=['POST'])
def post_data():
    new_data = request.json
    
    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            data = json.load(f)
    else:
        data = []
    
    data.append(new_data)

    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

    return jsonify(new_data), 201

if __name__ == '__main__':
    app.run(port=3000)