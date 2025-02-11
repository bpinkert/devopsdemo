from flask import Flask, render_template

app = Flask(__name__)

# A simple route for the main page
@app.route('/')
def home():
    # Render an HTML template with some dynamic data
    name = "John Doe"
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)