import os
#import Falsk class and render_template
from flask import Flask, render_template

app=Flask(__name__)

# rout is just to tell python where to find the re  quired page
@app.route("/")
def index():
    #we can return either the html file ->usual task, and or render the text into HTML
    return render_template("index.html")

#the def function which is under the decorator is called a view 
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__=="__main__":
    app.run(
        host=os.environ.get("IP","0.0.0.0"),
        port=int(os.environ.get("PORT","5001")),
        #in production make sure to make the debugger true.
        debug=True
    )