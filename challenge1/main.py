from flask import Flask
from transactions import transaction_blueprint  # Assuming this is the correct import

app = Flask(__name__)
app.register_blueprint(transaction_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
