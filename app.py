import os
from config import Config
from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(Config)

@app.route("/")
def index():
    return render_template("layout.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)