from flask import Flask, request, render_template_string
import pandas as pd

app = Flask(__name__)
data = pd.read_csv("retail_store_inventory.csv")

@app.route('/')
def home():
    total_items = len(data)
    return f"<h1>🛒 Welcome to Retail Inventory Dashboard</h1><p>Total Products: {total_items}</p>"

@app.route('/search')
def search():
    query = request.args.get('item')
    if query:
        filtered = data[data['item_name'].str.contains(query, case=False, na=False)]
        return filtered.to_html()
    return '''
    <h2>🔍 Search Inventory</h2>
    <form action="/search">
        <input name="item" placeholder="Enter item name...">
        <input type="submit">
    </form>
    '''

@app.route('/low-stock')
def low_stock():
    threshold = int(request.args.get('qty', 10))
    low_items = data[data['quantity'] < threshold]
    return f"<h2>⚠️ Low Stock Items (less than {threshold})</h2>" + low_items.to_html()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
