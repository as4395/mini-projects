from flask import Flask, send_from_directory
import logging
import ssl
import yaml

# Load configuration
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

app = Flask(__name__, static_folder='static')

# Setup logging
logging.basicConfig(filename='access.log', level=logging.INFO)

@app.route("/")
def home():
    logging.info("Home page accessed")
    return send_from_directory('static', 'index.html')

@app.route("/<path:filename>")
def serve_file(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain('cert.pem', 'key.pem')
    app.run(host=config['host'], port=config['port'], ssl_context=context)
