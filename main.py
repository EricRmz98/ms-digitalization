from flask import Flask, request
from flask_api import status
import pandas as pd
import requests

app = Flask(__name__)

def user_registration(request):
    try:
        # doc 'https://docs.google.com/spreadsheets/d/1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU/export?format=csv&id=1-Wx3MunuVlDT96K_fz18P1HgBUYaxSBjUu16_KyNjDU&gid=135007174'
        # my doc url'https://docs.google.com/spreadsheets/d/1ynSeKFh4bpz-y2akgqGGKljrz1Brhwj_Q1vT9tOkaBA/export?format=csv&id=1ynSeKFh4bpz-y2akgqGGKljrz1Brhwj_Q1vT9tOkaBA&gid=135007174'
        doc_url = request.json['docUrl']
        users = pd.read_csv(doc_url, header=0, on_bad_lines='skip').to_numpy()

        for user in users:
          payload = {
            'name': user[0] + ' ' + user[1],
            'email': user[2],
            'password': user[3]
          }

          requests.post('http://127.0.0.1:8000/v1/register', json=payload)

        return({'status': 'success'}, 200)

    except Exception as e:
        return({'error': e.args[0]}, 400)

@app.route('/register_users', methods=['POST'])
def user_quantity():
    response = user_registration(request)
    return response

if __name__ == '__main__':
    app.run(host='localhost', port=9000, debug=True)