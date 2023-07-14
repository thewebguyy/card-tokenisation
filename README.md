# card-tokenisation
This README provides instructions on how to install and run the app, as well as how to test the app using the cURL command.

To install the app, you will need to install the Flask and requests libraries. You can do this by running the following commands in your terminal:

pip install flask
pip install requests
Once you have installed the libraries, you can run the app by running the following command in your terminal:

python app.py
The app will run on port 5000. You can test the app by making a POST request to the /tokenize-card endpoint with the card details as JSON data. For example, you can use the following cURL command to test the app:

curl -X POST -H "Content-Type: application/json" -d '{"cardNumber": "4111111111111111", "expiryMonth": "12", "expiryYear": "23", "cvv": "123"}' http://localhost:5000/tokenize-card

If the tokenization is successful, the app will return the token as a JSON response. Otherwise, the app will return an error message.
