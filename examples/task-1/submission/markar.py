import yaml
import click
import os
import requests
import subprocess
import logging
logging.basicConfig(level=logging.DEBUG)

def load_config():
    """
    load the deployment file
    """
    with open("config.yml") as f:
        conf = yaml.safe_load(f)
    return conf

@click.group()
def main():
   pass

@main.command()
#@click.pass_context
def config():
    """
    Show the current weather for a location using OpenWeatherMap data.
    """
    conf = load_config()
    print(conf.keys())
    print(conf['CREDENTIAL'].get("email"))
    if conf['CREDENTIAL'].get("email") is not None and conf['CREDENTIAL'].get("token") is not None:
        print("Credentail Already Present!")

    email = click.prompt(
        "Please enter your Email>>",
        default=None
    )
    token = click.prompt(
        "Please enter your Token>>",
        default=None
    )
    conf['CREDENTIAL']["email"] = email
    conf['CREDENTIAL']["token"] = token

    with open('config.yml', 'w') as file:
        yaml.dump(conf, file)

    print("Email: {}, token: {} ".format(email, token))

@main.command()
def local():
    """
    it will test your task/assignment locally
    """
    test_file = os.getcwd() + "/html.py"
    subprocess.call(['python', test_file])

@main.command()
def reset():
    """
    it will reset email and credential to None
    """
    conf = load_config()
    conf['CREDENTIAL']["email"] = None
    conf['CREDENTIAL']["token"] = None

    with open('config.yml', 'w') as file:
        yaml.dump(conf, file)


@main.command()
def submit():
    """
    This function will submit the file to MARKAR
    """
    conf = load_config()

    section = conf['COURSE']['section']
    coursecode = conf['COURSE']['code']

    if conf['CREDENTIAL'].get("email") is None or conf['CREDENTIAL'].get("token") is None:
        print("ERROR, Credential not present.Please run 'python markar.py config' to setup credentail")
        exit()

    email = conf['CREDENTIAL']['email']
    token = conf['CREDENTIAL']['token']

    type_ = conf['GRADER']['type']
    number = conf['GRADER']['number']

    payload = {"email": email,"token": token, "number": number, "section": section, "type": task, "coursecode": coursecode}
    
    if type_ == "Task":
        filename = "task.cpp"
    if type_ == "Assignment":
        filename = "assignment.cpp"

    try:
        files = {
        'data': (None,json.dumps(payload), 'application/json'),
        'Task-File': open(filename,'rb')
        }
    except Exception as exp:
        logging.error("Got error in load file: {}".format(str(exp)))

    outcome = requests.post(conf['URL'], files=files)
    print("++++++++++++++SERVER REPORT++++++++++++++++++++++")
    print(outcome.json)
    print("**************************************************")

@main.command()
def deadline():
    conf = load_config()

    section = conf['COURSE']['section']
    coursecode = conf['COURSE']['code']

    if conf['CREDENTIAL'].get("email") is None or conf['CREDENTIAL'].get("token") is None:
        print("ERROR, Credential not present.Please run 'python markar.py config' to setup credentail")
        exit()

    email = conf['CREDENTIAL']['email']
    token = conf['CREDENTIAL']['token']

    type_ = conf['GRADER']['type']
    number = conf['GRADER']['number']
    headers = {'Content-type': 'application/json'}

    payload = {"email": email,"token": token, "number": number, "section": section, "type": task, "coursecode": coursecode}

    outcome = requests.post(conf['URL'] + "/CheckDeadline", data=data, headers=headers)
    print("++++++++++++++SERVER Result++++++++++++++++++++++")
    print(outcome.json)
    print("**************************************************")







#out = load_deployment_file()
#print(type(out))
if __name__ == "__main__":
    main()