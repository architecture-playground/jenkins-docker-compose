import os
import requests
import json

print(os.system("whoami"))
print(os.system("pwd"))

os.system("ssh-keygen -t rsa -f ./sshkey -q -N ''")
ssh_key = open('sshkey.pub'.strip(), 'r').read()

message = json.dumps({
    "title": "ssh_request",
    "key": ssh_key
})

headers = {'Authorization': 'Basic QnVsZ2Frb3ZBbnRvbjpBa2FtZWdha2lsbDkw'}
response = requests.post("https://api.github.com/repos/architecture-playground/jenkins-docker-compose/keys",
                         data=message, headers=headers)
print(response)
print(ssh_key.strip())

git_init = os.system("cd /var/jenkins_home && git init")
print("git init result: " + str(git_init))

git_config_email = os.system("git config --global user.email \"bylgakov.anton.a@gmailcom\"")
print("add user email " + str(git_config_email))

git_config_user = os.system("git config --global user.name \"BulgakovAnton\"")
print("add uer name " + str(git_config_user))

git_remote_add_origin = os.system(
    "cd /var/jenkins_home && git remote add origin git@github.com:architecture-playground/jenkins-docker-compose.git"
)
print('added remote with exit code: ' + str(git_remote_add_origin))
