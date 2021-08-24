from flask import Flask, request, render_template
from content import get_content


app = Flask(__name__)
@app.route("/")
def main_page():
    '''Main page '''
    return render_template("index.html")


#print(login)
@app.route("/", methods = ['POST'])
def git_login() :
    '''Getting data from Github Api and return to the user'''
    login = request.form.get("nm")
    result = get_content("{}".format(login))
    return render_template("index.html",value=(result))


if __name__=="__main__" :
    app.run(debug=True)