from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"


@app.route('/predict', methods=['POST'])
def print_square():
    received_value = int(request.get_json(force=True))
    print(received_value)
    return str(received_value**2) + "\n"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    # A few things to remember while making the flask app is that the host should be set to ‘0.0.0.0’
    # because we are running it inside Docker.
