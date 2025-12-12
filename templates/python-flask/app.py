# barebones flask template
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"Hello": "World"})

if __name__ == "__main__":
    # Helpful message when running directly
    print("Run with 'flask run' or 'python app.py'. For development, FLASK_ENV=development")
    app.run(host="0.0.0.0", port=5555, debug=True)
