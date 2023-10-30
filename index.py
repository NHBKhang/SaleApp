from flask import Flask, render_template
import dao

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', catogories=cat, products=prod)

if __name__ == '__main__':
    cat = dao.get_catogories()
    prod = dao.get_products()

    app.run(debug=True)