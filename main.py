from flask import Flask, render_template, request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import requests

def decrypt(cipherbytes, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plainbytes = decryptor.update(cipherbytes) + decryptor.finalize()
    return plainbytes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/decrypt', methods=['POST'])
def file():
    senha = bytes(request.form['senha'], 'UTF-8')
    
    link = request.form['link']
    response = requests.get(link)
    file_64 = bytes(response.text, 'UTF-8')
    f = base64.decodebytes(file_64)

    plainbytes = decrypt(f, senha)
    return plainbytes

@app.route('/api/test', methods=['GET'])
def test():
    f = open('decrypt.py', 'rb')
    file = f.read()
    f.close()

    key = b'abcdefghijklmnop'
    while len(file.decode('UTF-8')) % len(key.decode('UTF-8')) != 0:
        file += b' '

    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    plainbytes = encryptor.update(file) + encryptor.finalize()

    f_64 = base64.encodebytes(plainbytes)
    return f_64

if __name__ == '__main__':
    app.run(debug=True)