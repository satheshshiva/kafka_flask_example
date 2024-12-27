from flask import Flask, request, json

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
    return "ID is %d" % id

#Return HTML example
@app.route('/idInHtml/<int:id>')
def idInHtml(id):
    # show the post with the given id, the id is an integer
    return "ID is <b>%d</b>" % id

#Query Parameter Example
@app.route('/queryparam_example')
def queryparam_example():
    param1 = request.args.get('param1') 
    return '<h1> You sent %s </h1>' % param1

# GET AND POST Example
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        param1 = request.args.get('param1') 
        try:
            jsonData = json.loads(request.data)
        except:
            return "You sent param1 as {}. No json data was sent" % param1
        return "You sent param1 as <b>{}</b>. JSON you sent is <b>{}</b>. I am able to parse the name attribute as <b>{}</b>".format(param1,jsonData, jsonData["name"])
    else:
        return "This route only support POST method"