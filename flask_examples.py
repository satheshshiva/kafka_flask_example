from flask import Flask, request

app = Flask(__name__)

#Root page
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#Path Variable with data type
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return "User name is %s" % username

#Path Variable with data type
@app.route('/id/<int:id>')
def show_post(id):
    # show the post with the given id, the id is an integer
    return "ID is %d" % post_id

#Return HTML example
@app.route('/idInHtml/<int:id>')
def idInHtml(id):
    # show the post with the given id, the id is an integer
    return "ID is <b>%d</b>" % post_id

#Query Parameter Example
@app.route('/queryparam_example')
def queryparam_example():
    param1 = request.args.get('param1') 
    return '<h1> You sent %s </h1>' % param1