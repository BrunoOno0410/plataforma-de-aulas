from flask import Flask, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/meu_banco_de_dados"
mongo = PyMongo(app)


@app.route("/")
def index():
    return jsonify({"message": "Bem-vindo à API Flask"})


if __name__ == "__main__":
    app.run(debug=True)
