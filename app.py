from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","post"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","post"])
def main():
    #database
    return(render_template("main.html"))

if __name__ == "__main__":
    app.run()