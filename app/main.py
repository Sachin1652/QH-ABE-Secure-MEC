from flask import Flask, request, jsonify
from encryption import encrypt_data
from decryption import decrypt_data
from qkd import generate_qkd_key

app = Flask(__name__)

@app.route("/")
def home():
    return "QH-ABE Secure MEC API Running!"

@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.json.get("data")
    if not data:
        return jsonify({"error": "No data provided"}), 400
    encrypted_data = encrypt_data(data)
    return jsonify({"encrypted": encrypted_data})

@app.route("/decrypt", methods=["POST"])
def decrypt():
    encrypted_data = request.json.get("encrypted_data")
    if not encrypted_data:
        return jsonify({"error": "No encrypted data provided"}), 400
    decrypted_data = decrypt_data(encrypted_data)
    return jsonify({"decrypted": decrypted_data})

@app.route("/qkd", methods=["GET"])
def get_qkd_key():
    return jsonify({"qkd_key": generate_qkd_key()})

if __name__ == "_main_":
    app.run(host="0.0.0.0", port=5000, debug=True)