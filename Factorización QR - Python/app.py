
from flask import Flask, url_for, render_template, request
from markupsafe import escape
import qr

app = Flask(__name__)

global data
data = {}
@app.route('/', methods =["GET", "POST"])
@app.route('/index', methods =["GET", "POST"])
def index():
    data["active"] =  ["active","","",""]
    data["result"] = None
    data["Q"] = []
    data["R"] = []
    if  request.method=='POST' :
        data["result"] = (request.form["myquery"])
        if data["result"] != "":
            data["values"] = qr.createMatrix(int(data["result"]))
            return render_template("index.html",data=data,values = data["values"], Q = data["Q"], R =data["R"])
    return render_template("index.html",data=data)
@app.route('/calculate', methods =["GET", "POST"])
def calculate():
     if  request.method=='POST':
        for i in range(int(data["result"])):
            for j in range(int(data["result"])):
                data["values"][i][j] = int(request.form[f"value-{i}-{j}"]) 
        data["Q"],data["R"] = qr.calculteQR(data["values"])
        return render_template("index.html",data=data,values = data["values"], Q = data["Q"], R =data["R"])
@app.route('/marco')
def marco():
    data["active"] =  ["","active","",""]
    return render_template("marco.html",data=data)
@app.route('/about')
def about():
    data["active"] =  ["","","active",""]
    return render_template("about.html",data=data)
@app.route('/agradecimientos')
def agradecimientos():
    data["active"] =  ["","","","active"]
    return render_template("agradecimientos.html",data=data)

# app.run(debug=True)
