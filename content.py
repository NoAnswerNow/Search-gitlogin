import json
import os
from os.path import join, dirname
import requests
from dotenv import load_dotenv


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
API_TOKEN = os.environ.get("API_TOKEN")



def get_content(login) :
    '''Get content from api.github using token'''
    print(API_TOKEN)
    headers = {'Authorization': 'token %s' % API_TOKEN }
    url_name = "https://api.github.com/users/{}".format(login)
    data = {"type" : "all", "sort" : "full_name", "direction" : "asc"}
    req_name = requests.get(url_name, data = json.dumps(data), headers = headers)
    print(req_name)
    print(req_name.text)
    if req_name.status_code == 200 :
        req_name = json.loads(req_name.text)
    else :
        req_name = None
    url_repo = "https://api.github.com/users/{}/repos".format(login)
    req_repo = requests.get(url_repo, data = json.dumps(data), headers = headers)
    if req_repo.status_code == 200 :
        req_repo = json.loads(req_repo.text)
    else :
        req_repo = None
    if not req_repo or not req_name:
        return ("Cannot find the user")
    else :
        result = []
        if not req_name['name']:
            for res in req_repo :
                result.append(res['name'])
            result = ','.join(result)
            return ("Username not available. Login - " + req_name['login'] + " : " + result)
        else:
            for res in req_repo:
                result.append(res['name'])
            result = ','.join(result)
            return (req_name['name'] + " : " + result)


