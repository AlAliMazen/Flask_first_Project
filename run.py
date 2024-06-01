import os
#import Flask class and render_template
from flask import Flask, render_template

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
    #you can use as many paramters as you want in the render_template view function 
    return render_template("about.html", page_title="About", list_of_numbers=[1,2,3,4])


@app.route("/contact")
def contact():
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