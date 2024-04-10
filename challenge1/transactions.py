from flask import Flask, Blueprint, jsonify

transaction_blueprint = Blueprint('transactions', __name__)

@transaction_blueprint.route('/transaction/<id>', methods=['GET'])
def get_transaction(id):
    with open('transactions.json') as data_file:
        transactions_data = json.load(data_file)
    transaction = transactions_data.get(id, None)
    return jsonify(transaction), 200

@transaction_blueprint.route('/transaction', methods=['POST'])
def add_transaction():
    # TODO: Implement adding a new transaction
    return jsonify({"message": "Transaction added successfully"}), 201

@transaction_blueprint.route('/transaction/<id>', methods=['PUT'])
def update_transaction(id):
    # TODO: Implement updating an existing transaction
    return jsonify({"message": "Transaction updated successfully"}), 200

@transaction_blueprint.route('/transaction/<id>', methods=['DELETE'])
def delete_transaction(id):
    # TODO: Implement deleting an existing transaction
    return jsonify({"message": "Transaction deleted successfully"}), 204

# Create the Flask app and register the blueprint
app = Flask(__name__)
app.register_blueprint(transaction_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)

