import os
import json
import base64
from flask import Flask, request, render_template_string, send_from_directory, redirect
from werkzeug.utils import secure_filename
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

app = Flask(__name__)
CONFIG = json.load(open("config.json"))

UPLOAD_DIR = CONFIG["upload_dir"]
PASSWORD = CONFIG["password"]
USERNAME = CONFIG["username"]
KEY_SALT = CONFIG["salt"].encode()
ENCRYPTION_KEY = None

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Basic HTML interface
HTML = '''
<h2>Pi Cloud Upload/Download</h2>
{% if error %}<p style="color:red;">{{ error }}</p>{% endif %}
<form method="POST" enctype="multipart/form-data">
    Username: <input name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="file" name="file"><br>
    <input type="submit" value="Upload">
</form>

<h3>Available Files:</h3>
<ul>
{% for file in files %}
    <li><a href="/download/{{ file }}">{{ file }}</a></li>
{% endfor %}
</ul>
'''

def derive_key(password):
    # Derive AES key using PBKDF2.
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=KEY_SALT,
        iterations=100000,
    )
    return kdf.derive(password.encode())

def encrypt_file(path, key):
    """Encrypt file with AES-256-CBC."""
    from cryptography.hazmat.primitives import padding
    iv = os.urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    with open(path, 'rb') as f:
        data = f.read()
    padder = padding.PKCS7(128).padder()
    padded = padder.update(data) + padder.finalize()
    encrypted = encryptor.update(padded) + encryptor.finalize()
    with open(path, 'wb') as f:
        f.write(iv + encrypted)

def decrypt_file(path, key):
    """Decrypt file with AES-256-CBC."""
    from cryptography.hazmat.primitives import padding
    with open(path, 'rb') as f:
        raw = f.read()
    iv = raw[:16]
    data = raw[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded = decryptor.update(data) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    return unpadder.update(padded) + unpadder.finalize()

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    files = os.listdir(UPLOAD_DIR)
    if request.method == 'POST':
        if request.form.get('username') != USERNAME or request.form.get('password') != PASSWORD:
            error = "Invalid credentials"
        else:
            f = request.files['file']
            if f:
                filename = secure_filename(f.filename)
                save_path = os.path.join(UPLOAD_DIR, filename)
                f.save(save_path)
                encrypt_file(save_path, ENCRYPTION_KEY)
                return redirect('/')
    return render_template_string(HTML, files=files, error=error)

@app.route('/download/<filename>')
def download(filename):
    try:
        file_path = os.path.join(UPLOAD_DIR, filename)
        temp_path = file_path + ".tmp"
        decrypted = decrypt_file(file_path, ENCRYPTION_KEY)
        with open(temp_path, 'wb') as f:
            f.write(decrypted)
        return send_from_directory(UPLOAD_DIR, filename + ".tmp", as_attachment=True, download_name=filename)
    finally:
        try:
            os.remove(temp_path)
        except:
            pass

if __name__ == '__main__':
    ENCRYPTION_KEY = derive_key(PASSWORD)
    app.run(host='0.0.0.0', port=5000)
