from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def world():
    return jsonify({"message": "world"})


@app.route("/version")
def version():
    return jsonify({"version": "v1.0"})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
