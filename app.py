# importing two methods from flask, "Flask" and "render_template"
from flask import Flask, render_template
My_app = Flask(__name__) # creates the Flask instance.
#__name__ is the name of the current Python module. 
# #The app needs to know where it’s located to set up some paths, and __name__ is a convenient way to tell it that.

@My_app.route("/")
def index():
    '''
    Displays the index page accessible at '/'
    '''
    return render_template('index.html')