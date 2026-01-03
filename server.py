from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/webhook/nowpayments", methods=["POST"])
def nowpayments_webhook():
    data = request.json
    print("WEBHOOK DATA:", data)

    if data.get("payment_status") == "finished":
        user_id = data.get("order_id")
        amount = data.get("price_amount")
        print(f"PAYMENT OK: user={user_id}, amount={amount}")

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
