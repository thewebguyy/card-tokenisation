from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SEERBIT_API_KEY = "SBPUBK_DQ24K6T5TI1WOAOYPWWYMGMHKDRVEGPW"

@app.route('/tokenize-card', methods=['POST'])
def tokenize_card():
    card_number = request.json.get('cardNumber')
    expiry_month = request.json.get('expiryMonth')
    expiry_year = request.json.get('expiryYear')
    cvv = request.json.get('cvv')

    if not card_number or not expiry_month or not expiry_year or not cvv:
        return jsonify({'error': 'Incomplete card details provided.'}), 400

    url = "https://seerbitapi.com/api/v2/payments/create-token"
    headers = {"Authorization": f"Bearer {SEERBIT_API_KEY}"}
    data = {
        "cardNumber": card_number,
        "expiryMonth": expiry_month,
        "expiryYear": expiry_year,
        "cvv": cvv
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response_data = response.json()
        if response.status_code == 200 and response_data.get('status') == 'SUCCESS':
            token = response_data['data']['token']
            return jsonify({'token': token}), 200
        else:
            error_message = response_data.get('message', 'Card tokenization failed.')
            return jsonify({'error': error_message}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'An error occurred during card tokenization.'}), 500

if __name__ == '__main__':
    app.run()
