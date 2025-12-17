import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def greet():
    return "<h1>Get Started with Flask</h1>"

@app.route("/add")
def brief():
    return "<p1>Your test must run and work today. There's no longer tomorrow on this bs.</p1>"

@app.route("/tables")
def disp():
    return render_template('table test.html')



if __name__ == "__main__":
    app.run(debug=True)