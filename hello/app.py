from flask import Flask

app = Flask(__name__)


@app.route("/health")
def hello():
    return {"message": "hello"}


@app.route("/version")
def world():
    return {"version": "v1.0"}


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
