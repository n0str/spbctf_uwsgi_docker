import time
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(3)
    return "Hello abc Flask inside Docker!!"


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
