from flask import Flask, render_template, request, send_file
from flask_restful import Api, Resource
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import requests

def decrypt(cipherbytes, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plainbytes = decryptor.update(cipherbytes) + decryptor.finalize()
    return plainbytes

class Decrypt(Resource):
    def get(self):
        pass

    def post(self):
        senha = request.form['senha']
        link = request.form['link']
        file_64 = requests.get(link)
        file = base64.decodebytes(file_64)
        plainbytes = decrypt(file, senha)
        f = open('temp.bin', 'wb')
        f.write(plainbytes)
        f.close()
        return send_file('temp_files/temp.bin')

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/test', methods=['GET'])
def test():
    f = open('decrypt.py', 'rb')
    f_64 = base64.encodebytes(f.read())
    f.close()
    return f_64

api.add_resource(Decrypt, '/api/decrypt')

if __name__ == '__main__':
    app.run(debug=True)