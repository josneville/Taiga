from helpers import get_next_purchase_item

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return get_next_purchase_item()

if __name__ == "__main__":
    app.run()
