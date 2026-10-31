
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/hello")
def hello():
    return "Hello! Flask is working."

if __name__ == "__main__":
    app.run(debug=True)
    
    
    #from flask import Flask, render_template

#app = Flask(__name__)

#@app.route("/")
#def home():
    #return render_template("index.html")

#if __name__ == "__main__":
    #app.run(debug=True)
