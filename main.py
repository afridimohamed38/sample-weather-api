from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    temperature = str(23)
    return {"station": station,
            "date": date,
            "temperature": temperature}


if __name__ == "name":
    app.run(debug=True)
