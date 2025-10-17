from flask import Flask, request, send_file, jsonify, render_template
from flask_cors import CORS
import qrcode
import io
import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app)


def get_teacher_form_link(teacher_id):
    conn = sqlite3.connect('teachers.db')
    cursor = conn.cursor()
    cursor.execute("SELECT form_link FROM teachers WHERE id = ?", (teacher_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return row[0]
    return None

@app.route('/')
def index_page():   # unique name
    return render_template('index.html')

# Serve the HTML page
@app.route('/')
def home():
    return render_template('index.html')

# QR code generation route
@app.route('/generate-qr', methods=['POST'])
def generate_qr():
    try:
        data = request.json.get('data', '')
        if not data:
            return jsonify({'error': 'No data provided'}), 400

        qr_img = qrcode.make(data)
        buf = io.BytesIO()
        qr_img.save(buf, format='PNG')
        buf.seek(0)
        return send_file(buf, mimetype='image/png')
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get-form-link/<int:teacher_id>', methods=['GET'])
def get_form_link(teacher_id):
    link = get_teacher_form_link(teacher_id)  # fetch from DB
    if link:
        return jsonify({"form_link": link}), 200
    else:
        return jsonify({"error": "Form link not found for this teacher"}), 404

@app.route('/add-teacher', methods=['POST'])
def add_teacher():
    try:
        data = request.json
        name = data.get("name")
        subject = data.get("subject")
        form_link = data.get("form_link")

        if not (name and subject and form_link):
            return jsonify({"error": "All fields are required"}), 400

        conn = sqlite3.connect('teachers.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO teachers (name, subject, form_link) VALUES (?, ?, ?)",
            (name, subject, form_link)
        )
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()

        return jsonify({
            "status": "success",
            "teacher_id": new_id,
            "name": name,
            "subject": subject
        })
    except Exception as e:
        print("❌ Error in add-teacher:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
