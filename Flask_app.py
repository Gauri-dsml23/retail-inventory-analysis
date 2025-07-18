from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    data = pd.read_csv("retail_store_inventory.csv")
    return f"<h1>Total Items: {len(data)}</h1>"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
