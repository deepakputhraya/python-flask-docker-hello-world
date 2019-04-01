from flask import Flask

app = Flask(__name__)


@app.route("/health")
def world():
    return {"message": "world"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=4000)
