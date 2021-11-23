from flask import url_for,Flask,render_template,request
import sqlite3
import os
currrentdir=os.path.dirname(os.path.abspath(__file__))


app=Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")


@app.route("/", methods=["POST"])
def phnbook():
    name=request.form["name"]
    number=request.form["number"]
    marks=request.form["marks"]
    connection=sqlite3.connect(currrentdir + "demodb.db")
    cursor=connection.cursor()
    query="INSERT INTO demodb VALUES('{n}','{m}','{l}')".format(n=name,m=number,l=marks)
    cursor.execute(query)
    connection.commit()
    return "data submitted"











if __name__ =="__main__":
    app.run(debug=True)
