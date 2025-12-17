from flask import Flask, render_template

app = Flask(__name__) #this is the main

@app.route("/")
def greet():
    return "<h1>Get Started with Flask</h1>" #directs to homepage

@app.route("/add")
def brief():
    return "<p1>Your test must run and work today. There's no longer tomorrow on this bs.</p1>" #just a paragraph on another page

@app.route("/tables")
def disp():
    return render_template('table test.html') #example of a table with details



if __name__ == "__main__":

    app.run(debug=True)
