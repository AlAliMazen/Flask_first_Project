import os
import json
#import Flask class and render_template and use request class for sending mail
from flask import Flask, render_template, request

app=Flask(__name__)

# rout is just to tell python where to find the re  quired page
@app.route("/")
def index():
    #we can return either the html file ->usual task, and or render the text into HTML
    # we can give a second parameter to the view function which can be used from the template pages like the title of the page
    return render_template("index.html")

#the def function which is under the decorator is called a view 
@app.route("/about")
def about():
    #loading json file as read only in the data python list using with open
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    #you can use as many paramters as you want in the render_template view function 
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
def about_member(member_name):
    member={}
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member=obj
    
    return render_template("member.html", character=member)


@app.route("/contact", methods=["GET","POST"])
def contact():
    if request.method =="POST":
        print("Hello, anybody there!")
        #form is a dictionary; that is either use get(Keyname), or square brackets with keys to get value
        # get is exception safe and return none when key is not there, while square bracket throw an exception 
        print(request.form.get("name"))
        #print(request.form["name"])
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")

if __name__=="__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5001")),
        #in production make sure to make the debugger true.
        debug=True
    )