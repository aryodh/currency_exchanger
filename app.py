from flask import Flask, request, render_template, jsonify
import requests, json

app = Flask(__name__)

lis_cur = [
"AUD","BGN","BRL","CAD",
"CHF","CNY","CZK","DKK",
"EUR","GBP","HKD","HRK",
"HUF","IDR","ILS","INR",
"ISK","JPY","KRW","MXN",
"MYR","NOK","NZD","PHP",
"PLN","RON","RUB","SEK",
"SGD","THB","TRY","USD",
"ZAR"]

@app.route('/')
def index():
    return render_template("index.html", lis_cur=lis_cur)

# http://127.0.0.1:5000/convert/?from=usd&to=idr&total=1
@app.route('/convert/')
def convert():
    inp = request.args.to_dict()
    link = "https://api.exchangeratesapi.io/latest?base=" + inp['from'].upper()
    data = requests.get(link).json()
    res = float(inp['total']) * data['rates'][inp['to'].upper()] 
    return jsonify(
        currency = inp['to'].upper(), 
        total = "%.2f" % res,
        date = data['date']
        )



if __name__ == '__main__':
    app.run()