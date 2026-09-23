from flask import Flask

app = Flask(__name__)

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    return str(a - b)

@app.route("/health")
def health():
    return "SUB service is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)