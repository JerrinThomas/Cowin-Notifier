from flask import Flask


app = Flask(__name__)


@app.route('/user/register', methods=["POST"])
def register_user():

    return '200'


if __name__ == '__main__':
    app.run()
