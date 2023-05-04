from flask import Flask

app = Flask("WebApp")

@app.route("/")
def localPage():
    return "Hello first web app"


app.run('0.0.0.0', debug=True)
