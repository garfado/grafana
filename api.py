from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo
data = [
    {
        "beer_name": "IPA",
        "customer_name": "John Doe",
        "order_date": "2024-12-01",
        "quantity": 25
    },
    {
        "beer_name": "Stout",
        "customer_name": "Jane Smith",
        "order_date": "2024-12-02",
        "quantity": 13
    },
    {
        "beer_name": "Lager",
        "customer_name": "Alice Johnson",
        "order_date": "2024-12-03",
        "quantity": 100
    }
]

@app.route('/beer_sales', methods=['GET'])
def get_beer_sales():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

