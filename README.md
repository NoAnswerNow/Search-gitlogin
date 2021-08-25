*Python module to get name and all repos of the user from GitHub with using GitHub REST API*
# GitHub login![IMG_6509](https://user-images.githubusercontent.com/86563053/130796037-d606bbd3-491c-4658-9e73-cd47bbfd64a8.jpg)
This project enables you to find GitHub resources such as user,repositories of the user (default) or all information what you need (after parameter changes) with GitHub API. 
 You can see it here : https://github-login1.herokuapp.com/ 
 ## How to start project
 For local (your localhost) work :
  - create .env file in project and add API_TOKEN ="your api token" (read here: https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
  - run wsgi.py
  
 For deploy on Heroku :
 - you must have heroku auth:token (read here : https://devcenter.heroku.com/articles/authentication)
 
 ## test_flask.py
 Testing your code brings a wide variety of benefits. It increases your confidence that the code behaves as you expect and ensures that changes to your code won’t cause problems.
 In this project we have 6 basic checks:
 - Open main page and check 'Search' word exists and status code is 200
 - Check that we receive correct data for empty user
 - Check that we receive correct data for incorrect symbols user
 - Check that we receive correct data for no name user
 - Check that we receive correct data for user that exists
 - Check that we receive correct data for non existing user
 
 For example : 
 Check that we receive correct data for empty user
 
 
 
 'def test_no_data_for_empty_user(client):
 
      data = {
                "nm": "",
            }

    rv = client.post('/',data=data)
    assert b'Cannot find the user'  in rv.data
    assert b'Search' in rv.data
    assert '200' in rv.status'

## main.yml
In this project workflow run with GitHub event "push" and all run automatically (main.yml)

Steps: 
- Checks-out your repository under $GITHUB_WORKSPACE
- Set up Python 3.9 environment
- Install dependencies
- Run tests
All your variable values are taken from environment variable using Git-secret and Heroku config vars . This ensures the protection of personal data.
Project checked with using Pylint.

### Required prerequisites :
python== 3.9.1
astroid==2.7.2
atomicwrites==1.4.0
attrs==21.2.0
certifi==2021.5.30
charset-normalizer==2.0.4
click==8.0.1
colorama==0.4.4
Flask==2.0.1
idna==3.2
iniconfig==1.1.1
isort==5.9.3
itsdangerous==2.0.1
Jinja2==3.0.1
lazy-object-proxy==1.6.0
MarkupSafe==2.0.1
mccabe==0.6.1
packaging==21.0
platformdirs==2.2.0
pluggy==0.13.1
py==1.10.0
pylint==2.10.2
pyparsing==2.4.7
pytest==6.2.4
python-dotenv==0.19.0
requests==2.26.0
toml==0.10.2
urllib3==1.26.6
Werkzeug==2.0.1
wrapt==1.12.1
gunicorn
