# This is the application to convert plain text into cipher text using key transportation cipher
from flask import Flask, render_template, request,url_for,session
import os
app = Flask(__name__)
secret=os.urandom(24)
app.secret_key=secret


@app.route("/")
def welcome():
    return render_template('index.html')

@app.route("/encrypt", methods=['POST'])
def encrypt():
    if request.method == 'POST':
        plain = request.form.get('plain', '')
        key = request.form.get('key', '')  

        if not plain or not key:
            return render_template('/error.html')

        n = len(key)
        m = len(plain)

        #to get the number of coloumn for the given size of text i.e m in this case
        num_rows = (m + n - 1) // n
        array = [['' for _ in range(n)] for _ in range(num_rows)] 
        encrypt = [['' for _ in range(n)] for _ in range(num_rows)] 
        index = 0
        for i in range(num_rows):
            for j in range(n):
                if index < m:
                    array[i][j] = plain[index]
                    index += 1
        key_list = list(range(n))
        for i in range(n):
            key_list[i] = int(key[i]) - 1

        # this is the to encrypt the plain text
        for i in range(num_rows):
            for j in range(n):
                encrypt[i][j] = array[i][key_list[j]]

        session["encrypted_data"]=encrypt
        session["key_list"]=key_list
        return render_template('encrypt.html', result=encrypt)

@app.route("/decrypt", methods=['POST'])
def decrypt():
    encrypt = session.get("encrypted_data", None)
    key_list = session.get("key_list", None)

    if encrypt is not None and key_list is not None:
        num_rows = len(encrypt)
        n = len(key_list)
        decrypt = [['' for _ in range(n)] for _ in range(num_rows)]

        for i in range(num_rows):
            for j in range(n):
                decrypt[i][key_list[j]] = encrypt[i][j]

        return render_template("decrypt.html", result=decrypt)
    else:
        return "Could not decrypt the message; session ended!"

if __name__ == '__main__':
    app.run(debug=True)
