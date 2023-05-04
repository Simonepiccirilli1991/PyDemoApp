from flask import Flask, request

from model.UserRequest import UserRequest

app = Flask("WebApp")


@app.route('/service', methods=['POST'])
def process_request():
    request_data = request.get_json()
    # Do something with the user_request object
    return request_data


app.run(debug=True, port=8080)
