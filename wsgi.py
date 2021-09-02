from flask import Flask, request, render_template, redirect, url_for
import graphene
from graphene import ObjectType, Schema, Argument, String, Int,  Field, NonNull, List
from flask_graphql import GraphQLView
import json
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv
from graphql import GraphQLError

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_TOKEN = os.environ.get("API_TOKEN")

app = Flask(__name__)

@app.route("/")
def main_page():
    '''Main page '''
    return render_template("index.html")


class User(ObjectType):
    full_name  = String()
    repositories = String()


class UserQuery (ObjectType):
    user = graphene.Field(User,login=graphene.String())


    def resolve_user(self, info,login):
        headers = {'Authorization': 'token %s' % API_TOKEN }
        url_name = "https://api.github.com/users/{}".format(login)
        data = {"type" : "all", "sort" : "full_name", "direction" : "asc"}
        full_name = requests.get(url_name, data = json.dumps(data), headers = headers)
        if full_name.status_code == 200 :
            full_name = json.loads(full_name.text)
            full_name = full_name['name']
        else :
            full_name = None
        url_repo = "https://api.github.com/users/{}/repos".format(login)
        repos_list = requests.get(url_repo, data = json.dumps(data), headers = headers)
        if repos_list.status_code == 200 :
            repos_list = json.loads(repos_list.text)
            repositories = []
            for res in repos_list:
                repositories.append(res['name'])
            repositories = ','.join(repositories)
        else :
            repos_list = None
        if not repos_list or not full_name:
            full_name = 'no full name'
            repositories = '0'


        user_info = User(full_name = full_name, repositories = repositories )
        return user_info

userSchema = Schema(query=UserQuery)


@app.route("/", methods = ['POST'])
def git_login() :
    login = request.form.get("nm")
    graphqltest = UserQuery()
    result = graphqltest.resolve_user("info",login)
    return render_template("index.html",value="Full name: {} . Repositories: {}".format(result.full_name,result.repositories))



app.add_url_rule('/user', view_func=GraphQLView.as_view(
    'graphql',
    schema=userSchema,
    graphiql=True,
))


if __name__=="__main__" :
    app.run(debug=True)