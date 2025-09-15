from flask import Flask, render_template, request, redirect, url_for, send_file
import json
import os
from datetime import datetime

app = Flask(__name__)
DATA_FILE = 'blood_pressure.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    data = load_data()
    data.sort(key=lambda x: x['timestamp'], reverse=True)
    return render_template('index.html', entries=data)

@app.route('/add', methods=['POST'])
def add():
    systolic = request.form.get('systolic')
    diastolic = request.form.get('diastolic')
    if systolic and diastolic:
        entry = {
            'systolic': int(systolic),
            'diastolic': int(diastolic),
            'timestamp': datetime.now().isoformat(timespec='seconds')
        }
        data = load_data()
        data.append(entry)
        save_data(data)
    return redirect(url_for('index'))

@app.route('/download')
def download():
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'a').close()
    return send_file(DATA_FILE, as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)
