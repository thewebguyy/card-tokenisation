import requests
import json

TEST_SECRET_API_KEY = "SBTESTSECK_FoYlP9xMzRL1gdN2yLZkA5htjlmw8i1WYWKwj84g"
TEST_PUBLIC_KEY = "SBTESTPUBK_OQYbP7c42i8YAEdj7x7GeoWfeTZgWci3"
PRODUCTION_SECRET_API_KEY = "YOUR_PRODUCTION_SECRET_API_KEY"
PRODUCTION_PUBLIC_KEY = "YOUR_PRODUCTION_PUBLIC_KEY"

# Use the appropriate public key based on the environment
PUBLIC_KEY = TEST_PUBLIC_KEY

def tokenize_card(card_number, expiry_month, expiry_year, cvv):
    url = "https://seerbitapi.com/api/v2/charge-token/create-token"
    headers = {"Authorization": f"Bearer {TEST_SECRET_API_KEY}"}
    data = {
        "cardNumber": card_number,
        "expiryMonth": expiry_month,
        "expiryYear": expiry_year,
        "cvv": cvv,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["token"]
    else:
        raise Exception(response.json()["message"])


def charge_card(token, amount):
    url = "https://seerbitapi.com/api/v2/charges"
    headers = {"Authorization": f"Bearer {TEST_SECRET_API_KEY}"}
    data = {
        "token": token,
        "amount": amount,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["message"])


def retrieve_payment(payment_id):
    url = f"https://seerbitapi.com/api/v2/payments/{payment_id}"
    headers = {"Authorization": f"Bearer {TEST_SECRET_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["message"])


def refund_payment(payment_id, amount):
    url = f"https://seerbitapi.com/api/v2/payments/{payment_id}/refund"
    headers = {"Authorization": f"Bearer {TEST_SECRET_API_KEY}"}
    data = {
        "amount": amount,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["message"])


def payment_notifications(payment_id, public_key):
    url = f"https://seerbitapi.com/api/v2/payments/{payment_id}/webhook"
    headers = {"Authorization": f"Bearer {TEST_SECRET_API_KEY}"}
    data = {
        "public_key": public_key,
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json()["message"])


def main():
    token = tokenize_card("4111111111111111", "12", "23", "123")
    payment = charge_card(token, 1000)
    print(payment)
    payment_notifications(payment["id"], PUBLIC_KEY)


if __name__ == "__main__":
    main()
