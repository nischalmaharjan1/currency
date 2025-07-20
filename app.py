from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    currencies = ["USD", "EUR", "GBP", "JPY", "INR", "CAD", "AUD", "CHF", "CNY"]

    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        # Fetch exchange rate
        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
        response = requests.get(url)
        data = response.json()

        result = f"{amount} {from_currency} = {data['result']:.2f} {to_currency}"

    return render_template("index.html", result=result, currencies=currencies)

if __name__ == "__main__":
    app.run(port=7007)

