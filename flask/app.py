from flask import Flask
from flask import render_template # response for redirecting the html pages
from flask import request


"""
its create the instance of the Flask class
"""

#wsgi appliction
app=Flask( __name__)

@app.route("/")# home page
def welcome():#when server  goes to / route then this fuction will excute
    return "Welcome the flask "

@app.route("/index")
def index():

     return "welcome to the index page"

@app.route("/html_tag")
def html_tag():
    return "<html>  <h1>kiran</h1></html>"

@app.route("/redirect")
def redirect():
    return render_template("index.html")

#add the methods
@app.route("/methods",methods=[])#default is the GET method
def deaflult_method():
    return  "get method"

# GET + POST method example
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Access form data
        name = request.form.get("name")
        return f"Hello {name}, welcome to Flask learning"
    # If GET request, render the form
    return render_template("add.html")

@app.route("/sumbit",methods=["GET","POST"])
def sumbit():
    if request.method=="POST":
        name=request.form["name"]
        return f"hell {name} welcome to the flas learning"
    return render_template("add.html")

#varible rule
@app.route("/succes/<int:score>")
def succes(score):
    res=""
    if score>36:
        res= "pass"
    else:
        res="Fail"
    return render_template("result.html",result=res)


#use the loops
@app.route("/succes1/<int:score>")
def sussecs1(score):
    if score>36:
        res= "pass"
    else:
        res="Fail"
    exp={"score":score,"result":res}
    return render_template("result1.html",result=exp)
    


if __name__=="__main__": #starting point of the any .py files
    app.run(debug=True) 