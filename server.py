from helpers import get_next_purchase_item

from flask import Flask
from flask_restful import Api
app = Flask(__name__)
api = Api(app)

@app.route("/")
def hello():
    return get_next_purchase_item()

if __name__ == "__main__":
    app.run()
