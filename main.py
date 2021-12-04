from flask import Flask, render_template, request
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import base64
import requests

# função responsável pela decifra
def decrypt(cipherbytes, key):
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    decryptor = cipher.decryptor()
    plainbytes = decryptor.update(cipherbytes) + decryptor.finalize()
    return plainbytes

# instanciação da API
app = Flask(__name__)

# definição/disponibilização do endpoint / responsável pela interface gráfica
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# definição/disponibilização do endpoint /api/file, responsável por responder com o arquivo decifrado
@app.route('/api/decrypt', methods=['POST'])
def file():
    # transforma a senha em bytes
    senha = bytes(request.form['senha'], 'UTF-8')
    
    # recupera o base64 do arquivo no endpoint disponibilizado e transforma em bytes
    link = request.form['link']
    response = requests.get(link)
    file_64 = bytes(response.text, 'UTF-8')
    f = base64.decodebytes(file_64)

    # decifra o arquivo e retorna para o client
    plainbytes = decrypt(f, senha)
    return plainbytes

# definição/disponibilização do endpoint /api/test, responsável por disponibilizar o base64 de um arquivo teste
@app.route('/api/test', methods=['GET'])
def test():
    # lê os bytes de um arquivo
    f = open('decrypt.py', 'rb')
    file = f.read()
    f.close()

    # lê os 16 bytes da senha de teste
    key = b'abcdefghijklmnop'

    # Adiciona bytes de espaço ao fim do arquivo até seu tamanho ser múltiplo de 16 (n*16)
    while len(file.decode('UTF-8')) % len(key.decode('UTF-8')) != 0:
        file += b' '

    # Cifra o arquivo utilizando a senha de teste
    cipher = Cipher(algorithms.AES(key), modes.ECB())
    encryptor = cipher.encryptor()
    plainbytes = encryptor.update(file) + encryptor.finalize()

    # Transforma os bytes do arquivo cifrado e retorna ao client
    f_64 = base64.encodebytes(plainbytes)
    return f_64

# disponibilização da API
if __name__ == '__main__':
    app.run(debug=True)